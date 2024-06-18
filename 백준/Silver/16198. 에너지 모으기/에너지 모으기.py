N = int(input())
energy = list(map(int, input().split()))

def charge(energy, cur):    
    if len(energy) == 2:
        return cur
        
    max_val = 0
    for i in range(1, len(energy)-1):
        sumone = energy[i-1] * energy[i+1]
        new_val = energy[:i] + energy[(i+1):]
        max_val = max(max_val, charge(new_val, cur + sumone))
    
    return max_val

print(charge(energy, 0))