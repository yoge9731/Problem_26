"""Count Vowels in a String:

Write a program that counts how many vowels are in a given string using a for loop."""

vowels = "aeiou"
s="this is yogee"
count=0
for letters in s:
    if letters in vowels:
        count = count +1

print(count)

#1
"""Count vowels in a String:
Write a Program that counts how many vowels are in a string using a for loop"""
vowels="aeiou"
s="Hi I am Yogee How are you"
count = 0
for letters in s:
    if letters in vowels:
        count=count+1
print(count)

#2
vowels="aeiou"
s="hi how are you"
count=0
for i in s:
    if i in vowels:
        count = count+1
print(count)

#3
vowels="aeiou"
s="how are you"
count=0
for i in s:
    if i in vowels:
        count=count+1
print(count)

#4
vowels="aeiou"
s="how are you"
count=count+1
for i in s:
    if i in vowels:
        count=count+1
print(count)

#5
vowels="aeiou"
s="how are you"
count=0
for i in s:
    if i in vowels:
        count=count+1
print(count)
