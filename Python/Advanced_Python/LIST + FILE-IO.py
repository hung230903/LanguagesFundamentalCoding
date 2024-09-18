user_input = int(input("Enter an interger: "))

with open("exercise.txt", "w") as file:
    for i in range(user_input):
        file.write(str(user_input - i) + "\n")

numbers = []
with open("exercise.txt", "r") as file:
    numbers = file.read().split("\n")
    numbers.pop()

for i in range(len(numbers)):
    print("Line " + str(i+1) + ": " + numbers[i])