# String and Text Manipulation – Interview Questions
# ________________________________________
# 1. Remove Spaces from Given Text
# Problem: Write a function to remove all spaces from the input string. Explanation: Remove any whitespace characters. Input: "he llo wor ld" Output: "helloworld"
# name="he llo wor ld"
# result=name.replace(" ","")
# print(result)

# s="he llo world"
# rel=""
# for i in s:
#     if i!=" ":
#         rel+=i
# print(rel)

# def spaces(s):
#     rel=""
#     for i in s:
#         if i!=" ":
#          rel+=i
#     print(rel)
# spaces("he llo world")

# 2. Reverse a String
# Problem: Write a function to reverse the characters in a string. Input: "hello" Output: "olleh"
# str="hello"
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)

# s="hello"
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)


# def revers(s):
#     rev=""
#     for i in range(len(s)-1,-1,-1):
#         rev+=s[i]
#     print(rev)
# revers("hello")

# 3. Reverse a String After Removing Spaces
# Problem: Write a function to reverse a string after removing all spaces. Input: "he llo world" Output: "dlrowolleh"
# str1="he llo world"
# result=str1.replace(" ","")
# rev=""
# for i in result:
#     rev=i+rev
# print(rev)

# s="he llo world"
# res=""
# for i in s:
#     if i!=" ":
#         res+=i
#     print(res)

   


# 4. Convert Snake Case to Camel Case
# Problem: Convert a string from snake_case to camelCase. Input: "my_variable_name" Output: "myVariableName"
# s="my_variable_name"
# res=""
# under_score=False
# for i in range(len(s)):
#     if s[i]=="_":
#         under_score=True
#     elif under_score:
#         res+=s[i].upper()
#         under_score=False
#     else:
#         res+=s[i]
# print(res)

# s="my_variable_name"
# res=""
# under_score=False
# for i in range(len(s)):
#     if i==0:
#         res=s[i].upper()
#     elif s[i]=="_":
#         under_score=True
#     elif under_score:
#         res+=s[i].upper()
#         under_score=False
#     else:
#         res+=s[i]
# print(res)

# a="hello"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# list="hello"
# print(list[::-1])



# 5. Convert Snake Case to Pascal Case
# Problem: Convert a string from snake_case to PascalCase. Input: "my_variable_name" Output: "MyVariableName"
# s="my_variable_name"
# rev=""
# under_score=False
# for i in range(len(s)):
#     if i==0:
#         rev=s[i].upper()
#     elif s[i]=="_":
#         cond=True
#     elif under_score:
#         rev+=s[i].upper()
#         under_score=False
#     else:
#         rev+=s[i]
# print(rev)

# 6. Convert Camel Case to Snake Case
# Problem: Convert a string from camelCase to snake_case. Input: "myVariableName" Output: "my_variable_name"

# s="myVariableName"
# res=""
# under_scor=True
# for i in range(len(s)):
#     if s[i]=="_":
#        code=True
#     elif s[i].isupper():
#         res += "_" + s[i].lower()
#         under_scor=True
#     else:
#         res+=s[i]
# print(res)


# 7. Convert Camel Case to Pascal Case
# Problem: Convert a string from camelCase to PascalCase. Input: "myVariable" Output: "MyVariable"
# s="myVariable"
# res=""
# under_scor=True
# for i in range(len(s)):
#     if i==0:
#         res+=s[i].upper()
#     elif s[i]=="_":
#        code=True
#     elif s[i].isupper():
#         res +=s[i].upper()
#         under_scor=True
#     else:
#         res+=s[i]
# print(res)

# 8. Convert Pascal Case to Camel Case
# Problem: Convert a string from PascalCase to camelCase. Input: "MyVariable" Output: "myVariable"
# s="MyVariable"
# rev=""
# under_score=True
# for i in range(len(s)):
#     if i==0:
#         rev+=s[i].lower()
#     elif s[i]=="_":
#         condiction=True
#     elif s[i].isupper():
#         rev+=s[i].upper()
#         condction=True
#     else:
#         rev+=s[i].lower()
# print(rev)


# 9. Convert Pascal Case to Snake Case
# Problem: Convert a string from PascalCase to snake_case. Input: "MyVariable" Output: "my_variable"
# s="MyVariable"
# res=""
# under_code=True
# for i in range(len(s)):
#     if i==0:
#         res+=s[i].lower()
#     elif s[i]=="_":
#         condction=True
   
#     elif s[i].isupper():
#            res += "_" + s[i].lower()
#            condction=True
#     else:
#         res+=s[i].lower()
# print(res)

# 10. Convert Text to Camel Case
# Problem: Convert a space-separated sentence into camelCase. Input: "hello world example" Output: "helloWorldExample"

# s="hello world example"
# rev=""
# coud=False
# for i in range(len(s)):
#     if s[i]==" ":
#         coud=True
#     elif coud:
#         rev+=s[i].upper()
#         coud=False
#     else:
#         rev+=s[i]
# print(rev)

# 11. Convert Text to Snake Case
# Problem: Convert a space-separated sentence into snake_case. Input: "hello world example" Output: "hello_world_example"

# s="hello world example"
# rev=""
# cond=False
# for i in range(len(s)):
#     if s[i]==" ":
#         rev+="_"+s[i].lower()
#         cond=True
#     elif cond:
#         rev+=s[i].lower()
#         cond =False
#     else:
#         rev+=s[i]
# print(rev)


# 12. Convert Text to Pascal Case
# Problem: Convert a space-separated sentence into PascalCase. Input: "hello world example" Output: "HelloWorldExample"

# s="hello world example"
# rev=""
# cond=True
# for i in range(len(s)):
#     if s[i]==" ":
#         cond=True
#     elif cond:
#         rev+=s[i].upper()
#         cond=False
#     else:
#         rev+=s[i]
# print(rev)

# 13. Swap Upper and Lower Case
# Problem: Swap the case of each letter in a given string. Input: "HeLLo" Output: "hEllO"

# s="HeLLo"
# res=""
# for i in s:
#     if i.isupper():
#         res+=i.lower()
#     else:
#         res+=i.upper()
# print(res)


# 14. Separate Digits from Text
# Problem: Extract all digits from a given alphanumeric string. Input: "abc123d4" Output: "1234"
# d="abc123d4"
# res=""
# for i in d:
#     if i>="0" and i<="9":
#         res+=i
# print(res)


# 15. Print Uppercase, Lowercase, Digits, and Special Characters Separately
# Problem: Print each type of character separately from the string. Input: "Abc123!@#" Output:
# Uppercase: A
# Lowercase: b c
# Digits: 1 2 3
# Special Characters: ! @ #

# s="Abc123!@#"
# upper=""
# lower=""
# number=""
# spiceal=""
# for i in s:
#     if i>="A" and i<="Z":
#         upper+=i+""
#     elif i>="a" and i<="z":
#         lower+=i+""
#     elif i>="0" and i<="9":
#         number+=i+""
#     else:
#         spiceal+=i+""
# print(upper)
# print(lower)
# print(number)
# print(spiceal)





# 16. Count of Uppercase, Lowercase, Digits, and Special Characters
# Problem: Count each type of character in a string. Input: "AbC@123x!" Output:
# Uppercase: 2
# Lowercase: 1
# Digits: 3
# Special Characters: 2

# s="AbC@123x!"
# count_upper=0
# count_lower=0
# count_number=0
# count_spiceal=0

# for i in s:
#     if i>="A" and i<="Z":
#         count_upper+=1
#     elif i>="a" and i<="z":
#         count_lower=1
#     elif i>="0" and i<="9":
#         count_number+=1
#     else:
#         count_spiceal+=1
# print("upper_count",count_upper)
# print("lower_count",count_lower)
# print("number_count",count_number)
# print("spiceal_count",count_spiceal)



# 17. Check Password Strength
# Problem: Check if a password contains at least one uppercase, one lowercase, one digit, and one special character. Input: "Pass123!" Output: "Strong Password"
# p="Pass123!"
# upper=0
# lower=0
# number=0
# spiceal=0
# for i in p:
#     if i>="A" and i<="Z":
#         upper+=1
#     elif i>="a" and i<="z":
#         lower=1
#     elif i>="0" and i<="9":
#         number+=1
#     else:
#         spiceal+=1

# print("upper_count",upper)
# print("lower_count",lower)
# print("number_count",number)
# print("spiceal_count",spiceal)
# if upper>0 and lower>0 and number>0 and spiceal>0:
#     print("strong pasword")
# else:
#     print("not strong pasword")


# 18. Remove Duplicates in a Given Input
# Problem: Remove duplicate characters from a string. Input: "aabbcc" Output: "abc"
# s="aabbcc"
# rem=""
# for i in s:
#     if ("a">=1 and "b">=1 and "c">=1):
#         rem+=i
#     else:
#         rem-=i
# print(rem)


# 19. Print Duplicates in a Given String
# Problem: Identify and print duplicate characters in a string. Input: "aabbccde" Output: a b c
# str="aabbccde"
# dub=""
# for i in str:
#     if str.count(i) and i not in dub:
#         dub+=i+" "
    
# print(dub)

# 20. Print Next Characters in a Given String
# Problem: Replace each character in the string with its next character. Input: "abc" Output: "bcd"

# str="abc"
# rev=""
# for i in str:
#     rev+=chr(ord(i)+1)
# print(rev)
