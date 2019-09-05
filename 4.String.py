#Accessing Values in Strings
var1 = "Hello World"
var2 = "Python Development"
print("Access values in string")
print("var1[0]:",var1[0])
print("var2[1:5]:",var2[1:5])
print("---------------")
print('\n')

#Contact
x = "Hello World!"
print( "Contact string")
print( x[:6] )
print( x[0:6] + "User")
print("---------------")
print('\n')

#Python String replace() Method
oldstring = 'I like Python' 
newstring = oldstring.replace('like', 'love')
print( "replace()")
print( oldstring )
print( newstring)

oldstring = 'I like Python' 
oldstring.replace('like', 'love')
print( oldstring )
print("---------------")
print('\n')

#Changing upper and lower case strings
print( "Working with cases")
string="python"
print( string.upper())
string="python"		
print( string.capitalize())
string="PYTHON"
print( string.lower())
print("---------------")
print('\n')

#Using "join" function for the string
print( "Working with join")
print(":".join("Python"))	
print("---------------")
print('\n')
	
#Reversing String
print( "Working with reversed")
string="Python"		
print(''.join(reversed(string)))
print("---------------")
print('\n')

#Split Strings
print( "Working with split")
word="Python Development"		
print( word.split(' '))
word="Python Development"		
print( word.split('o'))
print("---------------")
print('\n')

#Double the word
print ("Working with double the word")
x="Python Developer"
print(x*2)
print("---------------")
print('\n')

#Cast To string
print( "String cast")
x=100
print("Python is "+str(x))
print("---------------")
print('\n')

#string format
print ("String format")
name = "Python"
number = 99
print("%s %d" % (name,number))
