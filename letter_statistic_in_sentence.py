sentence=input("Enter a sentecte : ")

dictionary={}
sentence=sentence.replace(" ","")

for i in sentence:
    if i in dictionary:
        dictionary[i]=dictionary[i]+1
    else:
        dictionary[i]=1


print("-LETTER STATİC İN SENTENCE-")

for i in dictionary:
    print(i,"---->",dictionary[i])


print("%d Kind Of Letter"%(len(dictionary)))