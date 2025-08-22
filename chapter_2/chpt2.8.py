#Display different types of operators used in python.
a=12
b=10
print("\nArithmetic operations:\n")
print("Addition is       :",a+b)
print("Substraction is   :",a-b)
print("Multiplication is :",a*b)
print("Division is       :",a/b)
print("Remainder is      :",a%b)
print("cube of a is      :",a**3)
print("floor division is :",a//b)
print("--------------------------------------------------------------------------")
print("Assignment operations:\n")
b+=5
print("Addition is         :",b)
a-=4
print("Substraction is     :",a)
a*=4
print("Multiplication is   :",a)
b/=5
print("Division is         :",b)
b%=9
print("Remainder is        :",b)
a**=2
print("Square of a is      :",a)
b//=2
print("floor division is   :",b)
print("--------------------------------------------------------------------------")
print("comparison operations:\n")
a=4
b=2
print("a is greater than b:",a>b)
print("b is greater than a:",b>a)
print("a is equal to b    :",a==b)
print("a is not equal to b:",a!=b)
print("--------------------------------------------------------------------------")
print("Logical Operations:\n")
c=8
d=5
print((c<10)and(d>0))
print((c<10)or(d>0))
print(not(c<10 and d>0))
print("--------------------------------------------------------------------------")
print("Bitwise Operations:\n")
a=10
b=2
c=0
print("A=",a,"B=",b,"C",c)
print("a&c ",a&c)
print("a|b",a|b)
print("a^b",a^b)
print("~c",~c)
print("a<<2",a<<2)
print("a>>2",a>>2)
print("--------------------------------------------------------------------------")
print("Membership Operations:\n")
a="hello this is a wonderful place"
print("hello"in a)
print("."not in a)
print("--------------------------------------------------------------------------")
print("Identity Operations:\n")
a="hello this is a wonderful place"
b="hello that is a wonderful place"
print(b is a)
print(b is not a)
print("--------------------------------------------------------------------------")
