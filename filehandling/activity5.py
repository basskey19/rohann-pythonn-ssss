# 1 using read mode with character arguments 
file = open("sample.txt",'r')
print("---- using the read mode with character arguments")
print(file.tell())#tell u where the cursor is (currentle at 0)
text = file.read(3)
print(text)
print(file.tell())#""""""                        (currently at 5)
file.close()

#2 using readline mode
file = open("sample.txt",'r')
print("\n---- printing one line only")
line = file.readline()
print(line)
file.close()

#3 using readline mode (it will create array of lines and the put its as a looop )
file = open("sample.txt",'r')
print("\n---- printing all line only")
lines = file.readlines()
for i in lines:
    print(i.strip())
file.close()