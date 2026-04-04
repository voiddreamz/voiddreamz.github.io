#import "../index.typ": template, tufted
#show: template.with(
  title: "为什么我上的二本大学是二本大学",
  description: "我所看到的二本大学是什么样子的",
  date: datetime(year: 2026, month: 3, day: 6),
  lang: "zh",
  image-path: "/assets/img/bg-music.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
