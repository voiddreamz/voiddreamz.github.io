#import "../index.typ": template, tufted
#show: template.with(
  title: "百度之外的新天地（下）",
  description: "使用插件快捷访问谷歌",
  date: datetime(year: 2019, month: 11, day: 17),
  lang: "zh",
  image-path: "/assets/img/post-bg-rwd.jpg",
)

#import "@preview/cmarker:0.1.8"
#import "@preview/mitex:0.2.6": *
#let md = read("post.md")
#let scope = (:)
#cmarker.render(md, math: mitex, scope: scope)
