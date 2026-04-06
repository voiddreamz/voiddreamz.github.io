#import "../index.typ": template, tufted
#show: template.with(
  title: "Hello World",
  description: "博客正式成立",
  date: datetime(year: 2019, month: 8, day: 18),
  lang: "zh",
  image-path: "/assets/img/tag-bg-o.jpg",
)

#include "content.typ"
