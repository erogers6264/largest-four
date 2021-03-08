#!/usr/bin/env python3

# Function takes in a list of ints and returns a
# list of ints consisting of the largest consecutive
# four elements
def largest_consecutive_four(list_of_ints):
	# Takes a greedy approach trying one solution after
	# another saving the best one so far
	current_largest_sum = 0
	current_largest_i = 0

	# Iterate through elements and their
	# indicies until the fourth to last
	for i, current in enumerate(list_of_ints[:-3]):
		# Calculate sum of current element
		# plus next three elements
		new_sum = current + list_of_ints[i+1] + list_of_ints[i+2] + list_of_ints[i+3]
		# If sum is greater than previous sum,
		# overwrite previous sum
		if current_largest_sum < new_sum:
			current_largest_sum = new_sum
			current_largest_i = i
	# Once loop terminates, return list
	# of greatest four consecutive elements
	return list_of_ints[current_largest_i:current_largest_i+4]

# Declare list of numbers to test
total_customers_per_half_hour = [10, 13, 6, 25, 32, 49, 49, 56, 48, 54, 42, 39, 39, 28, 39, 26, 25, 27, 21, 24, 17, 16, 16, 21, 19, 12, 17, 17, 11, 7, 11, 14, 16, 6, 7]

# Test function call
# (Should return [49, 56, 48, 54])
print(largest_consecutive_four(total_customers_per_half_hour))
