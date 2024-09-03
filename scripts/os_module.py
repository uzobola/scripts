#Create a Python script that counts the number of items (files and directories) in a specified directory(take dir as input). 
#The script should display the total number of items (both files and directories) present in the specified directory.
# Bonus Modify your script to count the number of files and directories separately. Hint: use the os module






import os

def count_dir(dir):
  files = os.listdir(dir)
  count_files = len(files)
  print(f"You have {files} files in this directory")



dir= input("Please center path of directory:")
count_dir(dir)
