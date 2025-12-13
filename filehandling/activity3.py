file = open('sample.txt','a')
file.write("\n hey new changes are here bc of A mode")
file.close()

file = open("sample.txt", "r")
text = file.read()
print(text)
file.close()