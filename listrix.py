# Pray for me.



# Sums all values in a list which evaluate to True TODO: put word stuff in (sub?)class of their own
def bool_eater(bool_list):
    ret_int = 0
    for bl in bool_list:
        if bl:
            ret_int += 1
    return ret_int

# takes in a character, and expands it into a bool list
def letter_eater(letter: str, size: int = 26, offset: int = 96):
    retlist = [False] * size
    retlist[ord(letter) - offset - 1] = True
    return retlist

# word in, bool listrix2 out!
def word_eater(word: str):
    char_list = list(word)
    retlist = list()
    for char in char_list:
        retlist.append(letter_eater(char))
    return retlist

# returns a string containing numbers representing the slots a particular letter occupies
# Look, it's better than n^n nested lists
def letter_width_eater(wid_list):
    retstring = ''
    for i in range(len(wid_list)):
        if wid_list[i] == True:
            retstring = retstring + str(i) + '-'
    if len(retstring) > 0:
        retstring = str(retstring[:-1])
    return retstring

# uhhhhhhhh 
# I literally just wrote this and idk what it does
# Well, it doesn't throw errors, so I guess it ships
def word_slot_eater(word_index, listrix):
    retlist = list()
    for letter_index in range(listrix.depth):
        retlist.append(letter_width_eater(listrix.axial_wid(word_index, letter_index))) # oh mhyy
    return retlist

# this is probably the one you're looking for. --Wyatt
def slotrix_eater(listrix):
    reslotrix = list()
    for i in range(len(listrix.len_listr)):
        reslotrix.append(word_slot_eater(i, listrix))
    return reslotrix

# word list in, listrix root (listr) out! 
def list_eater(word_list):
    listr = list()
    for word in word_list:
        listr.append(word_eater(word))
    return listr


class Listrix3:

    #class string_count:
    #    def __init__(self, string: str, count: int):
    #        self.string = string
    #        self.count = count
    #
    #    def plus_plus(self):
    #        self.count += 1
    
    # init => explode => set_listr => build_hstrx

    len_listr = list()
    len_listr_backup = list()
    len_slotrix = list()
    len_hotrix = list()
    # Histogram list matrix => histrix => hstrx
    hstrx_len = list()
    hstrx_wid = list()
    hstrx_dep = list()
    removed_words = 0
    removed_words_backup = 0
    removed_word_list = list()
    removed_word_list_backup = list()

    def __init__(self):
        self.len_listr
        self.len_listr_backup
        self.len_slotrix
        self.len_hotrix
        self.hstrx_len
        self.hstrx_wid
        self.hstrx_dep
        self.has_inflated = False
        self.length = 0
        self.width = 0
        self.depth = 0
        self.removed_word_list = []
        self.removed_word_list_backup = []
        self.removed_words = 0
        self.removed_words_backup = 0

    def explode(self, length: int, width: int, depth: int = 26):
        self.len_listr = []
        self.length = length
        self.width = width
        self.depth = depth
        for i in range(length):
            self.len_listr.append(list())
            for j in range(width):
                self.len_listr[i].append([False] * depth)

        self.len_listr_backup = list(self.len_listr)

    def set_listr(self, listr_in):
        self.len_listr = listr_in
        self.len_listr_backup = list(listr_in)

    def axial_len(self, width: int, depth: int):
        retrix = list()
        for listrix in self.len_listr:
                retrix.append(listrix[width][depth])
        return retrix

    def axial_wid(self, length: int, depth: int):
        retrix = list()
        for lisrix in self.len_listr[length]:
            retrix.append(lisrix[depth])
        return retrix

    def axial_dep(self, length: int, width: int):
        return self.len_listr[length][width]

    def build_hstrx_len(self):
        ristrix = list()
        for i in range(self.width):
            ristrix.append(list())
            for j in range(self.depth):
                ristrix[i].append(bool_eater(self.axial_len(i, j)))
        self.hstrx_len = ristrix
    
    def build_hstrx_wid(self):
        ristrix = list()
        for i in range(len(self.len_listr)):
            ristrix.append(list())
            for j in range(self.depth):
                ristrix[i].append(bool_eater(self.axial_wid(i, j)))
        self.hstrx_wid = ristrix

    def build_hotrix(self):
        hetrix = list()     
        for letter_index in range(self.depth):
            hetrix.append([list(), list()])
            for i in range(len(self.len_slotrix)):
                temp = self.len_slotrix[i][letter_index]
                if temp == '':
                    pass
                elif temp not in hetrix[letter_index][0]:
                    hetrix[letter_index][0].append(temp)
                    hetrix[letter_index][1].append(1)
                else: 
                    # May god have mercy on us all.
                    hetrix[letter_index][1][hetrix[letter_index][0].index(temp)] = hetrix[letter_index][1][hetrix[letter_index][0].index(temp)] + 1
        self.len_hotrix = hetrix
         
    def prune_hotrix(self, nnr_selection, letter_index): # matches = set(checklist).intersection(set(words))
        for i in range(len(self.len_slotrix)):
            if not (nnr_selection[0] == self.len_slotrix[i][letter_index]):  
                if i not in self.removed_word_list:
                    self.removed_words += 1
                    self.removed_words_backup += 1
                    self.removed_word_list.append(i)
                    self.removed_word_list_backup.append(i)
                    
                for slot in self.len_listr[i]:
                    for k in range(len(slot)):
                        slot[k] = False

                for slot in self.len_listr_backup[i]:
                    for k in range(len(slot)):
                        slot[k] = False
                
    def prune_letters(self, letter_index):
        for i in range(len(self.hstrx_wid)):
            if self.hstrx_wid[i][letter_index] > 0:
                if i not in self.removed_word_list:
                    self.removed_words += 1
                    self.removed_word_list.append(i)
            
                for slot in self.len_listr[i]:
                    for k in range(len(slot)):
                        slot[k] = False
            
    def rebuild_all(self):
        self.build_hstrx_len()
        self.build_hstrx_wid()
            
        self.len_slotrix = slotrix_eater(self)
        self.build_hotrix()
        
            
    # if there's a weird issue, check width thing here EDIT: called it.
    #def build_slotrix(self):
    #    #for i in range(len(self.len_listr)):
    #        #self.len_slotrix.append()
    #        #for j in range(self.width):
    #            self.len_slotrix[i].append(self.string_count('',0))

    def rel_chance(self, histrix_in):
        histrix_out = list()
        i = 0
        for hist in histrix_in:
            histrix_out.append([])
            l_sum = 0
            for count in hist:
                l_sum += count
            for count in hist:
                histrix_out[i].append(float(count) / l_sum)
            i += 1
        return histrix_out

    def letter_chance(self, letter_index):
        count = 0
        for word in self.hstrx_wid:
            if word[letter_index] > 0:
                count += 1
        return float(count) / float(len(self.len_listr) - self.removed_words)
