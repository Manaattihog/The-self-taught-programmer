#1n. Print each item in the following list:
#  ["The Walking dead", "Sopranos", "Entourage", #Syke"]

shows = ["The Walking dead", "Sopranos", "Entourage", "Syke"]

for show in shows:
    print(show)

#2. Print all the numbers from 25 to 50.

for i in range(25, 51):
    print(i)
    i =+ i

#3. Print each item of the list of first challenge and their indexes

for i, show in enumerate(shows):
    print(i, shows[i])

#4. Write a program with an infinite loop (with an option to type q to quit)
# and a list of numbers. Each time trough the loop ask the user
# to guess a number on the list and tell them wether or not they
# guessed correctly

numbers = ["1", "4", "7", "3", "8"]
inp = 0
print("Type \"q\" to quit")
while (inp != "q"):
    inp = input("Guess a number between 0-10: ")
    if inp in numbers:
        print("Guessed right!")
    else:
        print("try again")

#5. Multiply all the numbers in the list [8, 19, 148, 4]
# with all the numbers in the list [9, 1, 33, 83] and append each result in
# the third list

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)
