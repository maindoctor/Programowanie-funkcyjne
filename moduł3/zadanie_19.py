def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
result = check_anagrams(str1, str2)
print(result)
