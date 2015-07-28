from scrapy.spiders import Spider
from scrapy.selector import Selector
# 从scrapy里面引入的东西

from dirbot.items import Website
# 从自己package里面引入的东西,比如那个叫做Website的Item子类.

# 这是一个spider的子类
class DmozSpider(Spider):
    # 名字叫做dmoz
    name = "dmoz"
    # 这个爬虫允许访问"dmoz.org",这是个数组,["dmoz.org", "baidu.com"]表示可以允许这两个域名
    allowed_domains = ["dmoz.org"]
    # 开始的url地址,简单理解url就是一个网络地址,用来定位某个网络资源(其实就是个地址...比如你告诉我你家地址,我就能去武汉找到你,然后带你出去吃顿饭看个电影啥的)
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]
    
    # 这里先讲一下scrapy流程,大概就这么几步:
    # 1. 对于start_urls中的每个url,发送一个网络请求(request)过去,然后服务器就会返回给scrapy一个回应,回应的内容叫做response.
    # 2. scrapy就调用你爬虫里写的parse函数,并把服务器返回的response当做参数传进去.
    # 3. 在你自己写的parse里面,你对response进行了处理,然后返回一个数组(数组里面可以是item等数据,或者也可以放新的request)
    # 4. 如果放的是新的request,那么返回之后这些request请求会被发送,从而从服务器得到更多的response,调用更多次prase函数.
    # 5. 如果放的是item,那么item会被发送给pipelines.这些pipelines就像一个个小过滤网,每个pipeline都可以对数据进行进一步的修改或者统计,再或者将其保存到数据库里面.

    # 这个parse函数就是对服务器返回的response进行处理
    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        # 上面这一段是对函数的一段说明,可以用来自动生成文档.

        # 下面是对response进行处理
        # Selector是scrapy提供的一个格式处理的类,主要是用来解析HTML的那种XML格式.(吖?这个不懂哇?请发短信到 185 1663 0512 寻求帮助嘿嘿OvO)

        # 使用response创建一个selector,之后你就可以向这个selector询问数据
        sel = Selector(response)
        # 下面这句是问selector,请把所有class为directory-url的ul下面的li都找出来,放一个数组里返回.(数组里保存的仍然是个selector对象,也就是说还可以对这个对象继续询问信息)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        # 创建一个空的数组，用来存放结果．
        items = []

        # 对于刚刚selector返回的每个site
        for site in sites:
            # 创建一个新的Website对象
            item = Website()
            # 问这个site(这个site是个selector对象), 请返回a标签里面的text,

            # ((这里的a标签是相对于site的,而site是某个class为directory-url的ul标签下面的li标签,
            # 所以a标签实际上是某个class为directory-url的ul标签下面的li标签下面的a标签.))

            # 返回值仍然是个selector,对这个selector调用extract,可以把最终的text取出来.
            # obj['key']的用法相当于一个map/hashmap,可以存放键值对.
            item['name'] = site.xpath('a/text()').extract()

            # 这个是获取a标签里面的href属性的内容
            item['url'] = site.xpath('a/@href').extract()
            # 这个是获取site里面的所有text,然后用正则表达式选出"-"开头,后面跟了一个空白字符(space,tab之类的),
            # 在之后跟了0~n个非"\n"的字符,再之后是"\\r"这两个字符的字符串.
            # 这里我也不是很懂\\r这个东西为啥要写在这里,而且感觉有了\\r应该选不到东西才对....
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')

            # 最后把item放到items那个数组里面
            items.append(item)

        return items

# 这边是一些学习资料.
# html/xpath相关的东西戳这里:
#  1) http://www.w3school.com.cn/xpath/
#  2) http://www.w3school.com.cn/html/index.asp
# 正则表达式看这里:(有很多在线的测试器可以用)
# http://deerchao.net/tutorials/regex/regex.htm


# 上面这些看看基本的就好,没太大必要非常非常深入的记住每个细节,忘记了再查嘛
# T_T 其实我发现我也好多东西都不会...
# 而且我惊奇的发现我用中文注释之后python2就跑不起来了...
