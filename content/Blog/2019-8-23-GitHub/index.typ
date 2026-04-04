#import "../index.typ": template, tufted
#show: template.with(
  title: "博客的创建",
  description: "如何免费使用GitHub创建博客",
  date: datetime(year: 2019, month: 8, day: 23),
  lang: "zh",
  image-path: "/assets/img/home-bg.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
