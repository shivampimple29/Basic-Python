#list operations

list1=[34,'Shivam','INFT']
list2=[55,'SFIT','a']
print("2nd element of list is   : ",list1[1])
print("list[0] before assignment:",list1)
list1[0]="B"
print("list[0] after assignment :",list1)
print("Slicing                  :",list1[1:2])
a=list1+list1
print(a)
print("Assigning empty list:")
my_list=list()
print("Empty list:",my_list)
print("squeez")
li=[1,2,2,3,4,4]
li=list(set(li))
print(li)
a="Shivam"
print("Deleting List:",list1.remove("INFT"))
print(list1)
list1.clear()
print(list1)
print("Use of membership operators in list:")
print(55 in list2)
print(34 in  list2)
a="Shivam"
b=list(a)
print(b)
print("Sorting:",b.sort())
print(b)
print("length of list2 is:",len(list2))
list2.append("Shivam")
print(list2)
print("Index of SFIT is:",list2.index("SFIT"))
print("list befor pop:",list2)
list2.pop()
print("List after pop",list2)
list2.extend("IT")
print(list2)
print("--------------------------------------------------------------------------")