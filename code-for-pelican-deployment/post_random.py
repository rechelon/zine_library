import os
import random
import frontmatter
from pathlib import Path
from PIL import Image

import tweepy

from atproto import Client as BlueskyClient

from instagrapi import Client as InstaClient


OUTPUT_DIR = Path("./output")


def pick_random_markdown():
    md_files = list(OUTPUT_DIR.glob("*.md"))
    if not md_files:
        raise Exception("No markdown files found in output/")
    return random.choice(md_files)


def parse_post(md_path):
    post = frontmatter.load(md_path)
    title = post.get("Title", "")
    summary = post.get("Summary", "")
    slug = post.get("Slug", "")
    cover = post.get("Cover")
    if not cover:
        raise Exception(f"No Cover field in {md_path}")

    cover_path = cover.replace("{static}", "output")
    cover_path = Path(cover_path)

    if not cover_path.exists():
        raise Exception(f"Cover image not found: {cover_path}")

    caption = f"{title}\n\n{summary}" if summary else title

    return caption.strip(), cover_path




def post_to_twitter(image_path, caption):
    auth = tweepy.OAuth1UserHandler(
        os.environ["TWITTER_API_KEY"],
        os.environ["TWITTER_API_SECRET"],
        os.environ["TWITTER_ACCESS_TOKEN"],
        os.environ["TWITTER_ACCESS_SECRET"],
    )

    api = tweepy.API(auth)

    media = api.media_upload(str(image_path))
    api.update_status(status=caption[:280], media_ids=[media.media_id])



def post_to_bluesky(image_path, caption):
    client = BlueskyClient()
    client.login(
        os.environ["BLUESKY_HANDLE"],
        os.environ["BLUESKY_PASSWORD"],
    )

    with open(image_path, "rb") as f:
        img_data = f.read()

    upload = client.upload_blob(img_data)

    client.send_post(
        text=caption,
        embed={
            "$type": "app.bsky.embed.images",
            "images": [
                {
                    "image": upload.blob,
                    "alt": caption,
                }
            ],
        },
    )


def post_to_instagram(image_path, caption):
    client = InstaClient()
    client.login(
        os.environ["INSTAGRAM_USERNAME"],
        os.environ["INSTAGRAM_PASSWORD"],
    )

    client.photo_upload(
        path=str(image_path),
        caption=caption,
    )


def main():
    md_file = pick_random_markdown()
    caption, image_path = parse_post(md_file)

    print(f"Posting {md_file.name} with image {image_path}")

    post_to_twitter(image_path, caption)
    post_to_bluesky(image_path, caption)
    post_to_instagram(image_path, caption)

    print("Posted successfully.")


if __name__ == "__main__":
    main()

