#creating a function that takes a value and prints the order of frequency using dictonary
def char_frequency(str1):
    dict={}
    for s in str1:
        keys=dict.keys()
        if(s in keys):
            dict[s]+=1
        else:
             dict[s]=1
    return dict
a=input("Enter a string:")
frequency=char_frequency(a)
print(frequency)
                
