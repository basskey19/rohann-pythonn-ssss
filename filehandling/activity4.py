file = open('sample.txt','r')
print("file in read mode -")
text = file.read()
print(text)
file.close()

file = open('sample.txt', 'w')
file.write("file in write mode")
file.write("hello! iam pennywise i like chilldren for breakfast")
file.close()


file = open('sample.txt', 'a')
file.write("\n file in append mode")
file.write("hello! iam pennywise i like chilldren for breakfast")
file.close()