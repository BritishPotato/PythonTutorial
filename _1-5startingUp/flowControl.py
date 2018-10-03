spam = 0
while spam < 5:
    print("Hello world.")
    spam += 1

while True:
    print("Please type your name.")
    name = input()
    if name == "your name":
        break
print("Fuck off <3")

# use ctrl-c to immediately stop program

while True:
    print("Who are you?")
    name = input()
    if name != "Denizhan":
        continue
    print("Hello Denizhan. Give password.")
    password = input()
    if password == "gay":
        break
print("Access granted. You may now use the nuclear codes.")
