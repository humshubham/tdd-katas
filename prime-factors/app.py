def prime_factors(n:int):
    factors_list = []
    if n>1:
        while n%2==0:
            factors_list.append(2)
            n //= 2
    if n>1:
        factors_list.append(n)
    return factors_list