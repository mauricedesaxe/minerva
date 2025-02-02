# Minerva

Turn your S3 documents into a searchable knowledge base for easy RAG applications.

- Self-hosted for complete control over your data.
- Easy to setup and use.
- Smart chunking strategy for better context awareness.
- Reranking for better search results.
- OpenAI & self-hosted embedding models compatible.

## Quick Start (for development)

1. Set up environment:
```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Turn on the server:
```bash
uvicorn api.main:app --reload --log-level debug
```

## Docker

### Using Docker Compose (Recommended)

1. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

2. Use Docker Compose to start the service:

```bash
# Build and start the services
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down
```

The Docker setup includes:
- Automatic health checks
- Volume persistence for SQLite and ChromaDB databases
- Resource limits and memory management
- Environment variable configuration via .env file

## What is RAG?

RAG = retrieval augmented generation.

For example, let’s imagine Les Miserables by Victor Hugo is a private, secret book that only we have.
And you want your LLM to be able to answer to queries based on it in a correct way.
But, since in this hypothetical world the book is not public, the LLM would never have been trained on it.
And so it would never know correct answers.

How do we make it know?
We provide the appropriate context to it alongside the query.

Instead of just asking the LLM: `“What were the circumstances that led M. Charles Myriel to become a priest after returning from Italy? What role did the French Revolution play in his transformation?”` and expecting it to know, which it won’t here.

We could provide a relevant piece of information from the book, like so:
```
{
 "text": "The Revolution came; events succeeded each other with precipitation; the parliamentary families, decimated, pursued, hunted down, were dispersed. M. Charles Myriel emigrated to Italy at the very beginning of the Revolution. There his wife died of a malady of the chest, from which she had long suffered. He had no children. What took place next in the fate of M. Myriel? The ruin of the French society of the olden days, the fall of his own family, the tragic spectacles of '93, which were, perhaps, even more alarming to the emigrants who viewed them from a distance, with the magnifying powers of terror,--did these cause the ideas of renunciation and solitude to germinate in him? Was he, in the midst of these distractions, these affections which absorbed his life, suddenly smitten with one of those mysterious and terrible blows which sometimes overwhelm, by striking to his heart, a man whom public catastrophes would not shake, by striking at his existence and his fortune? No one could have told: all that was known was, that when he returned from Italy he was a priest.",
 "metadata": {
   "chunk": 8,
   "embedded_at": "2025-01-12T21:22:20.375498",
   "source": "les_miserables.md"
 },
 "similarity": 1
},
```

Well, now the LLM would know the answer and could use its natural language ability to produce a very accurate response.

RAG is all about this.
How do we do the above in an automatic, accurate and feasible way?

While in the past year this has come to be known as an “applied AI” problem.
At heart it really is a search problem.

## The search problem explained

If you’ve ever worked on search problems before, you might already know what “semantic search” is.

If you haven’t, well, you probably already know keyword-search.
You look through text to see if the keywords in the query match and there’s your result.
But that’s rudimentary and won’t find all relevant information.

Semantic search doesn’t look for exact words, but for meaning.
So `“football”` and `“soccer”` might have a semantic similarity of anywhere between 70% and 95% depending on what model you use.

This is also called vector search sometimes.
And that’s because you are vectorizing the pieces of text and then comparing the vectors.

A vector is a set of coordinates (sort of) in a database that map to concepts.
This illustration should help you visualize things and you might already have an idea of how RAG works now.
![](/docs/images/vectoried_concepts_illustration.png)<!-- {"width":346} -->

So you get the user query, vectorize it (also called embedding) and turn it into coordinates.
You use these to look through your database to find other similar data points.
And you return them, sorted by similarity.

This is a big part of what RAG is about.
But it’s not the only thing.

## How you can do RAG in the most rudimentary way

Another big part of RAG is how you vectorize/embed your data.

Different models have different abilities.

But even beyond that, there’s many ways you can choose to structure your data before embedding it.

Earlier I showed you `“football”` and `“soccer”`.

But you could also embed full sentences: `"I love football so much I could watch it all day"` and `"I watch soccer all day because I like it a lot"` have a similarity of 75% (if embedded with `all-minilm`).

Hey, you could even embed paragraphs and even bigger ~chunks~ (you’ll see this word a lot from now on).
How big the chunk that produces the embedding can be depends on what model you pick.
To give you a sense of size of text, the Les Miserables example you saw above was an actual 
example we’ve tested Minerva with.

The simplest way you could do RAG is to do what is called “crude chunking”.
You figure out what is a good size for your embedding model, let’s call it `2000` characters for now.
You take your text and code a simple script to split it every `2000`, maybe do a bit of overlap so context is not lost.
The resulting chunks you pass to and embedding model and put in a vector database.

Now you can take a user query, embed it and compare the produced vector with what you have in the database.

Hopefully you get good results in the search too.
But, if I’m being honest with you, most “applied AI” engineers nowadays don’t do crude chunking anymore (the above) because it’s not as good as other options.

## How we do chunking/embedding for RAG and why it's really fucking amazing compared to rudimentary way

There are different strategies you can have when chunking your data (or feed it into the LLM at user query time).

A few common problems:
- Your chunks could be too big and you might end up providing too much context so the LLM gets “confused”.
- Chunks might be too small so context is lost when embedding (i.e. search won’t return them as expected) or when provided into the LLM.
- Duplicate/similar info clould confuse" the system

It’s important to test ideas for your specific use case, I’d say.
But there are common best practices.

A solid one that we have seen a surprising amount of people not do is "semnatic chunking".

I’m being unrealistic here about chunk size, but with crude chunking you could have a situation like this:
```
[
	"I watch soccer all day bec",
	"ause I like it a lot"
]
```

This could very well result in lost context when creating the embedding, even if you use overlaps.

Semantic chunking, at least the way we do it, tries to first fit in a full section (defined by headings within the text), if not we attempt a paragraph, then a sentence, then a part of a sentence with a word break.

This means that you’ll often have chunks that are semantically meaningful.
Look at the earlier Les Miserables by Victor Hugo stuff, that was a real chunk generated by Minerva.

This is quite possibly the single most important part of your RAG setup aside from what model you use for embeddings. And we do it by default.

You’ll see Minerva is set up with a lot of opinionated, but in our opinion good, defaults like this to make your life easier.

## The simplest, lowest config way to set up Minerva

If the goal is “simple, low config, fast” we suggest:
- go with our already made `Dockerfile` and `docker-compose.yml`
- use any S3 provider that you like
- go with OpenAI for models (simple to use, solid models)

I won’t sit here and explain how to use Docker.

But I will say you need to set your own variables.
You can use `.env.example` for an example.

For an OpenAI setup, make sure you have these:
```
OPENAI_API_KEY="your_openai_api_key"
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
BUCKET_NAME="spacestation-labs-companion"
STORAGE_URL="https://storage.googleapis.com" # if not using AWS
```

You can also add `API_KEY` if you want to protect your API with basic authentication.

That’s it.
Deploy it with your infra provider of choice.
Make sure you persist SQLite and Chroma if you haven’t used our `docker-compose.yml` file

## How to use Minerva 101 (how to process a file, how to search)

Go to `https://<the_URL_you_deployed_to>/docs` to see the Swagger UI generated based on the API endpoints.

You’ll see every endpoint you can interact with here.

Most of the time, you’ll only care about `/documents/process` and `/search` because these allow you to handle the core functionality.

If you play around with the Swagger UI you’ll see it generates curl examples based on the queries you run, like so:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/documents/process' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "bucket": "spacestation-labs-companion",
  "force_reload": true,
  "key": "les_miserables.md"
}'
```

Let’s define what the above means. Minerva will look for the provided bucket and key (file name).
If it can find them and has access to them through S3, it will download it for chunking.

The `force_reload=true` means that if the file alread exists in the vector db, we’ll replace it.
By default this is disabled (i.e.: won’t replace existent embeddings).

Chunking will happen in the background and meanwhile you’ll get a job object back like so:

```
{
  "bucket": "spacestation-labs-companion",
  "key": "les_miserables.md",
  "job_id": "d075d5fc-3759-4c82-9158-f764c27c6e48",
  "status": "processing",
  "created_at": "2025-01-12T23:31:14.718505",
  "completed_at": null,
  "chunks_processed": null,
  "error": null
}
```

For rough performance benchmarks (we’ll add automated ones later), Les Miserables usually takes less then one minute to process (depending on the used model and other factors).

You can use the `job_id` and the jobs related endpoint to monitor this.
Once the status equals `”success”` you’re good to go.
The file you’ve provided has been fully embedded.
And you can use it in search:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/search' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "limit": 5,
  "query": "What were the circumstances that led M. Charles Myriel to become a priest after returning from Italy? What role did the French Revolution play in his transformation?",
  "rerank": true
}'
```

This should return an array of these:

```
{
 "text": "The Revolution came; events succeeded each other with precipitation; the parliamentary families, decimated, pursued, hunted down, were dispersed. M. Charles Myriel emigrated to Italy at the very beginning of the Revolution. There his wife died of a malady of the chest, from which she had long suffered. He had no children. What took place next in the fate of M. Myriel? The ruin of the French society of the olden days, the fall of his own family, the tragic spectacles of '93, which were, perhaps, even more alarming to the emigrants who viewed them from a distance, with the magnifying powers of terror,--did these cause the ideas of renunciation and solitude to germinate in him? Was he, in the midst of these distractions, these affections which absorbed his life, suddenly smitten with one of those mysterious and terrible blows which sometimes overwhelm, by striking to his heart, a man whom public catastrophes would not shake, by striking at his existence and his fortune? No one could have told: all that was known was, that when he returned from Italy he was a priest.",
 "metadata": {
   "chunk": 8,
   "embedded_at": "2025-01-12T21:22:20.375498",
   "source": "les_miserables.md"
 },
 "similarity": 1
},
```

Reranking is disabled by default.

## How we do reranking and why it can be useful

Remember earlier when I said semantic search looks for meaning instead of exact words? Well, sometimes that's not enough.

Let's say you're searching through a technical document. A pure semantic search might return chunks that miss the perfect passage containing the keyword you're looking for.

This is where reranking comes in. When you set `rerank=true` in your search, here's what happens:

1. First, we cast a wider net. Instead of just getting your requested number of results (let's say 5), we get 3x that amount (15), but max 20 results.
2. For each result, we calculate two scores:
   - A semantic score (70% weight): How close the meaning is based on vector similarity
   - A keyword score (30% weight): What percentage of your query words appear in the chunk
3. We combine these scores and pick the top (5 in this case) results.

## Why you might not want to use OpenAI

I personally like OpenAI's models, but there are a few key reasons why you might not want to use them:
* latency to their servers
* privacy concerns
* rate limits
* cost at scale

Embedding when processing documents and when doing search will be so much faster if the LLM that does embeddings is on the same machine, or at least in the same data center as your application that requests embeddings.

You may have data that you simply don’t want, or due to compliance you legally can’t, have on third party servers.
A self-hosted LLM coupled with the fact that Minerva itself is self-hosted gets you out of a pickle here.

OpenAI also has its rate limits which, in maybe rare cases, may not be enough for you.
And it does have to ask for a $ amount that makes it worthwhile for them too to offer the service.
Which can be pricey at scale.

These are all cases where self-hosting LLMs / embedding models can come in handy.
I’ve seen this called MLOps in the industry.
But don’t imagine it’s some crazy new thing, it’s mostly normal Dev Ops.

Still, I think most of you won’t have these trade-offs so I’d suggest using a provider like OpenAI or Anthropic because it’s just easier.
If you do have this trade-offs, [contact me](https://alexlazar.dev/) and I’ll see if I can nudge you in the right direction.

## TODO: Topics I want to cover in our docs, but haven't yet

* how to set up minerva with local models with ollama
* how to do query destructuring and why it’s useful
* performance benchmarks (how fast can we process a file, how fast can we provide a response, where we use caching) 
