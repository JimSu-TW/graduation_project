class Label:
    def __init__(self, id, product_class_id, icon_id, name):
        self.setId(id)
        self.setProductClassId(product_class_id)
        self.setIconId(icon_id)
        self.setName(name)
        return

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def setId(self, value):
        self._id = value
    
    @property
    def product_class_id(self):
        return self._product_class_id
    
    @product_class_id.setter
    def setProductClassId(self, value):
        self._product_class_id = value

    @property
    def icon_id(self):
        return self._icon_id
    
    @icon_id.setter
    def setIconId(self, value):
        self._icon_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def setName(self, value):
        self._name = value