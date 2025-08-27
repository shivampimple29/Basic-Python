def SA(numbers):
    Sum=sum(numbers)
    avg=Sum/5
    return(Sum,avg)
#main Function:    
numlist=[1,2,3,4,5]
Sum,avg=SA(numlist)
print(f"Sum is:{Sum} and average is:{avg}")