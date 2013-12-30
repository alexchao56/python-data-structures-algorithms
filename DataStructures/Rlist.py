class Rlist:

    class EmptyList:
        def __len__(self):
            return 0
    empty = EmptyList()

    def __init__(self, first, rest):
        assert type(rest) is Rlist or rest is Rlist.empty
        self.first = first
        self.rest = rest

    def __getitem__(self, index):
        if index == 0:
            return self.first
        else:
            return self.rest[index-1]

    def __len__(self):
        return 1 + len(self.rest)
