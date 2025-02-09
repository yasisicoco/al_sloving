def solution(chicken):    
    serviceChic = 0
    coupon = chicken
    while True:
        if coupon < 10:
            break
        
        coupon -= 10
        serviceChic += 1
        coupon += 1
        
    return serviceChic