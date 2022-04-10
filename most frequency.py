def most_frequent(str1):
    dict1=dict()
    for i in str1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    print(sorted(dict1.items(),key =
             lambda kv:(kv[1], kv[0]),reverse=True))
string=input("enter a string ")
most_frequent(string)
