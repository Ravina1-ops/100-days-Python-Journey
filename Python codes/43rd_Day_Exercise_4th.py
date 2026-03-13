'''
EXERCISE 4: SECRET CODE LANGUAGE
--------------------------------

Write a python program to translate a message into secret code language. 
Use the rules below to translate normal English into secret code language and vice-versa.

RULES FOR CODING:
1. If the word contains at least 3 characters:
   - Remove the first letter and append it at the end.
   - Now append three random characters at the starting and at the end.
2. Else (if the word contains less than 3 characters):
   - Simply reverse the string.

RULES FOR DECODING:
1. If the word contains less than 3 characters:
   - Reverse it back to original.
2. Else (if the word contains at least 3 characters):
   - Remove 3 random characters from the start and 3 from the end.
   - Take the last letter and move it to the beginning.

GOAL:
- Ask the user whether they want to 'Code' or 'Decode'.
- Take the input message and perform the conversion.
- Print the final result.
'''

# Code by me  : 
import random
choice = input("What you want (Code (c) or Decode(dc)): ").lower()
message = input("Enter your word: ")
words =  message.split(" ")
new_words = []
if(choice == 'c' ):
   for word in words:
      if len(word) >= 3:
       r1 = "lvk"
       r2 = "pro"
       stnew = r1 + word[1:] + word[0] + r2
       new_words.append(stnew)
      else:
        new_words.append(word[::-1])
   print("Encoded message"," ".join(new_words))
elif choice == 'dc':
  for word in words:
    if len(word) >= 3:
      temp = word[3:-3]
      if len(temp) > 0:
       stnew = temp[-1] + temp[:-1]
       new_words.append(stnew)
      else:
        new_words.append(word)
    else: 
      new_words.append(word[::-1])
  print("Decoded Message :", " ".join(new_words))
else: 
  print("Invalid choice! Please enter 'c' or 'dc'.")


# Exercise 4: Secret Code Language - Solution by CodeWithHarry

# st = input("Enter message: ")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding: ")
# coding = True if (coding == "1") else False

# print(coding)

# if(coding):
#     nwords = []
#     for word in words:
#         if(len(word) >= 3):
#             # Rule for Coding:
#             # 1. Remove first letter and append it at the end
#             # 2. Append 3 random characters at the start and the end
#             r1 = "dsf" # In the video, Harry uses hardcoded strings 
#             r2 = "jkr" # but suggests using the random module as an upgrade
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             # If word length < 3, simply reverse the string
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

# else:
#     nwords = []
#     for word in words:
#         if(len(word) >= 3):
#             # Rule for Decoding:
#             # 1. Remove 3 random characters from start and end
#             # 2. Remove the last letter and append it to the beginning
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             # Reverse the string back
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

  

