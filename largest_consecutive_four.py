#!/usr/bin/env python3

# Function takes in a list of ints and returns a
# list of ints consisting of the largest consecutive
# four elements of the inputed list
def largest_consecutive_four(list_of_ints):
	# This algorithm takes a greedy approach
	# trying one solution after another saving
	# the best one it has seen so far
	current_largest_sum = 0
	current_largest_i = 0

	# Iterate through the list of ints and their
	# corresponding indexes until the fourth to the
	# last element
	for i, total in enumerate(list_of_ints[:-3]):
		# Calculate the sum of the current element
		# plus the next three elements
		new_sum = total + list_of_ints[i+1] + list_of_ints[i+2]
		# If this sum is greater than the one we
		# already have, this is the new best answer
		if current_largest_sum < new_sum:
			# Set our new values
			current_largest_sum = new_sum
			current_largest_i = i
	# Once the iteration through the list terminates,
	# return a slice of the input using the index where
	# the greatest consecutive four was found
	return list_of_ints[current_largest_i:current_largest_i+4]

# Declare list of numbers to test
total_customers_per_half_hour = [10, 13, 6, 25, 32, 49, 49, 56, 48, 54, 42, 39, 39, 28, 39, 26, 25, 27, 21, 24, 17, 16, 16, 21, 19, 12, 17, 17, 11, 7, 11, 14, 16, 6, 7]

# Test to see if our function works
# (Should return [3, 4, 5, 6])
print(largest_consecutive_four(total_customers_per_half_hour))

