import datetime

class Post:
    def __init__(self, source, title, link, date, content, product):
        self.setSource(source)
        self.setTitle(title)
        self.setLink(link)
        self.setDate(date)
        self.setContent(content)
        return
    
    @property
    def source(self):
        return self._source
    
    @source.setter
    def setSource(self, value):
        self._source = value
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def setTitle(self, value):
        self._title = value
    
    @property
    def link(self):
        return self._link
    
    @link.setter
    def setLink(self, value):
        self._link = value
    
    @property
    def date(self):
        return self._date.date.strftime("%Y/%m/%d")
    
    @date.setter
    def setDate(self, value):
        date = datetime.strptime(value, '%Y/%d/%m')
        self._date = date
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def setContent(self, value):
        self._content = value

    @property
    def product(self):
        return self._product
    
    @product.setter
    def setProduct(self, value):
        self._product = value
