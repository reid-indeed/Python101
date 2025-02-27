from sys import argv 

script,filename = argv

print(f"We're going to erase {filename}.")

print("If you don't want that, hit CTRL-C (^C).)")

print("If you want to continue, hit RETURN (or ENTER, for all the modern folks who have never heard of RETURN).")
      
#input("?")

      
print(f"Opening: {filename}")
      
target = open(filename, 'w') 

print("Truncating the file. Goodbye!")
target.truncate() 

#print("Now I'm going to ask you for three lines.")

#line1 = input("line1: ") 

#print("I'm going to write to the file.")

#target.write(line1) 
#target.write("\n") 

print("And finally, we close it.")
target.close() 