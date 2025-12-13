file = open('sample.txt', 'w')
file.write("this is changed write mode FH")
file.close()

file = open("sample.txt","r")
text = file.read()
print(text)
file.close()