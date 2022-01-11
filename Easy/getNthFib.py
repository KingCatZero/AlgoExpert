def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	
    fib0 = 0
	fib1 = 1
	fib2 = 1
	n -= 3
	
	while n > 0:
		fib0 = fib1
		fib1 = fib2
		fib2 = fib0 + fib1
		n -= 1
		
	return fib2
