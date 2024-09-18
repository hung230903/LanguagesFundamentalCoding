#Write mode - "w": write to a new file 
with open("data.txt", "w") as file:
    file.write("lmao\n")
    file.write("lol\n")

#Append mode - "a": wirte to an existing file
with open("data.txt", "a") as file:
    file.write("lmfao\n")
    file.write("fuk\n")

#Reading mode - "r": read an existing file
with open("data.txt", "r") as file:
    data = file.read()
    print(data)
