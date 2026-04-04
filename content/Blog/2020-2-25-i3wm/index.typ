#import "../index.typ": template, tufted
#show: template.with(
  title: "i3wm桌面的配置",
  description: "一个优秀的桌面平铺管理器",
  date: datetime(year: 2020, month: 2, day: 25),
  lang: "zh",
  image-path: "/assets/img/i3-bg.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
