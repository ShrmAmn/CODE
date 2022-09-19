seq = [1,2,3,4,5]

def times2(var):
    return var*2
  
map(times2,seq)
# <map at 0x105316748>

list(map(times2,seq))
# [2, 4, 6, 8, 10]

list(map(lambda var: var*2,seq))
# [2, 4, 6, 8, 10]

filter(lambda item: item%2 == 0,seq)
# <filter at 0x105316ac8>

list(filter(lambda item: item%2 == 0,seq))
# [2, 4]
