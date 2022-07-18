class Soure:
    def __init__(self, id, icon_id, name):
        self.setId(id)
        self.setIconId(icon_id)
        self.setName(name)
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
    def name(self):
        return self._name
    
    @name.setter
    def setName(self, value):
        self._name = value