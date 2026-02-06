import os
import re
import shutil
# import pillow
from pathlib import Path
from datetime import datetime

from pdf2image import convert_from_path
from PIL import Image

from blessings import Terminal
term = Terminal()
green = term.green
bred = term.bold_red
byellow = term.bold_yellow


ROOT_DIR = Path("./input_zines") 

SCRIPT_DIR = Path(__file__).parent.resolve()
CONTENT_DIR = SCRIPT_DIR / "content"
IMAGES_DIR = CONTENT_DIR / "images"
LIBRARY_DIR = CONTENT_DIR / "library"

CONTENT_DIR.mkdir(exist_ok=True)
IMAGES_DIR.mkdir(exist_ok=True)
LIBRARY_DIR.mkdir(exist_ok=True)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")

def sanitize_path_part(text: str) -> str:
    text = text.lower()
    text = text.replace("&", "and")
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"[^a-z0-9_-]", "", text)
    return text

def clean_title(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text.rstrip(" -–—:")


def parse_title_and_author_from_filename(pdf_path: Path):
    base = pdf_path.stem
    if " - " in base:
        title_part, author_part = base.rsplit("-", 1)
        return clean_title(title_part), clean_title(author_part)
    return clean_title(base), ""


def get_category_and_tags(pdf_path: Path):
    relative = pdf_path.parent.relative_to(ROOT_DIR)
    parts = list(relative.parts)
    category = parts[0].replace("&", "and").title() if parts else ""
    tags = [
        p.replace("&", "and").lower().replace(" ", "_")
        for p in parts[1:]
    ]
    return category, tags


def markdown_path_for_pdf(pdf_path: Path) -> Path:
    relative = pdf_path.relative_to(ROOT_DIR).with_suffix("")
    slug = slugify("-".join(relative.parts))
    return CONTENT_DIR / f"{slug}.md"

def copied_pdf_path(pdf_path: Path) -> Path:
    relative = pdf_path.relative_to(ROOT_DIR)
    sanitized_parts = []
    for part in relative.parts:
        if part.lower().endswith(".pdf"):
            stem = Path(part).stem
            suffix = Path(part).suffix  # problems here before
            sanitized_name = sanitize_path_part(stem) + suffix
            sanitized_parts.append(sanitized_name)
        else:
            sanitized_parts.append(sanitize_path_part(part))

    dest = LIBRARY_DIR.joinpath(*sanitized_parts)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        shutil.copy2(pdf_path, dest)
    return dest


def cover_image_path_for_pdf(pdf_path: Path) -> Path:
    md_path = markdown_path_for_pdf(pdf_path)
    return IMAGES_DIR / f"{md_path.stem}.jpg"


def generate_cover_image(pdf_path: Path) -> Path:
    cover_path = cover_image_path_for_pdf(pdf_path)
    if cover_path.exists():
        return cover_path
    images = convert_from_path(
        pdf_path,
        first_page=1,
        last_page=1,
        dpi=200
    )
    page = images[0]
    width, height = page.size
    right_half = page.crop((width // 2, 0, width, height))
    right_half.convert("RGB").save(cover_path, "JPEG", quality=90)
    return cover_path


def create_markdown(pdf_path: Path):
    md_path = markdown_path_for_pdf(pdf_path)
    if md_path.exists():
        print(byellow(f"Skipping existing: {md_path}"))
        return
    title, author = parse_title_and_author_from_filename(pdf_path)
    slug = slugify(title)
    category, tags = get_category_and_tags(pdf_path)
    copied_pdf = copied_pdf_path(pdf_path)
    cover_path = generate_cover_image(pdf_path)
    rel_pdf = copied_pdf.relative_to(CONTENT_DIR).as_posix()
    today = datetime.today().strftime("%Y-%m-%d")
    front_matter = [
        "---",
        f"Title: {title}",
        f"Date: {today}",
        f"Slug: {slug}",
        f"Category: {category}",
        f"Tags: {', '.join(tags)}",
        "Summary:",
    ]
    if author:
        front_matter.append(f"Author: {author}")
    front_matter.extend([
        f"Cover: {{static}}/images/{cover_path.name}",
        f"PDF: {{static}}/{rel_pdf}",
        "---",
        "",
        f'<img src="{{static}}/images/{cover_path.name}" width="200" />',
        "",
        f"[Download imposed PDF]({{static}}/{rel_pdf})",
        "",
    ])

    md_path.write_text("\n".join(front_matter), encoding="utf-8")
    print(bgreen(f"Created: {md_path}"))


def main():
    for root, _, files in os.walk(ROOT_DIR):
        for name in files:
            if name.lower().endswith(".pdf"):
                pdf_path = Path(root) / name
                try:
                    create_markdown(pdf_path)
                except Exception as e:
                    print(bred(f"Failed processing {pdf_path}: {e}"))


if __name__ == "__main__":
    main()

