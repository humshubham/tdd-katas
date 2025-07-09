def prime_factors(n:int):
    
    factors_list = []
    divisor = 2

    while n>1:
        while n%divisor==0:
            factors_list.append(divisor)
            n //= divisor
        divisor+=1

    return factors_list