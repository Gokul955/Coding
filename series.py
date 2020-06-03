def sum(num):
	result=0
	fact=1
	for i in range(1,num+1):
    		fact=fact*i
    		result=result+(i/fact)
	return result
n= int(input("Enter a number"))
print("Sum:",sum(n))

