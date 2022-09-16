x = [1 , 2, 3]
print(x)
# [1 , 2, 3]

x = ['hi' , 1 , [1,2] ]
print(x)
# ['hi' , 1 , [1,2] ]

my_list = ['a' , 'b' , 'c']
my_list.append('d')
print(my_list)
# ['a' , 'b' , 'c' , 'd']

print(my_list[0])
# a

print(my_list[1])
# b

print(my_list[1:])
# ['b' , 'c' , 'd']

print(my_list[:1])
# ['a']

my_list[0] = 'NEW'
print(my_list)
# ['NEW' , 'b' , 'c' , 'd']

nest = [1,2,3,[4,5,['target']]]
print(nest[3])
# [4,5,['target']]

print(nest[3][2])
# ['target']

print(nest[3][2][0])
# target

