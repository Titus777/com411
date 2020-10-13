print("Program Started")
print("please enter an ASCII code")
code = int(input())

lowv = 32
highv = 127 
if code in range(lowv, highv) :
 letter = chr(code)
 print("The character represented by the ASCII code {} is {}". format(code,letter))
else:
 print("The value entered is outside of the ASCII code range") 

 print("Program ended")