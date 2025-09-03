# You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…
# Sample Input: 
# 7
# Sample Output: 
# 3 6 12 24 48 96 192
# Explanation: The series starts with 3 and every time multiplies 2 to get the next term.

def print_series(n):
    term = 3
    for _ in range(n):
        print(term, end=" ")
        term *= 2


n = int(input("Enter number:"))  
print_series(n)
