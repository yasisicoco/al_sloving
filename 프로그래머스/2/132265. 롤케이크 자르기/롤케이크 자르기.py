def solution(topping):
    topping_cnt = {}
    for t in topping:
        if t in topping_cnt:
            topping_cnt[t] += 1
        else:
            topping_cnt[t] = 1
            
    bro = set()
    me = set(topping)
    ans = 0
    
    for t in topping:
        bro.add(t)

        topping_cnt[t] -= 1
        if topping_cnt[t] == 0:
            me.remove(t)
            
        if len(bro) == len(me):
            ans += 1
            
    return ans