#import "../index.typ": template, tufted
#show: template.with(
  title: "学了C++后第一次写Python",
  description: "Python",
  date: datetime(year: 2020, month: 1, day: 20),
  lang: "zh",
  image-path: "/assets/img/meizi.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
