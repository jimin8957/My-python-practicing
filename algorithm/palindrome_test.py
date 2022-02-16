def is_palindrome(word):
    i = 0
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

def is_palindrome2(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

# 테스트
print(is_palindrome2("racecar"))
print(is_palindrome2("stars"))
print(is_palindrome2("토마토"))
print(is_palindrome2("kayak"))
print(is_palindrome2("hello"))