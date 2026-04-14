'''
Exercise 7: Clear the Clutter
Write a program to clear the clutter inside a folder on your computer.
You should use the os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder.
Do the same for other file formats as well.
'''
import os

# Create a dummy folder and files to test this logic
# os.rename("oldname.txt", "newname.txt")

# Exercise 7 Solution


files = os.listdir("clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
        i += 1