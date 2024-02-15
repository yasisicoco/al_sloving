import sys

def dus(cur):
    if cur[0] == 'push':
        st.append(int(cur[1]))
    elif cur[0] == 'pop':
        if st == []:
            print(-1)
        else:
            print(st.pop())
    elif cur[0] == 'size':
        print(len(st))
    elif cur[0] == 'empty':
        if st:
            print(0)
        else:
            print(1)
    elif cur[0] == 'top':
        if st == []:
            print(-1)
        else:
            print(st[-1])
        
N = int(input())
st = []
for _ in range(N):
    a = sys.stdin.readline().split()
    
    dus(a)