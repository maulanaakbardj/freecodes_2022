def Fibonacci(n):


	if n < 0:
		print("Incorrect input")


	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

fib = int(input("Enter the number : "))
print(Fibonacci(fib))