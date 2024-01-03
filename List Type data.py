'''mo=["mottalib","Shafin","Shahadot",54453,6556.66,5445j ]
print(mo)
print(type(mo))
#data update
mo[0]=545454
print(mo[0])
mo[5]="bijoy"
print(mo[5])'''
#Python List Type Data Add
'''We can add  list type data in 3 ways 
1.append()   it helps add data last endex
2 insert()   id helps add data index number
3 extend()        '''

# 1 append()



#m=[1233,5434,"mottalib","Bijoy","Shafin"]
#m.append("Shorab Hossain")
#print(m)

# 2 insert()

#insert index number start form 1
'''
bi=["mottalib","shafin","jabir","kabir","shamim"]
bi.insert(2,"Google+")
print(bi)
'''
# 3 extend()
'''mo=["mottalib","Shafin","Shahadot",54453,6556.66,5445j ]
mo.extend("Bijoyyyy")
print(mo)
mo.extend("Barishal Polytechnic Institude")
print(mo)'''

'''Python list Type data  Remove options 
1 remove()
2 del()
3 pop()
4 clear()
'''
mo=["mottalib","Shafin","Shahadot",54453,6556.66,5445j ]
mo.remove("mottalib")
print(mo)

#3 pop()
#pop index start form 0

thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

# python list type data  removed by del method

# del method use curfully it start frist then variable name last squire brackers index number

mo=["mottalib","Shafin","Shahadot",54453,6556.66,5445j ]
del mo[0]
print(mo)

#Python List Type data Clear Method

list = ["apple", "banana", "cherry"]
list.clear()
print(list)

#loop creat
'''
ist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

hislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  '''


islist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1