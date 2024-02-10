#                                                                            𝔻𝕒𝕥𝕒 𝕋𝕪𝕡𝕖𝕤 🙌🙌🙌

# #<----------------------------------------------------------------------------- >🙂Strings--------------------------------------------------------------------------------------------------->
# #Concatination
# str1 = "Hello"
# str2 = "World"
# result = str1 + " " + str2
# print(result)

# #<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# #length 
# length = len(result)
# print ("Length of result --> ", length)

# #<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# #Upper Case  &  Lower Case
# uppercase = result.upper()
# lowercase = result.lower()
# print("UpperCase : ", uppercase)
# print("LowerCase : ", lowercase)

# #<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# #Replace Text
# new_txt = result.replace("Hello World", "Hemlo Domsto")
# print("new text : ",new_txt)

# #<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# #Split Text
# words = result.split()
# print("Split : " , words)

# #<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# #Strip --> remove space from front and behind of the text
# stripped_text = result.strip()
# print("Stripped text:", stripped_text)

# #<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# #Availability
# text = "Python is awesome"
# substring = "is"
# if substring in text:
#     print("substring found in text")

# #<-------------------------------------------------------------------------------🙂Numberic Data Type-------------------------------------------------------------------------------------->
# # Float variables
# num1 = 5.0
# num2 = 2.5

# # Basic Arithmetic
# result1 = num1 + num2
# print("Addition:", result1)

# result2 = num1 - num2
# print("Subtraction:", result2)

# result3 = num1 * num2
# print("Multiplication:", result3)

# result4 = num1 / num2
# print("Division:", result4)

# # Rounding
# result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
# print("Rounded:", result5)  

# # Integer variables
# num1 = 10
# num2 = 5

# # Integer Division
# result1 = num1 // num2
# print("Integer Division:", result1)

# # Modulus (Remainder)
# result2 = num1 % num2
# print("Modulus (Remainder):", result2)

# # Absolute Value
# result3 = abs(-7)
# print("Absolute Value:", result3)

# #<-----------------------------------------------------------------------------😲Regex(Reg-regular, ex-expression)----------------------------------------------------------------------->
# #Find/Search
# import re

# text = "Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing. The re module in Python is used for working with regular expressions. Examples of regex usage: matching emails, phone numbers, or extracting data from text."
# pattern = "expressions"

# exist = re.search(pattern, text)
# if exist:
#     print("exist : " , exist.group() )
# else:
#     print("does not exist")

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
#match
import re

text = "The quick brown fox. Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing. The re module in Python is used for working with regular expressions. Examples of regex usage: matching emails, phone numbers, or extracting data from text."
pattern = "The quick brownfox"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
#replace
pattern = "expressions"
replacement = "💀💀💀💀"
new_text = re.sub(pattern,replacement,text)
print("Text --> " , text )
print("New Text --> " , new_text )

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
#search
split_result = re.split(pattern, text)
print("Split result:", split_result)























#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->


#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->