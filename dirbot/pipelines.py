from scrapy.exceptions import DropItem
# 从scrapy.exceptions里面引入DropItem(看起来应该是个异常,用来抛出去的)

# 声明了一个类,集成自object
class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']
    # 这是定义了一个数组,这个数组里面有两个字符串,'politics'和'religion'.

    # 定义了一个成员函数,self就相当于c++里面的this,但是在python里面是必须显式写出来的.
    # item和spider是两个参数,参数类型暂时看不出来...
    def process_item(self, item, spider):

        # 访问类成员变量的时候必须使用self.member_var_name, 相当于c++里面的this->member_var_name.
        # 这个for用来遍历words_to_filer里面的所有元素,相当于
        #   int i;
        #   for (i=0; i<this->words_to_filter.length(); ++i) {
        #       string word = this->words_to_filter[i];
        #       if item.get('description').toLowerCase().contains(word) {
        #           throw new DropItem("Contains forbidden word: " + word);
        #       }
        #   }
        #   if (i == this->words_to_filter.length()) {
        #       return item;
        #   }
        #
        #  for ... else 是个简写,当for遍历完所有的元素,但是没有被break打断时,else后面的语句会被执行.

        # 函数的意思大概就是,给我一个item,我看看item的description里面有没有我自己定义的不和谐字符串,如果有的话,
        # 抛出异常,如果没有的话就返回这个item.

        # See more here: https://docs.python.org/2/tutorial/controlflow.html
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item
