#import "../index.typ": template, tufted
#show: template.with(
  title: "RISC-V内核开发学习踩过的坑与建议",
  description: "零基础三周的RISC-V系统内核开发学习总结",
  date: datetime(year: 2025, month: 5, day: 21),
  lang: "zh",
  image-path: "/assets/img/bg-music.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
