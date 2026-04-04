#import "../index.typ": template, tufted
#show: template.with(
  title: "高效 简洁",
  description: "高效与简洁能否划等号？",
  date: datetime(year: 2019, month: 11, day: 27),
  lang: "zh",
  image-path: "/assets/img/timg.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
