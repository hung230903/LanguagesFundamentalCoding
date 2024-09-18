colors = ["red", "green", "blue", "yellow"]
print(colors)

#remove from list
colors.remove("green")

if "lmao" in colors:
    colors.remove("lmao")
else:
    print("not exist ")

print(colors)

#remove last element
colors.pop()
print(colors)

#add 
colors.insert(0, "black")
print(colors)

#find index of the first "red"
colors = ["black", "purple", "red", "blue", "red"]
try:
    print(colors.index("red"))
except:
    print("not exist")

#find index of "red" in list
red_index = []
for i in range(len(colors)):
    if colors[i] == "red":
        red_index.append(i)

print(red_index)

#find number of occurance of "red"
print(colors.count("red"))

a = [9,5,4,3,8,2]
a.sort()
print(a)

# change the element
a[0] = "djtnhauxaorau"
print(a)