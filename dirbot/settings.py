# Scrapy settings for dirbot project

# 爬虫模块们的名字
SPIDER_MODULES = ['dirbot.spiders']

# 并不知道这个是什么,我猜是新建爬虫的时候new哪个爬虫
NEWSPIDER_MODULE = 'dirbot.spiders'
# 默认的item类
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

# 定义的pipeline,所有的数据会从这些pipeline中流过,这里定义的filter,其实就是个过滤器.
# 用pipeline也可以用来做一些统计工作,比如统计下一共有多少个item流了过去.
ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1}
