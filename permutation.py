# CS223P - Python Programming

# Author Name: Kathy Saad
# Project Title: Assignment 6 - Generators and Iterators - Permutations
# Project Status: Working
# External Resources:
#	Class notes
#	https://www.python.org/

class PermutationIterator:
	def __init__(self, L):
		self.counter = 0
		self.length_for_counter = len(L) - 1
		self.true_length = len(L)
		self.l = L

	def __iter__(self):
		return self

	def __next__(self):
		for index, element in enumerate(self.l):
			theRest = self.l[:index] + self.l[index + 1:]
			print([element] + theRest)
			print([element] + theRest[::-1])
		raise StopIteration()

def main():
	# NOTE TO SELF: REMOVE TEST LIST CODE BEFORE SUBMITTING
	numList1 = [1, 2, 3, 4, 5] # keep
	#numList2 = [1, 2, 3, 4]
	#numList3 = [1, 2, 3]
	#numList4 = [1, 2]
	#numList5 = [1]
	letterList1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # keep
	letterList2 = ['b', 'c', 'a'] # keep
	#letterList3 = ['k', 'y']
	#letterList4 = ['x']

	print("Permutations of list [1, 2, 3, 4, 5]:")
	for permutation in PermutationIterator(numList1):
		print(permutation)

	#print()

	#print("Permutations of list [1, 2, 3, 4]:")
	#for permutation in PermutationIterator(numList2):
	#	print(permutation)

	#print()

	#print("Permutations of list [1, 2, 3]:")
	#for permutation in PermutationIterator(numList3):
	#	print(permutation)

	#print()

	#print("Permutations of list [1, 2]:")
	#for permutation in PermutationIterator(numList4):
	#	print(permutation)

	#print()

	#print("Permutations of list [1]:")
	#for permutation in PermutationIterator(numList5):
	#	print(permutation)

	print()
		
	print("Permutations of list ['a', 'b', 'c', 'd', 'e', 'f', 'g']:")
	for permutation in PermutationIterator(letterList1):
		print(permutation)

	print()

	print("Permutations of list ['b', 'c', 'a']:")
	for permutation in PermutationIterator(letterList2):
		print(permutation)

	#print()

	#print("Permutations of list ['k', 'y']:")
	#for permutation in PermutationIterator(letterList3):
	#	print(permutation)

	#print()

	#print("Permutations of list ['x']:")
	#for permutation in PermutationIterator(letterList4):
	#	print(permutation)

if __name__ == "__main__":
	main()