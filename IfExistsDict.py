class IfExistsDict(dict):
    def __getitem__(self, item):
        if item in self.keys():
            return super().__getitem__(item)
        else:
            return IfExistsDict()
