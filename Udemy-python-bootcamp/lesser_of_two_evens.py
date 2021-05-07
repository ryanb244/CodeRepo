#def lesser_of_two_evens(a,b):
#	sum = a+b
#	if sum % 2 == 0:
#		if a < b:
#			return a
#		else:
#			return b
#	elif a % 2 == 0:
#		return b
#	else:
#		return a
#
#print(lesser_of_two_evens(2,5))


def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		if a < b:
			result = a
		else:
			result = b
	else:
		if a > b:
			result = a
		else:
			result = b

	return result

print(lesser_of_two_evens(2,4))

