def duplicate_encode(word):
    lower = word.lower()
    return ''.join(['(' if lower.count(char) == 1 else ')' for char in lower])


conv = duplicate_encode('Petele')


# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
def persistence(n):
    n_to_string = str(n)
    res = 1
    while res >= 10:
        for number in n_to_string:
            digit = int(number)
            res *= digit
        
        return res


res = persistence(245)


print(res)
