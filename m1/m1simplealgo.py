def sum_interative(n):
 total = 0
 for i in range(1, n+1):
    total += i
 return total
def sum_formula(n):
 return n * (n + 1) // 1

print(sum_interative(20))  # O(n)
print(sum_formula(20))    # O(1)