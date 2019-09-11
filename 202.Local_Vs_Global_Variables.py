val1 = 100;
val2 = 200;

print(val1);
print(val2);

def ChangeValue():
	global val1
	val1 = "global variable val1"
	val2 = "global variable val2"
	print(val1)
	print(val2)

ChangeValue();


print(val1);
print(val2);
