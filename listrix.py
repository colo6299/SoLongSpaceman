

# Pray for me. 


class Listrix3:
    def __init__(self):
        self.len_list
        self.has_inflated = False

    len_list = list()
    
    # Histogram list matrix => histrix => hstrx
    hstrx_len = list()
    hstrx_wid = list()
    hstrx_dep = list()

    def explode(self, length: int, width: int, depth: int = 26):
        self.len_list = []
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


l = Listrix3()
l.explode(100,4,26)