count = 1
while True:
    res = input("press enter to contiue and type exit to stop")
    if res.lower() == "exit":
        print("goodbye")
        break
    else:
        print(f"counter is at {count}")
        count -= 1