def solution(numer1, denom1, numer2, denom2):
    bunmo = denom1 * denom2
    bunja = denom1 * numer2 + denom2 * numer1
    
    def gongyaksu(a, b):
        while b:
            a, b = b, a % b
        return a
    
    val = gongyaksu(bunja, bunmo)
        
    result = [bunja // val, bunmo // val]
    return result