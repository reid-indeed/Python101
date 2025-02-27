#import sys from the argv module/library
from sys import argv

# Get argv to store 3 user-defined variables. 
# 'script' is a reserved code word meaning the file name of the Python script (in this case 'ex-13.py')

script, first, second, third = argv

#print the 3 user-defined variables stored in argv that were typed on the 'command line'

print(f"""
    The first variable written on the command line, after 'python' and the script name is: {first}
    
    The first variable written on the command line, after 'python' and the script name is: {second}
    
    The first variable written on the command line, after 'python' and the script name is: {third}
    """)