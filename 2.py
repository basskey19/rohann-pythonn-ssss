text1 = input("please enter your First String as Text1 :")
text2 = input("please enter your Second String as Text2 :")


print("/nJoining two strings :",text1 + "" + text2)

print("/nConverting Alphabets into Uppercase :", text1.upper(),text2.upper())

print("/nConverting Alphabets into lowercase :", text1.lower(),text2.lower())

print("/nSlicing the text string '",text1[0:5])

print("/nRepeating the string 1 and 1 two times :",text1*2,text2*2)

print("n/Length of the string 1 and 2 :",len(text1),len(text2))

print("/nPrinting Reverse of the string :",text1[::-1],text2[::-1])