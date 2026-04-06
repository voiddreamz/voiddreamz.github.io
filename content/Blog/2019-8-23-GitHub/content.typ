= 关于GitHub
<关于github>
GitHub是目前最大的开源项目代码分享平台。在其中，你可以找到许多不怎么出名，但十分实用的软件，也可以分享自己的开源项目，受众多程序员的喜爱。GitHub为每位用户提供了一部分免费的云储存空间。本文将与大家分享#strong[借助GitHub的云储存空间免费创建个人博客或个人网站]。#strong[#emph[但由于平台的原因，网站只能为静态网站，想使用动态网站只能自己购买服务器]]（关于静态网站与动态博客的区别，请阅读#link("https://www.cnblogs.com/bluesungz/p/5955170.html")[这篇文章].

== 关于GitHub项目的管理，极力推荐使用GitHub-desktop
<关于github项目的管理极力推荐使用github-desktop>
\*\*\*外国服务器慢。推荐外网，或百度云链接：链接:
https:/\/pan.baidu.com/s/1VOujKxAP\_Z7C1y0rrQYryg 提取码: gith

#v(0.5em)
#line(length: 100%)
#v(0.5em)

= GitHub的注册
<github的注册>
关于其注册的步骤笔者认为不需要过多赘述，其注册步骤与大多数网站注册步骤几乎无异，甚至无需用任何翻译就可以轻松注册一个账号，下图简单为大家翻译了一下，尤其注意的是：此处的用户名是唯一且不可更改的，设置前请思虑一番，接下来会多次用到。

#link("https://raw.githubusercontent.com/codesjobs/codesjobs.github.io/master/_posts/image/githubandblog/signup.png")[singup1]

此处选择免费套餐即可，付费的功能大多数用不上，为专业用户设定的

#link("https://raw.githubusercontent.com/codesjobs/codesjobs.github.io/master/_posts/image/githubandblog/sing.PNG")[singup1]

完成后进入自己的邮箱选择最新的由github发出的邮件，点击verify email
address，登陆后即可完成注册

== Fork
<fork>
Fork是github中一种简单供大家学习他人代码的功能，进入他人的项目主页中后点击Fork即可将他人的项目文件复制到你的项目库中。
此处推荐大家Fork此博客的的文件，本人认为此博客的主题NeXT十分简洁，是个不错的主题，推荐大家使用。但是本博客经过了部分修改，此处提供官方源链接，Fork后也是不错的。#link("https://github.com/simpleyyt/jekyll-theme-next")[NeXT]。其他的主题也可以在网络上寻找，但不可直接使用官方文档，会无法打开，只能用Fork过的用户的文件（此主题是个例外，官方文档可直接使用）

- 此处附上另外一位酷安用户的主题：#link("https://github.com/Alexander-Huang/Alexander-Huang.github.io")[Alexander-huang]此主题适合不喜欢简洁，追求个性的人使用。
- 更多的可以在coolapk.com的个人博客话题中寻找

#v(0.5em)
#line(length: 100%)
#v(0.5em)

接下来需要修改一下项目名为
`yourusername.github.io`，点击rename，稍后访问即可

#link("https://i.loli.net/2019/09/08/Gydnp3b1cYgQsLq.png")[捕获.PNG]

= 博客的个性化管理与博文的发布
<博客的个性化管理与博文的发布>
关于个性化管理，可直接阅读此主题的#link("http://theme-next.simpleyyt.com/")[官方文档]来管理，博文的发布在`/_post`中加入即可，格式为`YYYY-MM-DD-名称.md`此处的名称不是文章的标题。文章使用Markdown格式。可以在#link("https://www.runoob.com/markdown/md-tutorial.html")[菜鸟教程Markdown]中学习。文章开头必须按照此格式输入
'--- published: 【false（不显示）或true（显示）】 title: 标题 category:
分类 tags: -标签a -标签b layout: post ---'

#v(0.5em)
#line(length: 100%)
#v(0.5em)

头像的位置不是官方文档的位置，首先确保其格式为jpg，重命名为portrait.jpg，移动到`/assets`下即可。侧栏的GitHub和school链接的设置在`/_config.yml`中分别搜索GitHub和school，找到有链接的一行修改即可。

#v(0.5em)
#line(length: 100%)
#v(0.5em)

本文到此结束，文章开头的GitHub-desktop极力推荐使用。有了它，可以在本地修改文档后传到云端，可以使用自己喜爱的文件编辑器并简单地管理文档。
