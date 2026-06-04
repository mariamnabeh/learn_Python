"""
Write a Python function called reverseFile(file_name) that reserves the content of a text file called numbers.txt then write the new reversed
content in the same file. All values should be given and not received from the user.
"""
def reverseFile(file_name):
    with open("file_name",'r') as f:
        lines=f.readline()
        with open("file_name","w") as f:
         f.writelines(lines[::-1])
    
reverseFile("number.txt")
            