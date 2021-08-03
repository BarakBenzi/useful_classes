class IfExistsDict(dict):
    def __getitem__(self, item):
        if item in self.keys():
            return super().__getitem__(item)
        else:
            return IfExistsDict()


class IfNotBlacklistDict(IfExistsDict):
    def __init__(self, blacklist=[None]):
        super().__init__(self)
        self.blacklist = blacklist if isinstance(blacklist, list) else [blacklist]

    def __getitem__(self, item):
        if item in self.keys() and super().__getitem__(item) not in self.blacklist:
            return super().__getitem__(item)
        else:
            return IfNotBlacklistDict(self.blacklist)
