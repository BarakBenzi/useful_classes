class IfExistsDict(dict):
    def __init__(self, not_exists_type='IfExistsDict'):
        self._type = not_exists_type

    def __getitem__(self, item, **kwargs):
        if item in self.keys():
            return super().__getitem__(item)
        else:
            return IF_EXISTS_TYPES[self._type](**kwargs)


class IfNotBlacklistDict(IfExistsDict):
    def __init__(self, blacklist=[None], not_exists_type='IfNotBlacklistDict'):
        super().__init__(not_exists_type)
        self.blacklist = blacklist if isinstance(blacklist, list) else [blacklist]

    def __getitem__(self, item, **kwargs):
        if super().__getitem__(item, blacklist=self.blacklist) not in self.blacklist:
            return super().__getitem__(item, blacklist=self.blacklist)
        else:
            return IfNotBlacklistDict(self.blacklist)


class SafeExtractDict(dict):
    def __init__(self, empty_value=None):
        super().__init__()
        self.empty_value = empty_value

    def __getitem__(self, item):
        if item in self.keys():
            return super().__getitem__(item)
        else:
            return self.empty_value


IF_EXISTS_TYPES = {
    'IfExistsDict': IfExistsDict,
    'IfNotBlacklistDict': IfNotBlacklistDict
}

if __name__ == '__main__':
    bdict = IfNotBlacklistDict()
    bdict['a'] = None
    bdict['a']['b']['c']
    bdict[1][2][3]
    print("Need to replace this with a proper test :)")
