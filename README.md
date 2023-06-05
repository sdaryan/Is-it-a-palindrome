## Is it a palindrome

Zargiso, who has just become familiar with programming, wants to write a program that determines whether a word is a palindrome or not. A word is called a palindrome if it reads the same from left to right as from right to left. For example, "Madam" is a palindrome but "Tehran" is not. Now you need to help Zargiso write this program.

Please note that the capitalization of letters does not matter. As we mentioned, "Madam" is a palindrome, and so is "maDAM".

## Input:
```python
madam
```

## Output:
```python
palindrome
```

------------------------------------------------------------------------------
## آیا Palindrome است؟

زرگیسو که تازه با برنامه نویسی آشنا شده می خواد برنامه ای بنویسه که تعیین کنه آیا یک کلمه palindrome هست یا خیر. به کلمه ای میگن palindrome که چه از چپ چه از راست بخونیش یه چیز بشه. مثلا Madam یه palindrome هستش ولی tehran یک palindrome نیست. حالا شما باید به زرگیسو کمک کنی این برنامه رو بنویسه.
لطفا توجه کنید که کوچک یا بزرگ بودن حروف مهم نیست همونطور که گفتیم Madam یک palindrome هست همانطور که maDAM یک palindrome است.

## ورودی نمونه
```python
madam
```
## خروجی نمونه
```python
palindrome
```
## ورودی نمونه
```python
tehran
```
## خروجی نمونه
```python
not palindrome
```
روش اول
```python
my_string = "level"
if my_string == "".join(reversed(my_string)):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
```
روش دوم
```python
my_string = "level"
if my_string == my_string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

```
