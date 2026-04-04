#import "../index.typ": template, tufted
#show: template.with(
  title: "Manjaro变Arch！",
  description: "Arch大法好！",
  date: datetime(year: 2020, month: 1, day: 31),
  lang: "zh",
  image-path: "/assets/img/postam.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
