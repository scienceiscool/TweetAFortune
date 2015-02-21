CS223P - Python Programming

Author Name: Kathy Saad<br>
Project Title: Assignment 6 - Generators and Iterators - Permutations<br>
Project Status: Working<br>
External Resources:<br>
- Class notes<br>
- https://www.python.org/<br>

Instructions:

Write a class named Permutation that will generate on demand all the permutations of a given list. Write a short main function that demonstrates its use on the following lists:<br>
[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['b', 'c', 'a'].<br>
(Do not use anything from the itertools module)

Sample Run:

	python3.4 permutation.py 
	Permutations of list [1, 2, 3, 4, 5]:
	[1, 2, 3, 4, 5]
	[1, 5, 4, 3, 2]
	[2, 1, 3, 4, 5]
	[2, 5, 4, 3, 1]
	[3, 1, 2, 4, 5]
	[3, 5, 4, 2, 1]
	[4, 1, 2, 3, 5]
	[4, 5, 3, 2, 1]
	[5, 1, 2, 3, 4]
	[5, 4, 3, 2, 1]

	Permutations of list ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
	['a', 'b', 'c', 'd', 'e', 'f', 'g']
	['a', 'g', 'f', 'e', 'd', 'c', 'b']
	['b', 'a', 'c', 'd', 'e', 'f', 'g']
	['b', 'g', 'f', 'e', 'd', 'c', 'a']
	['c', 'a', 'b', 'd', 'e', 'f', 'g']
	['c', 'g', 'f', 'e', 'd', 'b', 'a']
	['d', 'a', 'b', 'c', 'e', 'f', 'g']
	['d', 'g', 'f', 'e', 'c', 'b', 'a']
	['e', 'a', 'b', 'c', 'd', 'f', 'g']
	['e', 'g', 'f', 'd', 'c', 'b', 'a']
	['f', 'a', 'b', 'c', 'd', 'e', 'g']
	['f', 'g', 'e', 'd', 'c', 'b', 'a']
	['g', 'a', 'b', 'c', 'd', 'e', 'f']
	['g', 'f', 'e', 'd', 'c', 'b', 'a']

	Permutations of list ['b', 'c', 'a']:
	['b', 'c', 'a']
	['b', 'a', 'c']
	['c', 'b', 'a']
	['c', 'a', 'b']
	['a', 'b', 'c']
	['a', 'c', 'b']