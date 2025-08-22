#Q. Can we have a set with 18 (int) and "18(str) as a values in it?
s=set()
s1=int(input("Enter a value :"))
s.add(s1)
s2=input("Enter a value :")
s.add(s2)
print(s)
print("-----------------------------------------------------------------------------------------------------------------------------------------")
#Q :What will be the length of following sets?
ss=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
print("-----------------------------------------------------------------------------------------------------------------------------------------")
#Q :what is the type of Set={} ?
Set={}
print(type(Set))