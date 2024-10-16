def full_pyramid(n):
	for i in range(1, n + 1):	
		for j in range(n - i):
			print(" ", end="")
		for k in range(1, 2*i):
			print("*", end="")
		print()
def reverce_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i, n + 1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
            
    print()

print(full_pyramid(5))
print(reverce_pyramid(5))
