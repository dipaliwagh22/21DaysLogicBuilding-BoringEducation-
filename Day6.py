# Star Pattern 1:
# Print the following pattern based on the given input.
# Sample Input: 
# 6
# Sample Output: 
# *
# **
# ***
# ****
# *****
# ******
# Explanation: Since the input is 6, it prints a total of 6 lines. In each line, the star count increases.
n = int(input("Enter:"))
for i in range(1, n + 1):
    print('*' * i)
