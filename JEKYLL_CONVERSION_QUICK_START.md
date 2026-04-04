# Jekyll to Typst Converter - Quick Start

## Installation

```bash
pip install pyyaml
```

## Basic Commands

### Convert from Jekyll _posts directory
```bash
python jekyll_to_typst.py /path/to/_posts
```

### Preview changes without converting
```bash
python jekyll_to_typst.py /path/to/_posts --dry-run
```

### Convert to custom output location
```bash
python jekyll_to_typst.py /path/to/_posts --output /my/content
```

### Convert to different category
```bash
python jekyll_to_typst.py /path/to/_posts --category Docs
```

### Convert with English language
```bash
python jekyll_to_typst.py /path/to/_posts --lang en
```

## Output Structure

Each converted post creates a folder like this:

```
content/Blog/2024-01-15-post-title/
├── index.typ          # Typst template with metadata
└── post.md            # Markdown content
```

## Supported Input Formats

### Jekyll filename (date in name)
```
_posts/2024-01-15-my-post.md
```

### Jekyll with YAML front matter
```markdown
---
title: My Post Title
description: Optional subtitle
date: 2024-01-15
author: Your Name
tags:
  - tag1
  - tag2
---

# Content starts here...
```

## After Conversion

Build your site:
```bash
python build.py build
python build.py preview
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No posts found | Check posts are in `_posts/` with `.md` extension |
| Date parsing errors | Use `YYYY-MM-DD-title.md` format or add `date:` to front matter |
| Encoding errors | Ensure files are UTF-8 encoded |

## All Options

```
--output, -o PATH      Output directory (default: content/)
--category, -c STRING  Category folder (default: Blog)
--lang, -l STRING      Language code (default: zh)
--dry-run             Preview without changes
```

For detailed documentation, see `JEKYLL_CONVERSION_GUIDE.md`
