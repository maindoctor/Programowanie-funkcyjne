def is_palindrome(s):
    return ''.join(char.lower() for char in s if char.isalnum()) == ''.join(char.lower() for char in reversed(s) if char.isalnum())

print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("race car"))
print(is_palindrome("hello"))
