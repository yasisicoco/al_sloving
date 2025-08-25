import sys
input = sys.stdin.readline

n, m = map(int, input().split())
salary = list(map(int, input().split()))

max_salary = 0
if m == 0:
    print(0)    
else:
    cur = sum(salary[:m])
    max_salary = cur

    for i in range(m, n):
        cur = cur - salary[i-m] + salary[i]
        if cur > max_salary:
            max_salary = cur

print(max_salary)