#Q4:WAP to double each element of the given list using map().
def Double(x):
    return(x*2)
#main function:
numlist=[1,2,3,4,5]
doubled_numbers=list(map(Double,numlist))
print(f"Orginal list:{numlist}")
print(f"Doubled list:{doubled_numbers}")