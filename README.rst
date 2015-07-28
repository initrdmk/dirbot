======
先说说爬虫是干什么的
======

我理解的爬虫,就是用来自动发送网络请求,从而获得网络资源的.
举个很简单的例子,当你发现豆瓣上有好多书籍的简介,你想把他们全部都保存下来,这个时候你就需要写一只爬虫,*自动*把书的简介爬下来.
再举个例子,你想研究一下微博上某个人的生活习惯和社交信息,你可以去微博上把和TA相关的所有微博都爬下来,然后再用一些数据分析的工具对
这些微博进行分析,从而得到自己想要的信息.

1. 爬虫只是获取信息,一般来说并不能用来对数据进行分析.
2. 很多网站(比如豆瓣)会对爬虫行为进行检测,防止数据被抓走.(某师兄有次去豆瓣爬东西,然后实验室IP被豆瓣封掉了T_T)所以有些时候,
   写爬虫的人会用代理服务器去运行爬虫,防止IP被网站封掉.
3. 爬虫能做的事情,基本都可以手工的来完成.之所以用爬虫,是因为它是自动的.

======
下面那些英文的小总结
======

这是个Scrapy项目,仅仅用于教育目的.

Ubuntu的话,
先把这个repo clone下来::

    $ git clone https://github.com/initrdmk/dirbot.git

然后安装Scrapy::

    $ sudo pip install scrapy

然后在repo的目录里面::

    $ scrapy list

应该可以看到输出::

    domz

运行的话执行::

    $ scrapy crawl dmoz

输出会有一大堆...

======
稍微介绍下目录结构
======

dirbot/
        spider/
                dmoz.py         最主要的东西,进去看吧
                __init__.py     初始化spider这个子包(subpackage)
        __init__.py             python里面用来初始化一个package/subpackage的文件 `See more here. <https://docs.python.org/2/tutorial/modules.html`
        items.py                dirbot里面定义的Item的地方.实际上定义了scrapy.item这个类的子类,叫做Website.
        pipelines.py            dirbot里面定义的相当于过滤器的东西,用于和谐"不和谐"的字符串
        settings.py             定义了整个scrapy项目的比较关键的配置.
README.rst                      就是你现在看的这个东西0,0
scrapy.cfg                      scrapy的配置文件(我猜的,反正这个文件里面指向了dirbot/settings.py这个文件)
setup.py                        用来安装和管理python包(package)的文件 `See more here. <https://docs.python.org/2/install/index.html>`


======
dirbot
======

This is a Scrapy project to scrape websites from public web directories.

This project is only meant for educational purposes.

Items
=====

The items scraped by this project are websites, and the item is defined in the
class::

    dirbot.items.Website

See the source code for more details.

Spiders
=======

This project contains one spider called ``dmoz`` that you can see by running::

    scrapy list

Spider: dmoz
------------

The ``dmoz`` spider scrapes the Open Directory Project (dmoz.org), and it's
based on the dmoz spider described in the `Scrapy tutorial`_

This spider doesn't crawl the entire dmoz.org site but only a few pages by
default (defined in the ``start_urls`` attribute). These pages are:

* http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
* http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/

So, if you run the spider regularly (with ``scrapy crawl dmoz``) it will scrape
only those two pages.

.. _Scrapy tutorial: http://doc.scrapy.org/en/latest/intro/tutorial.html

Pipelines
=========

This project uses a pipeline to filter out websites containing certain
forbidden words in their description. This pipeline is defined in the class::

    dirbot.pipelines.FilterWordsPipeline
