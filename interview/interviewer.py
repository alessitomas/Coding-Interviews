# insert
# remove
# replace 


# -- if the are equal --

# abc -> abc -> 0
# all letters would match and I can retun 0

# -- remove --

# abd
# abbd
# remove b from abbd -> can return 1

# -- insert --

# abbd
# abd 
# add b to abd -> can return 1



# remove only if str B is bigger the A
# insert only if B is smaller than A

# Just insert
# remove -> insert into the smaller

# remove from B is the same of Insert in A

# replace if the have equal sizes

# abcd

# fabcd

def one_edit_away(first: str, second: str) -> bool:
    len_diff = abs(len(first) - len(second))
    if len_diff > 1:
        return False
    
    count_diff = 0
    
    if len_diff == 0:
        for i in range(len(first)):
            if first[i] != second[i]:
                count_diff += 1
        if count_diff > 1: return False
        return True
    
    if len(first) < len(second):
       first, second = second, first
    
    
    if len_diff == 1:
        count_diff = 0
        i, j = 0, 0
        while i < len(first) and j < len(second):
            if first[i] != second[j]:
                count_diff += 1
                i += 1
            else:
                i += 1
                j += 1
    
    if count_diff > 1: return False
    else: return True

            

        




            


print(one_edit_away(" bcd", "abcd"))

# 012345
# 0123

# d = 1


# "cd"
# "bcd"