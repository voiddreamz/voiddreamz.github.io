#!/usr/bin/env python3
"""
Convert Jekyll markdown posts to Typst folder structure.

This script converts Jekyll markdown blog posts (with YAML front matter)
to the Tufted Typst blog template structure, where each post becomes a folder
containing index.typ and post.md files.

Usage:
    python jekyll_to_typst.py <jekyll_posts_dir> [--output OUTPUT_DIR] [--category CATEGORY]
"""

import argparse
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml


def parse_front_matter(content: str) -> Tuple[Dict, str]:
    """
    Parse YAML front matter from Jekyll markdown file.

    Front matter should be between --- delimiters at the start of the file.

    Args:
        content: Full file content

    Returns:
        Tuple of (front_matter_dict, markdown_content)
    """
    # Match front matter: --- at start, then YAML, then --- again
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)

    if not match:
        return {}, content

    try:
        front_matter = yaml.safe_load(match.group(1))
        markdown = match.group(2)
        return front_matter or {}, markdown
    except yaml.YAMLError:
        return {}, content


def extract_date_from_filename(filename: str) -> Optional[datetime]:
    """
    Extract date from Jekyll post filename format: YYYY-MM-DD-*.md

    Args:
        filename: The filename to parse

    Returns:
        datetime object or None if not in Jekyll format
    """
    # Match Jekyll date format: YYYY-MM-DD
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", filename)
    if match:
        try:
            return datetime(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        except ValueError:
            return None
    return None


def extract_title_from_filename(filename: str) -> str:
    """
    Extract title from Jekyll post filename by removing date prefix.

    Args:
        filename: The filename to parse (without .md extension)

    Returns:
        Title string
    """
    # Remove date prefix (YYYY-MM-DD-) and the .md extension
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", filename)


def slugify(text: str) -> str:
    """
    Convert text to a slug suitable for folder names.

    Args:
        text: Text to slugify

    Returns:
        Slugified text
    """
    # Keep Chinese characters and convert to lowercase
    slug = text.lower()
    # Replace spaces and special chars with hyphens
    slug = re.sub(r"[^\w\u4e00-\u9fff-]", "-", slug)
    # Remove multiple consecutive hyphens
    slug = re.sub(r"-+", "-", slug)
    # Strip leading/trailing hyphens
    slug = slug.strip("-")
    return slug


def generate_typst_index(
    title: str,
    date: datetime,
    description: str = "",
    lang: str = "zh",
    image_path: str = "/assets/img/tag-bg-o.jpg",
    author: str = "",
    tags: List[str] = None,
) -> str:
    """
    Generate index.typ content for a Typst blog post.

    Args:
        title: Post title
        date: Post date
        description: Post description/subtitle
        lang: Language code
        image_path: Path to header image
        author: Post author (optional)
        tags: List of tags (optional)

    Returns:
        Generated Typst template code
    """
    tags = tags or []

    # Build the function call
    params = [
        f'  title: "{title}",',
        f'  description: "{description}",',
        f"  date: datetime(year: {date.year}, month: {date.month}, day: {date.day}),",
        f'  lang: "{lang}",',
        f'  image-path: "{image_path}",',
    ]

    if author:
        params.insert(2, f'  author: "{author}",')

    if tags:
        # Format tags as a Typst array of strings
        tags_str = ", ".join(f'"{tag}"' for tag in tags)
        params.append(f"  tags: ({tags_str}),")

    params_str = "\n".join(params)

    typst_content = f"""#import "../index.typ": template, tufted
#show: template.with(
{params_str}
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#cmarker.render(md, math: mitex, scope: scope)
"""

    return typst_content


def process_jekyll_post(
    markdown_file: Path,
    output_base_dir: Path,
    category: str = "Blog",
    lang: str = "zh",
) -> Tuple[bool, str]:
    """
    Process a single Jekyll markdown post and convert to Typst format.

    Args:
        markdown_file: Path to Jekyll markdown file
        output_base_dir: Base output directory (e.g., content/)
        category: Category name (default: "Blog")
        lang: Language code

    Returns:
        Tuple of (success, message)
    """
    try:
        # Read the file
        content = markdown_file.read_text(encoding="utf-8")

        # Parse front matter
        front_matter, markdown_content = parse_front_matter(content)

        # Extract metadata
        filename_stem = markdown_file.stem
        date = extract_date_from_filename(filename_stem)

        if not date and "date" in front_matter:
            # Try to parse date from front matter
            try:
                date_str = front_matter["date"]
                if isinstance(date_str, datetime):
                    date = date_str
                else:
                    date = datetime.strptime(str(date_str), "%Y-%m-%d")
            except (ValueError, TypeError):
                pass

        if not date:
            return False, f"Could not extract date from {markdown_file.name}"

        # Get title
        title = front_matter.get("title", extract_title_from_filename(filename_stem))
        description = front_matter.get("description", front_matter.get("subtitle", ""))
        author = front_matter.get("author", "")
        tags = front_matter.get("tags", [])

        # Ensure tags is a list
        if isinstance(tags, str):
            tags = [tags]
        elif not isinstance(tags, list):
            tags = []

        # Create output folder with format: YYYY-MM-DD-Title
        folder_name = f"{date.strftime('%Y-%m-%d')}-{slugify(title)}"
        output_dir = output_base_dir / category / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Write post.md (just the markdown content without front matter)
        post_md_path = output_dir / "post.md"
        post_md_path.write_text(markdown_content.strip() + "\n", encoding="utf-8")

        # Generate and write index.typ
        index_typ_content = generate_typst_index(
            title=title,
            date=date,
            description=description,
            lang=lang,
            author=author,
            tags=tags,
        )
        index_typ_path = output_dir / "index.typ"
        index_typ_path.write_text(index_typ_content, encoding="utf-8")

        return True, f"✓ Converted: {title} → {folder_name}"

    except Exception as e:
        return False, f"✗ Error processing {markdown_file.name}: {str(e)}"


def find_jekyll_posts(jekyll_dir: Path) -> List[Path]:
    """
    Find all Jekyll markdown posts in a directory.

    Supports both:
    - _posts/ directory structure (standard Jekyll)
    - Current structure where posts are directly in directories

    Args:
        jekyll_dir: Directory to search

    Returns:
        List of Path objects to markdown files
    """
    posts = []

    # Look for _posts directory (standard Jekyll structure)
    posts_dir = jekyll_dir / "_posts"
    if posts_dir.exists():
        posts.extend(posts_dir.glob("*.md"))

    # Also look for .md files directly in the directory structure
    # (for existing Tufted blog with post.md files)
    posts.extend(jekyll_dir.glob("**/post.md"))

    return list(set(posts))  # Remove duplicates


def main():
    parser = argparse.ArgumentParser(
        description="Convert Jekyll markdown posts to Typst folder structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert from _posts directory to content/Blog
  python jekyll_to_typst.py /path/to/_posts
  
  # Convert and save to custom output directory
  python jekyll_to_typst.py /path/to/_posts --output /custom/content
  
  # Convert to Docs category instead of Blog
  python jekyll_to_typst.py /path/to/_posts --category Docs
  
  # Convert existing post.md files in current blog structure
  python jekyll_to_typst.py . --category Blog
        """,
    )

    parser.add_argument(
        "jekyll_dir", type=Path, help="Path to Jekyll posts directory or blog root"
    )

    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output base directory (default: content/)",
    )

    parser.add_argument(
        "--category", "-c", default="Blog", help="Category folder name (default: Blog)"
    )

    parser.add_argument(
        "--lang", "-l", default="zh", help="Language code (default: zh)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be converted without making changes",
    )

    args = parser.parse_args()

    # Validate input directory
    if not args.jekyll_dir.exists():
        print(f"Error: Directory not found: {args.jekyll_dir}")
        return 1

    # Set output directory
    output_base = args.output or (args.jekyll_dir / "content")

    # Find Jekyll posts
    posts = find_jekyll_posts(args.jekyll_dir)

    if not posts:
        print(f"No Jekyll markdown posts found in {args.jekyll_dir}")
        print("Looking for:")
        print("  - _posts/*.md (standard Jekyll)")
        print("  - **/post.md (Tufted blog structure)")
        return 1

    print(f"Found {len(posts)} post(s) to convert\n")

    # Process each post
    successful = 0
    failed = 0

    for post_file in sorted(posts):
        if args.dry_run:
            print(f"[DRY RUN] Would process: {post_file}")
        else:
            success, message = process_jekyll_post(
                post_file,
                output_base,
                category=args.category,
                lang=args.lang,
            )
            print(message)
            if success:
                successful += 1
            else:
                failed += 1

    # Summary
    print(f"\n{'=' * 60}")
    print(f"Conversion complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

    if not args.dry_run and successful > 0:
        print(f"\nOutput location: {output_base}/{args.category}/")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    exit(main())
