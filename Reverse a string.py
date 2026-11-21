def reverse(s):
    str=" "d
    for i in s:
        str=i+str
    return str
s=input("Enter a string ")
print("Original string is",s)
print("the reversed string is",reverse(s))
