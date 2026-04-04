#!/usr/bin/env python3
"""
Generate dynamic Blog index for Typst blog.

Scans all post directories in content/Blog/, groups them by year,
and generates a Typst index.typ file with links to all posts.
"""

import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


def extract_date_and_title(dirname: str) -> Tuple[datetime, str]:
    """
    Extract date and title from directory name format: YYYY-MM-DD-title

    Args:
        dirname: Directory name

    Returns:
        Tuple of (datetime, title)
    """
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)", dirname)
    if match:
        year, month, day, title = match.groups()
        date = datetime(int(year), int(month), int(day))
        # Convert slug to readable title (replace hyphens with spaces, title case)
        readable_title = title.replace("-", " ").title()
        return date, readable_title
    return None, None


def extract_title_from_index(post_dir: Path) -> str:
    """
    Try to extract title from index.typ file in post directory.
    Falls back to directory name title.

    Args:
        post_dir: Path to post directory

    Returns:
        Post title
    """
    index_file = post_dir / "index.typ"
    if index_file.exists():
        try:
            content = index_file.read_text(encoding="utf-8")
            # Look for: title: "..."
            match = re.search(r'title:\s*"([^"]+)"', content)
            if match:
                return match.group(1)
        except Exception:
            pass

    # Fallback to directory name
    return extract_date_and_title(post_dir.name)[1]


def get_all_posts(blog_dir: Path) -> List[Tuple[datetime, str, str]]:
    """
    Get all posts organized with date, slug name, and title.

    Args:
        blog_dir: Path to Blog directory

    Returns:
        List of (date, slug, title) tuples, sorted by date descending
    """
    posts = []

    for item in blog_dir.iterdir():
        if item.is_dir() and not item.name.startswith("_"):
            date, _ = extract_date_and_title(item.name)
            if date:
                title = extract_title_from_index(item)
                posts.append((date, item.name, title))

    # Sort by date, newest first
    posts.sort(key=lambda x: x[0], reverse=True)
    return posts


def group_posts_by_year(
    posts: List[Tuple[datetime, str, str]],
) -> Dict[int, List[Tuple[datetime, str, str]]]:
    """
    Group posts by year.

    Args:
        posts: List of (date, slug, title) tuples

    Returns:
        Dictionary mapping year to list of posts
    """
    grouped = {}
    for date, slug, title in posts:
        year = date.year
        if year not in grouped:
            grouped[year] = []
        grouped[year].append((date, slug, title))

    return grouped


def generate_typst_index(blog_dir: Path) -> str:
    """
    Generate complete Typst index.typ content for the Blog.

    Args:
        blog_dir: Path to Blog directory

    Returns:
        Generated Typst content
    """
    posts = get_all_posts(blog_dir)
    grouped = group_posts_by_year(posts)

    # Generate header
    typst_content = """#import "index.typ": template, tufted
#show: template.with(
  title: "Blog",
  description: "Articles and thoughts",
  lang: "zh",
)

"""

    typst_content += "= Blog Posts\n\n"

    # Generate content by year
    years = sorted(grouped.keys(), reverse=True)

    for year in years:
        typst_content += f"== {year}\n\n"

        # Sort posts in this year by date, newest first
        year_posts = sorted(grouped[year], key=lambda x: x[0], reverse=True)

        for date, slug, title in year_posts:
            date_str = date.strftime("%B %d, %Y")  # e.g., "November 15, 2019"
            typst_content += f"- [{title}](/{slug}/) _{date_str}_\n"

        typst_content += "\n"

    return typst_content


def main():
    """Main entry point."""
    blog_dir = Path("/home/voiddreamz/doc/git/voiddreamz.github.io/content/Blog")

    if not blog_dir.exists():
        print(f"Error: Blog directory not found: {blog_dir}")
        return 1

    print(f"Scanning Blog directory: {blog_dir}")

    # Get all posts
    posts = get_all_posts(blog_dir)

    if not posts:
        print("No blog posts found!")
        return 1

    print(f"Found {len(posts)} post(s)\n")

    # Group by year
    grouped = group_posts_by_year(posts)

    # Show summary
    print("Posts by year:")
    for year in sorted(grouped.keys(), reverse=True):
        count = len(grouped[year])
        print(f"  {year}: {count} post(s)")

    print()

    # Generate index
    typst_content = generate_typst_index(blog_dir)

    # Write to file
    index_file = blog_dir / "index.typ"
    index_file.write_text(typst_content, encoding="utf-8")

    print(f"✓ Generated: {index_file}")
    print(f"\nIndex preview (first 50 lines):")
    print("=" * 60)
    lines = typst_content.split("\n")
    for line in lines[:50]:
        print(line)
    if len(lines) > 50:
        print(f"... ({len(lines) - 50} more lines)")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
