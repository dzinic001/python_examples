def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Beispielaufruf
result = is_palindrome("A man a plan a canal Panama")
print(result)