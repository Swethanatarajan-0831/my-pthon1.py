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
