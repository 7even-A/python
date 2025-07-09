import time

chatbot_name = input("Give your chatbot a name: ")
print(f"{chatbot_name} a name only a goofy would come up with. Honestly. Do better.")
uName = input("What yo name ")
request = input(f"Hey {uName}. How can I help you? ")

if (request == "Calculator"):
    FN = input("first int please ")
    SN = input("secont int please ")
    WO = input("What operation? (+, -, *, /, %)")

    if (WO=="+"):
        print(int(FN) + int(SN))

    elif (WO =="-"):
        print(int(FN) - int(SN))

    elif(WO =="*"):
        print(int(FN) * int(SN))

    elif (WO=="/"):
        print(int(FN) / int(SN))
    
    elif (WO =="%"):
        print(int(FN) % int(SN))

else:
    print("Error: I can't do that twinjamin")

time.sleep(2)
print("still right")

