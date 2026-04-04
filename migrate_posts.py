import os
import yaml
import re
import shutil
from pathlib import Path

OLD_POSTS_DIR = Path('/home/voiddreamz/doc/git/voiddreamz.github.io.bak/_posts')
NEW_BLOG_DIR = Path('/home/voiddreamz/doc/git/voiddreamz.github.io/content/Blog')

def fix_frontmatter(text):
    # Remove tabs in yaml frontmatter
    return text.replace('\t', ' ')

def parse_frontmatter(content):
    if not content.startswith('---'):
        return None, content
    end_idx = content.find('---', 3)
    if end_idx == -1:
        return None, content
    fm_text = content[3:end_idx]
    fm_text = fix_frontmatter(fm_text)
    try:
        fm = yaml.safe_load(fm_text)
        return fm, content[end_idx+3:].strip()
    except Exception as e:
        print(f"Failed to parse frontmatter: {e}")
        return None, content[end_idx+3:].strip()

def main():
    post_file = OLD_POSTS_DIR / '2020-1-31-Manjaro变Arch.md'
    with open(post_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    fm, md_content = parse_frontmatter(content)
    
    date_str = '2020-1-31'
    slug = 'Manjaro变Arch'
    
    post_dir = NEW_BLOG_DIR / f"{date_str}-{slug}"
    post_dir.mkdir(exist_ok=True, parents=True)
    
    title = fm.get('title', slug) if fm else slug
    desc = fm.get('subtitle', '') if fm else ''
    date_parts = date_str.split('-')
    year, month, day = date_parts[0], date_parts[1], date_parts[2]
    
    img_path_str = ''
    if fm and 'header-img' in fm:
        img_val = fm['header-img']
        if img_val.startswith('img/'):
            img_path_str = f'image-path: "/assets/{img_val}",'
            
    md_content = re.sub(r'!\[([^\]]*)\]\((/?img/[^\)]+)\)', r'![\1](/assets/\2)', md_content)
    md_content = re.sub(r'src=["\'](/?img/[^"\']+)["\']', r'src="/assets/\1"', md_content)
    
    with open(post_dir / 'post.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    typ_content = f'''#import "../index.typ": template, tufted
#show: template.with(
  title: "{title}",
  description: "{desc}",
  date: datetime(year: {year}, month: {month}, day: {day}),
  lang: "zh",
  {img_path_str}
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#cmarker.render(md, math: mitex, scope: scope)
'''
    with open(post_dir / 'index.typ', 'w', encoding='utf-8') as f:
        f.write(typ_content)

if __name__ == '__main__':
    main()
