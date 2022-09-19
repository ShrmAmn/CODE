st = 'hello my name is Sam'
st.lower()
# 'hello my name is sam'

st.upper()
# 'HELLO MY NAME IS SAM'

st.split()
# ['hello', 'my', 'name', 'is', 'Sam']

tweet = 'Go Sports! #Sports'
tweet.split('#')
# ['Go Sports! ', 'Sports']

tweet.split('#')[1]
# 'Sports'

d = {'key1': 'item1', 'key2': 'item2'}
# {'key1': 'item1', 'key2': 'item2'}

d.keys()
# dict_keys(['key2', 'key1'])

d.items()
# dict_items([('key2', 'item2'), ('key1', 'item1')])

lst = [1,2,3]
lst.pop()
# 3

print(lst)
# [1, 2]

'x' in [1,2,3]
# False

'x' in ['x','y','z']
# True
