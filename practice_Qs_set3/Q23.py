#Q23:Use filter() to filter out even numbers from a given list. 

list1=[1,2,3,4,5,6,7,8,9,10]
even_nums=list(filter(lambda a:a%2==0,list1))
print(f"Original list    :{list1}")
print(f"Even numbers list:{even_nums}")
print("------------------------------------------------------") 