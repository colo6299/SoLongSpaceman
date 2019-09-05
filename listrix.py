

# Pray for me. 


class Listrix3:
    def __init__(self):
        self.len_list
        self.has_inflated = False

    len_list = list()

    def inflate(self, length: int, width: int, depth: int = 26):
        len_list = []
        for i in range(length):
            len_list.append(list())
            for j in range(width):
                len_list[i].append([False] * depth)

l = Listrix3()
l.inflate(4,4,26)

print(l.len_list)