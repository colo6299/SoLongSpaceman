

# Pray for me.


def bool_eater(bool_list):
    ret_int = 0
    for bl in bool_list:
        if bl:
            ret_int += 1
    return ret_int


class Listrix3:
    
    len_list = list()
    # Histogram list matrix => histrix => hstrx
    hstrx_len = list()
    hstrx_wid = list()
    hstrx_dep = list()

    def __init__(self):
        self.len_list
        self.hstrx_len
        self.hstrx_wid
        self.hstrx_dep
        self.has_inflated = False
        self.length = 0
        self.width = 0
        self.depth = 0

    def explode(self, length: int, width: int, depth: int = 26):
        self.len_list = []
        self.length = length
        self.width = width
        self.depth = depth
        for i in range(length):
            self.len_list.append(list())
            for j in range(width):
                self.len_list[i].append([False] * depth)

    def axial_len(self, width: int, depth: int):
        retrix = list()
        for listrix in self.len_list:
                retrix.append(listrix[width][depth])
        return retrix

    def axial_wid(self, length: int, depth: int):
        retrix = list()
        for lisrix in self.len_list[length]:
            retrix.append(lisrix[depth])
        return retrix

    def axial_dep(self, length: int, width: int):
        return self.len_list[length][width]
    
    
    def build_hstrx_len(self):
        ristrix = list()
        for i in range(self.width):
            ristrix.append(list())
            for j in range(self.depth):
                ristrix[i].append(bool_eater(self.axial_len(i, j)))
        self.hstrx_len = ristrix
    
    def build_hstrx_wid(self):
        ristrix = list()
        for i in range(self.length):
            ristrix.append(list())
            for j in range(self.depth):
                ristrix[i].append(bool_eater(self.axial_wid(i, j)))
        self.hstrx_wid = ristrix

l = Listrix3()
l.explode(100, 4, 26)
l.build_hstrx_wid()
print(l.hstrx_wid[99][25])