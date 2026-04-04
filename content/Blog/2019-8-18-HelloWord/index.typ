#import "../index.typ": template, tufted
#show: template.with(
  title: "Hello World",
  description: "博客正式成立",
  date: datetime(year: 2019, month: 8, day: 18),
  lang: "zh",
  image-path: "/assets/img/tag-bg-o.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
