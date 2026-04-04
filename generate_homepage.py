#!/usr/bin/env python3
"""
Convert old Jekyll about.html to Typst homepage content.

Extracts the About content from the old HTML and converts it to
Typst format for the homepage.
"""

from pathlib import Path


def generate_homepage() -> str:
    """
    Generate Typst homepage content from about.html content.

    Returns:
        Generated Typst content
    """

    typst_content = """#import "config.typ": template
#show: template

= About VoidDreamZ

#block(
  fill: rgb("#f0f0f0"),
  inset: 1em,
  radius: 0.5em,
  [
    _兰生幽谷，不为莫服而不芳；_
    
    _舟行江海，不为莫乘而不浮；_
    
    _君子行义，不为莫知而止休。_
  ]
)

== Hey! 👋

Hey，我是 Void DreamZ，一名普通的科技爱好者兼中学生。

也是酷安基友一枚。酷安用户名：生来彷徨的人

== Who I Am

我热爱技术，对编程、系统和开源充满热情。这个博客记录了我的学习历程和技术思考。

== This Blog

这个博客由 Typst 和 #link("https://github.com/Yousa-Mirage/Tufted-Blog-Template")[Tufted Blog Template] 驱动。

你可以在 #link("/Blog/")[Blog] 中找到我的文章，在 #link("/CV/")[CV] 中了解我的履历，在 #link("/Docs/")[Docs] 中查看更多资源。

== Stay Hungry, Stay Foolish

_"Stay hungry, stay foolish"_ - Steve Jobs

永远保持对知识的渴望和对未知的敬畏。
"""

    return typst_content


def main():
    """Main entry point."""
    homepage_file = Path(
        "/home/voiddreamz/doc/git/voiddreamz.github.io/content/index.typ"
    )

    print("Generating homepage content from about.html...")

    # Generate content
    typst_content = generate_homepage()

    # Write to file
    homepage_file.write_text(typst_content, encoding="utf-8")

    print(f"✓ Generated: {homepage_file}")
    print(f"\nHomepage preview:")
    print("=" * 60)
    print(typst_content)
    print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
