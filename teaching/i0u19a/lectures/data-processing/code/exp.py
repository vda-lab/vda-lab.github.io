
def exp(x, n):
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)


def loopExp(x,n):
	tmp = 1
	for i in range(0,n):
		tmp = tmp * x
	return tmp

print exp(3,3)
print loopExp(3,3)

