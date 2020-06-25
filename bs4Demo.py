from bs4 import BeautifulSoup
#官网：https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc)
#打印的规范一些
#print(soup.prettify())

#取title文本
print(soup.title.text)
print(type(soup.title))
#看类的属性
print(soup.title.__dir__())
print(dir(soup.title))

#取标签属性
print(soup.a)
print(soup.a.__dir__())
print(soup.a.attrs)
print(soup.a.attrs['class'])
print(soup.a.text)
print(soup.a['href'])

#取标签内的标签
print(soup.p)
print(list(soup.p.children))
print(list(soup.p.children)[0].text)
print(soup.p.b)

#取出所有的标签，如a
print(soup.find_all('a'))
print(type(soup.find_all('a')))
for each in soup.find_all('a'):
    print(each.attrs['href'])

#根据id找节点
print(soup.find(id='link3'))

#找出所有文字内容，不论在何种标签,爬取文章页面有用
print(soup.get_text())



