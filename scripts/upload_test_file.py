import os
from modules.s3_connection import get_s3_client, check_bucket_exists
from dotenv import load_dotenv
from modules.logger import logger

# Load environment variables 
load_dotenv()

def upload_test_file():
    # Get bucket name from env
    bucket = os.getenv('BUCKET_NAME')
    if not bucket:
        logger.error("BUCKET_NAME environment variable not set")
        return False

    # Check bucket exists
    s3_client = get_s3_client()
    if not check_bucket_exists(bucket, s3_client):
        logger.error("Bucket '%s' not found or not accessible", bucket)
        logger.error("Check your credentials and bucket name")
        return False

    logger.info("Creating test markdown content")
    # Create simple test markdown content
    test_content = """# Paul Xue

This one is *packed* with golden nuggets.

Paul built his development shop (Spacestation Labs) on targeting startups.
It feels natural cause startups generally need to do dev work.

It can also feel counter-intuitive because startups do tend to hire in-house.
So a big way Paul handles that is through…

## Timing the fundraising cycle

Turns out there's a pattern of startups rasing, hiring people, and 12 months later when they need to raise again looking for contractors.
I've seen this once too.

It makes sense because they're in a "crunch time" of "let's push this one feature out to make investors optimistic".
So that's when you approach them.
Or at least when you pitch them.

## You're problem isn't sales, it's marketing

This one's a pattern already.
It's what [Jamon](https://alexlazar.dev/on-consulting-with-jamon-holmgren/) kind of said as well.

Your problem is likely not sales i.e. converting the lead.
Your problem likely is the top of the funnel i.e. finding enough leads.

That's actually quite true for me with [LeetSoftware](https://leetsoftware.com/).
It's not that we're not good.
I think we're great.
And I think, and have been told, that I have a good personality too.

The problem is I barely got to pitch our services to leads.

## So how do you fix the top of funnel?

- your network, people you meet at events, etc
- twitter, reddit, social media in general
- [youtube content](https://x.com/dabit3/status/1848725955813970353) & content in general

The usual suspects.

One thing which I appreciate a lot about Paul is he called me out on some BS I said.
More particularly on this assumption I haven't actually tested.

My thinking was "all these (networking, twitter, youtube) are great, but they're not going to pay off short-term".
But have I validated that?
Not really, no.

He pointed out how the designer community does this really well on twitter by showing sample work in public.
He pointed out he's met people that did this consistently for a 2-3 months and found work from it.

It's a bit harder to do the same for dev work sometimes.
But I can't discount this strategy if I haven't done it.

Made me genuinely consider if I should build some projects for "fake" clients in public to showcase my skills.
I *should* do this…
(I'm going to be so dissapointed in me if I don't at least test this strategy)

## The interview

There's a few other things we touched on like enterprise sales.
And obviously text can't contain nuance the same way that voice and video can.
Give it a watch."""

    # Upload the file
    try:
        file_key = "test_doc.md"
        logger.debug("Uploading test file to %s/%s", bucket, file_key)
        s3_client.put_object(
            Bucket=bucket,
            Key=file_key,
            Body=test_content,
            ContentType='text/markdown'
        )
        logger.info("Successfully uploaded test file to %s/%s", bucket, file_key)
        return True
    except Exception as e:
        logger.error("Failed to upload file: %s", str(e))
        return False

if __name__ == "__main__":
    success = upload_test_file()
    if not success:
        exit(1)
