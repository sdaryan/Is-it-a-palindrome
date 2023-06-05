# Is it a palindrome
# آیا Palindrome است؟

my_string=input().lower()
if my_string == my_string[::-1]:
    print("palindrome")
else:
    print("not palindrome")