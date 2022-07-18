import datetime

class LabelDetail:
    def __init__(self, id, product_id, label_id, content):
        self.setId(id)
        self.setProductId(product_id)
        self.setLabelId(label_id)
        self.setContent(content)
        self.setCreateDate()
        self.setModifiedDate()
        return 
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def setId(self, value):
        self._id = value
    
    @property
    def product_id(self):
        return self._product_id
    
    @product_id.setter
    def setProductId(self, value):
        self._product_id = value

    @property
    def label_id(self):
        return self._label_id
    
    @label_id.setter
    def setLabelId(self, value):
        self._label_id = value
    
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