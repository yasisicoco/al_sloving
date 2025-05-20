def solution(info, n, m):
    length = len(info)
    memo = {} 

    def dfs(index, a_trace, b_trace):
        if a_trace >= n or b_trace >= m:
            return float('inf')  

        if index == length:
            return a_trace

        key = (index, a_trace, b_trace)
        if key in memo:
            return memo[key]

        a_choice = dfs(index + 1, a_trace + info[index][0], b_trace)
        b_choice = dfs(index + 1, a_trace, b_trace + info[index][1])

        memo[key] = min(a_choice, b_choice)
        return memo[key]

    result = dfs(0, 0, 0)
    # for k, v in memo.items():
    #     print(f"{k}: {v}")
    return result if result != float('inf') else -1
