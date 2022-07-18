class ProductClass:
    def __init__(self, id, name):
        self.setId(id)
        self.setName(name)
        return

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def setId(self, value):
        self._id = value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def setName(self, value):
        self._name = value