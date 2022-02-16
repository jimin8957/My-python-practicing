def sum_digit(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum


k = 0
ssum = 0
for k in range(1, 1001):
    ssum += int(sum_digit(k))

print(ssum)



def mask_security_number(security_number):
    str_sec = security_number
    k = len(str_sec) - 4
    str_sec = str_sec[0: k] + "****"
    return str_sec

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

print(is_palindrome("racecar"))

