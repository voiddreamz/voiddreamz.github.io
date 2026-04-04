# Jekyll to Typst Converter - Examples

This document shows real examples of how the converter works.

## Example 1: Simple Post with Front Matter

### Input (Jekyll)

**File**: `_posts/2024-01-15-getting-started.md`

```markdown
---
title: Getting Started with Typst
description: A beginner's guide
date: 2024-01-15
author: Jane Doe
tags:
  - typst
  - tutorial
---

# Getting Started with Typst

Typst is amazing!

## Why Typst?

- Fast compilation
- Better syntax than LaTeX
- Native PDF output
```

### Output (Typst)

**Directory Structure**:
```
content/Blog/2024-01-15-getting-started-with-typst/
├── index.typ
└── post.md
```

**Generated index.typ**:
```typst
#import "../index.typ": template, tufted
#show: template.with(
  title: "Getting Started with Typst",
  description: "A beginner's guide",
  date: datetime(year: 2024, month: 1, day: 15),
  lang: "zh",
  image-path: "/assets/img/tag-bg-o.jpg",
  author: "Jane Doe",
  tags: ("typst", "tutorial"),
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#cmarker.render(md, math: mitex, scope: scope)
```

**Generated post.md** (front matter removed):
```markdown
# Getting Started with Typst

Typst is amazing!

## Why Typst?

- Fast compilation
- Better syntax than LaTeX
- Native PDF output
```

## Example 2: Jekyll Filename Format (Date in Name)

### Input

**File**: `_posts/2024-02-20-python-tips.md`

```markdown
# Python Tips

Some Python best practices...
```

### Output

**Directory**: `content/Blog/2024-02-20-python-tips/`
- Title extracted from filename: "python tips" → "Python Tips"
- Date extracted from filename: 2024-02-20

## Example 3: Advanced Post with Custom Image

### Input

```markdown
---
title: Advanced Typst Layouts
description: Create complex document layouts
date: 2024-03-10
author: Bob Smith
tags:
  - advanced
  - layouts
  - design
image-path: /assets/img/custom-header.jpg
---

# Advanced Layouts

Let's create some beautiful layouts!
```

### Output

The `image-path` from front matter overrides the default header image:

```typst
#import "../index.typ": template, tufted
#show: template.with(
  title: "Advanced Typst Layouts",
  description: "Create complex document layouts",
  date: datetime(year: 2024, month: 3, day: 10),
  lang: "zh",
  image-path: "/assets/img/custom-header.jpg",
  author: "Bob Smith",
  tags: ("advanced", "layouts", "design"),
)
```

## Example 4: Batch Conversion

### Command
```bash
python jekyll_to_typst.py _posts/ --lang en
```

### Input Structure
```
_posts/
├── 2024-01-15-first-post.md
├── 2024-02-20-second-post.md
├── 2024-03-10-third-post.md
└── 2024-04-05-fourth-post.md
```

### Output Structure
```
content/Blog/
├── 2024-01-15-first-post/
│   ├── index.typ
│   └── post.md
├── 2024-02-20-second-post/
│   ├── index.typ
│   └── post.md
├── 2024-03-10-third-post/
│   ├── index.typ
│   └── post.md
└── 2024-04-05-fourth-post/
    ├── index.typ
    └── post.md
```

## Example 5: Converting Existing post.md Files

If you already have a Tufted blog with `post.md` files, you can reorganize them:

### Command
```bash
python jekyll_to_typst.py . --category Blog
```

The script will find all `post.md` files and ensure they follow the standard structure.

## Example 6: Using Dry-Run

### Command
```bash
python jekyll_to_typst.py _posts/ --dry-run
```

### Output
```
Found 5 post(s) to convert

[DRY RUN] Would process: 2024-01-15-first-post.md
[DRY RUN] Would process: 2024-02-20-second-post.md
[DRY RUN] Would process: 2024-03-10-third-post.md
[DRY RUN] Would process: 2024-04-05-fourth-post.md
[DRY RUN] Would process: 2024-05-01-fifth-post.md

============================================================
Conversion complete!
Successful: 0
Failed: 0
```

This shows what *would* be converted without actually making changes. Perfect for verifying before running the real conversion!

## Example 7: Chinese Title Handling

### Input
```
_posts/2024-01-15-我的第一篇文章.md
```

### Output Folder
```
content/Blog/2024-01-15-我的第一篇文章/
```

The script preserves Chinese characters in folder names and generates proper Typst templates.

### Generated index.typ
```typst
#show: template.with(
  title: "我的第一篇文章",
  description: "",
  date: datetime(year: 2024, month: 1, day: 15),
  lang: "zh",
  image-path: "/assets/img/tag-bg-o.jpg",
)
```

## Tips for Best Results

1. **Use consistent date format**: Always use `YYYY-MM-DD` in filenames or front matter
2. **Add descriptions**: Including a `description` field makes posts more discoverable
3. **Organize with tags**: Use tags to categorize your content
4. **Custom images**: Use the `image-path` field for post-specific header images
5. **Dry run first**: Always test with `--dry-run` before converting
6. **Backup original**: Keep your `_posts/` directory as backup

## Troubleshooting Examples

### Problem: "Could not extract date"

**Incorrect**: `my-post.md` (no date in filename)
**Correct**: `2024-01-15-my-post.md` (Jekyll format)

Or add to front matter:
```yaml
date: 2024-01-15
```

### Problem: Invalid YAML in front matter

**Incorrect**:
```yaml
---
title: My Post
tags: tag1, tag2
---
```

**Correct**:
```yaml
---
title: My Post
tags:
  - tag1
  - tag2
---
```

### Problem: Special characters in title

**Input**: `2024-01-15-Python & Rust Tips!.md`
**Output folder**: `2024-01-15-python-rust-tips/` (slugified)

The script automatically converts special characters to hyphens and preserves readability.

---

For more details, see the [full conversion guide](JEKYLL_CONVERSION_GUIDE.md).
