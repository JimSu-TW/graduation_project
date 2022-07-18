import datetime

class Post:
    def __init__(self, id, source_id, product_id, title, link, date, content):
        self.setId(id)
        self.setSourceId(source_id)
        self.setTitle(title)
        self.setLink(link)
        self.setDate(date)
        self.setContent(content)
        self.setProductId(product_id)
        self.setCreateDate()
        self.setModifiedDate()
        return

    @property
    def id(self):
        return self._id
    
    @id.setter
    def setId(self, value):
        self._id = value
    
    @property
    def source_id(self):
        return self._source_id
    
    @source_id.setter
    def setSourceId(self, value):
        self._source_id = value

    @property
    def product_id(self):
        return self._product_id
    
    @product_id.setter
    def setProductId(self, value):
        self._product_id = value
    
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
    def create_date(self):
        return self._create_date.date.strftime("%Y/%m/%d")
    
    @create_date.setter
    def setCreateDate(self):
        self._create_date = datetime.date.today()
    
    @property
    def modified_date(self):
        return self._modified_date.date.strftime("%Y/%m/%d")
    
    @create_date.setter
    def setModifiedDate(self):
        self._modified_date = datetime.date.today()

