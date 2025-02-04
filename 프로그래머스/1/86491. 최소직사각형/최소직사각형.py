def solution(sizes):
    row_val = 0
    col_val = 0
    result = 0
    for size in sizes:
        row, col = min(size), max(size)
        row_val = max(row_val, row)
        col_val = max(col_val, col)
        
        print(row_val, col_val)
        result = row_val * col_val
        
    return result