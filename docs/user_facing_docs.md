# Minerva Documentation

## What Minerva does

Minerva helps you make documents searchable. It:
1. Takes markdown files from S3
2. Splits them into smart chunks
3. Makes chunks searchable with AI through a simple REST API endpoint
4. Lets you find stuff with normal questions

## Why should you use Minerva?

It's literally the simplest way to abstract all the work that is RAG away from you.
You just put your documents into S3, spin Minerva up on any Docker enabled server and you're done.

What is RAG (Retrieval Augmented Generation)?

RAG is when you are trying to add custom documents to your LLM's context.
Things like internal company docs, customer support docs, anything that's not on the public domain and so not in the LLM's training data.

Unlike other RAG solutions, Minerva is not a library. It's a standalone, self-hosted, open source API.

Unlike some of our competitors, we offer intelligent chunking and search.
We offer, dare I say, great defaults, but also full configurability.

Since you are self-hosting, there are no GDPR, SOC2 or general compliance concerns.

You have to source code so we can't run away and take the product (or your data) with us.
And you can modify it to your needs.

## What are the costs involved?

We offer Minerva entirely for free to the community.
But that doesn't mean zero costs.

You will have to pay for:
- S3 storage
- a server to run Minerva on
- embedding model costs (we use OpenAI at this particular moment, but we'll add more options in the future)

Our estimations is that a SME will probably start by spending $20/month on these and not grow much from there.

## What's the expected processing time for documents?

Right now we are looking at roughly 23 KB/second of markdown.
For the average company who has under 200MB, that means roughly 2.5 hours to process all documents.

Not too bad, but we have a roadmap for optimizations and this will improve.

## S3 Setup

Minerva needs read-only access to your S3 bucket. You'll need:

1. AWS credentials with these permissions:
```json
{
    "Version": "2012-10-17",
    "Statement": [
    {
        "Effect": "Allow",
        "Action": [
        "s3:HeadBucket",
        "s3:GetObject"
        ],
        "Resource": [
        "arn:aws:s3:::your-bucket",
        "arn:aws:s3:::your-bucket/*"
        ]
    }
    ]
}
```

2. Environment variables:
```bash
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
STORAGE_URL=optional_custom_endpoint  # Only if using S3-compatible storage
```

Note: You can use any S3-compatible storage (like MinIO, DigitalOcean Spaces, etc) by setting the STORAGE_URL.

## Quick Example of how to use Minerva

```python
# 1. Start job to process document
response = requests.post(
    "http://your-minerva-api/api/v1/documents/process",
    headers={"X-API-Key": "your-key"},
    json={
        "bucket": "my-bucket",
        "key": "docs/example.md"
    }
)

# 2. Check job status
status = requests.get(
    f"http://your-minerva-api/api/v1/documents/jobs/{job_id}",
    headers={"X-API-Key": "your-key"}
)

# 3. Search document
results = requests.post(
    "http://your-minerva-api/api/v1/search",
    headers={"X-API-Key": "your-key"},
    json={
        "query": "What is Minerva?",
        "limit": 5
    }
)
```

## Basic Rules

- Only process markdown (.md) files
- Files must be in S3
- Files must be under 5MB
- Need API key for all requests
- All responses in JSON

## How Search Work?

1. You can ask question in normal words
2. Question turned into AI embedding
3. Find chunks most similar to question
4. Return chunks with source info

Example response:
```json
{
    "results": [
        {
            "text": "chunk of text that matches",
            "metadata": {
                "source": "docs/example.md",
                "chunk": 0
            },
            "similarity": 0.95
        }
    ]
}
```

## Smart Chunking explained

Minerva splits documents in smart way:
1. First we try to split into sections at headings (# ## ###)
2. If chunks too big, split at paragraphs
3. If still too big, split at sentences
4. If still too big (rare), split at words

This make chunks keep meaning better than crude splitting where you could have ended up with chunks like these:
```
[
    "This is a paragraph about the docu",
    "ment and what it does",
]
```

Generally, you want your chunks to be meaningful.
A chunk should encapsulate a single idea or concept and it should do it well.

That is because embedding models basically transform your chunk into a vector (a set of coordinates).
So if your text doesn't represent the concept well, the vector will be bad.

## Processing Options

When processing a document you have the option to provide the following:
```json
{
    "bucket": "s3-bucket-name", // this is the bucket where your document is stored
    "key": "path/to/file.md", // this is the path to your document
    "force_reload": false  // (optional) set true to reprocess
}
```

`force_reload` is useful if you want to reprocess a given document within the system.
Maybe you've processed `docs/how_to_use_minerva.md` yesterday and now it changed.

## Job Status Response

When checking a job you get a response like this:
```json
{
    "job_id": "unique-id",
    "status": "processing|completed|failed", 
    "created_at": "timestamp",
    "completed_at": "timestamp or null",
    "file_info": {
        "bucket": "s3-bucket-name",
        "key": "path/to/file.md"
    },
    "result": {
        "chunks_processed": 42,
        "error": "error message if failed"
    }
}
```

## Search Options

When searching you can provide the following:
```json
{
    "query": "your question here",
    "limit": 5  // how many results you want
}
```

## Swagger Docs

We won't document all the endpoints here, but you can check them out at: `http://your-minerva-api/docs`

## Coming Soon

We are looking at an early version of Minerva right now.

Here are some things we are working on:
- More file types (PDF, DOCX)
- Webhooks when a job is done
- Delete documents from S3 / Vector DB
- Different improvements in chunking and search

## Need Help?

Check API docs at: `http://your-minerva-api/docs` 
Or contact us on X ([Alex](https://x.com/_alexlazar_) or [Paul](https://x.com/pxue))
