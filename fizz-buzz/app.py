def convert(n:int)->str:
    result = ""
    if n%3==0:
        result += "Fizz"
    if n%5==0:
        result += "Buzz"
    return result if len(result) else str(n)