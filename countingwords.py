introstring=input("enter a paragraph ")
charactercount=0
wordcount=1
for i in introstring:
    charactercount=charactercount+1
    if(i==' '):
        wordcount=wordcount+1
print("number of words in this string")
print(wordcount)
print("number of charecters in this string")
print(charactercount)