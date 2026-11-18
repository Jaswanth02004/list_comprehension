#ONE, Basic list variable operation, [expression for item in iterable if condition]
'''
a = [2,4,6,8]
result = [val**2 for val in a]
print(result)
'''


#THE ABOVE IS SAME AS BELOW (using LAMBDA)
'''
a = [2, 3, 4, 5]
res = list(map(lambda val:val**2, a))
print(res)
'''


#TWO, Conditional statements
'''
a = [1,2,3,4,5,6,7,8,9]
result_1 = [val for val in a if val%2 == 0]
result_2 = [val for val in a if val >= 5]
print(result_1)
print(result_2)
'''


#THREE, creating a list from empty list
'''
a = []
result = [(i,j) for i in range(3) for j in range(3)]
print(result)
'''


#Four, Handling a MATRIX or a Nested list.
'''
a = [[1,2,3], [4,5,6], [7,8,9]]
result = [y for x in a for y in x ]
print(a)
print(result)
'''



'''
#FOR LOOP:  1. Uses multiple lines of code
            2. Requires manual appending of elements
            3. But, Better for complex logic and conditions
            
#List Comprehension:1. Uses a single line of code
                    2. Creates the list directly
                    3. But, Better for simple and concise operations only
'''
