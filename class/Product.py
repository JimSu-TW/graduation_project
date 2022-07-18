import datetime

class Product:
    def __init__(self, id, icon_id, brand_id, product_class_id, name, release_date, specification):
        self.setId(id)
        self.setIconId(icon_id)
        self.setBrandId(brand_id)
        self.setProductClassId(product_class_id)
        self.setName(name)
        self.setReleaseDate(release_date)
        self.setSpecification(specification)
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
    def icon_id(self):
        return self._icon_id
    
    @icon_id.setter
    def setIconId(self, value):
        self._icon_id = value
    
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def setBrandId(self, value):
        self._brand_id = value
    
    @property
    def product_class_id(self):
        return self._product_class_id
    
    @product_class_id.setter
    def setProductClassId(self, value):
        self._product_class_id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def setName(self, value):
        self._name = value
    
    @property
    def release_date(self):
        return self._release_date.date.strftime("%Y/%m/%d")
    
    @release_date.setter
    def setReleaseDate(self, value):
        date = datetime.strptime(value, '%Y/%d/%m')
        self._release_date = date

    @property
    def specification(self):
        return self._specification
    
    @specification.setter
    def setSpecification(self, value):
        self._specification = value
    
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
