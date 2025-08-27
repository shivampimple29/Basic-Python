#Q5:Write a program to show use of a filter() in python.
def is_even(num):
    return(num%2==0)
#main function:
numlist=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(is_even,numlist))
print(f"Orginal list         :{numlist}")
print(f"Filtered EVEN numbers:{even_numbers}")