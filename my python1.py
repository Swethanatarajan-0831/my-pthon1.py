TASK:1
#radius of a circle
r=float(input("Enter radius of circle :"))
a=3.14159*r*r
print("Area of circle=",a)

TASK:1
#filename and printing its extension
filename=input("Enter a filename:")
x=list(filename.split("."))
del x[0]
if x==['py']:
    print("The extension of the file is python")
elif x==['html']:
    print("The extension of the file is hypertext markup language")
elif x==['c']:
    print("The extension of the file is c")
elif x==['c++']:
    print("The extension  of the file is c++")
else:
    print("Enter the correct extension")


