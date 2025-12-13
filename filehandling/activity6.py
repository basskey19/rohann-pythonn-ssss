with open("sample.txt","w") as file:
    file.write("Hello,tch tch mic testing.\n")
    file.write("we are checking,if the mic was working:>.\n")
print("Alright it is working Perfectly.")

#using write function along with split
text = "at first mic wasn't working but after some testing it WORKED"
with open("sample.txt","w") as file:
    words = text.split()
    print("trying to check what happens after splitiing a MIC :(   ",words)
    for i in words:
        file.write(i + "\n")
print("words written to words.txt succesfully")          