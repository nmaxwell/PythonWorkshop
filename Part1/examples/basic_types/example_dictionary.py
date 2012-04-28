d1 = {'a':1,'b':2}
d2 = {'nested_list' : [1,2,3], 
      'nested_dictionary' : {'a' : 1, 'b' : 2}}
d3 = dict(brain="cancer", liver="failure")

for key in d1.keys():
    print key

for value in d2.values():
    print value

for key,value in d3.items():
    print key,value

d1['new_key'] = "hi, i'm a new key"
print d1

del d1['new_key']
print d1
