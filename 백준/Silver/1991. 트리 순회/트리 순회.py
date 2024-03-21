N = int(input())
par = [0] * N
left = [0] * N
right = [0] * N

for i in range(N):
    a, b, c = input().split()
    par[i] = a
    left[i] = b
    right[i] = c

# print(par); print(left); print(right)

def preorder(cur):
    print(par[cur], end='')
    if left[cur] != '.':
        preorder(par.index(left[cur]))
    if right[cur] != '.':
        preorder(par.index(right[cur]))

def inorder(cur):
    if left[cur] != '.':
        inorder(par.index(left[cur]))
    print(par[cur], end='')
    if right[cur] != '.':
        inorder(par.index(right[cur]))

def postorder(cur):
    if left[cur] != '.':
        postorder(par.index(left[cur]))
    if right[cur] != '.':
        postorder(par.index(right[cur]))
    print(par[cur], end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)