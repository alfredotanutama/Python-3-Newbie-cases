def is_prime(num):
    counter=0
    for i in range(1,10):
        if num%i==0:
          # print(counter)#debug
           counter=counter+1
    if counter<=2:
       return True
    else:
       return False

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
