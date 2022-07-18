class Icon:
    def __init__(self, id, link):
        self.setId(id)
        self.setLink(link)
        return
    
    @property
    def id(self):
        return self._id

    @id.setter
    def setId(self, value):
        self._id = value
    
    @property
    def link(self):
        return self._link
    
    @link.setter
    def setLink(self, value):
        self._link = value