from scrapy.item import Item, Field
# 从scrapy.item这个包里面引入Item和Field

# 声明一个class,名字是Website,父类是Item,这个Item就是前面import进来的那个Item.
class Website(Item):

    name = Field()
    description = Field()
    url = Field()
    # 这三行是类里面的三个成员变量的初始化
