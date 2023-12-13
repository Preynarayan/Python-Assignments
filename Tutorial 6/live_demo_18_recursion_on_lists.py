# Q1: What arguments would you consider simple?
# A1: The empty list [] is always simplest

# Q2: How could you make an argument simpler?
# A2: A list can be shorted by one element using a slice - e.g., my_list[1:]
   
# Q3: How could the result with a simple argument be used for a more complex one?
# A3: If you had the sum of all but the first element, just add the first one...
#     If you had the count of all the zeros excluding the first, just consider the head...
#     If you had the largest of all elements but the first, just consider the first as well...

def recursive_sum(arg: list) -> int:

	# first we branch if we are dealing with a base case...
	if arg == []:
		return 0
	
	# ...but if not we...
	else:
		# 1. simplify the argument (see Q1/A1 above)
		# 2. make the recursive call (see Q2/A2 above)
		# 3. do the additional work incurred by simplifying (see Q3/A3 above)
		return arg[0] + recursive_sum(arg[1:])


def recursive_count(arg: list) -> int:

	# first we branch if we are dealing with a base case...
	if arg == []:
		return 0
	
	# ...but if not we...
	else:
		# 1. simplify the argument (see Q1/A1 above)
		# 2. make the recursive call (see Q2/A2 above)
		number_of_zeros = recursive_count(arg[1:])

		# 3. do the additional work incurred by simplifying (see Q3/A3 above)
		if arg[0] == 0:
			number_of_zeros += 1

		return number_of_zeros
		

def recursive_max(arg: list) -> int:

	# first we branch if we are dealing with a base case...
	# since the maximum of an empty list is undefined, we just return -1
	if arg == []:
		return -1
	
	# ...but if not we...
	else:
		# 1. simplify the argument (see Q1/A1 above)
		# 2. make the recursive call (see Q2/A2 above)
		max_so_far = recursive_max(arg[1:])

		# 3. do the additional work incurred by simplifying (see Q3/A3 above)
		if arg[0] > max_so_far:
			max_so_far = arg[0]

		return max_so_far


# this uses a stucture similar to the input validation loop to allow the user
# to submit all of the elements to the list of integers, one at a time
def main():

	input_list = []
	
	while True:
	
		user_input = input("Enter an integer or press 'Q' to quit >>").upper()
		
		if user_input == "Q":
			break
		else:
			input_list.append(int(user_input))
	
	print(f"The list provided is was {input_list}.")
	print()
	print(f"The sum of this list is {recursive_sum(input_list)}.")
	print(f"The zero count of this list is {recursive_count(input_list)}.")
	print(f"The maximum of this list is {recursive_max(input_list)}.")
	
	
main()
