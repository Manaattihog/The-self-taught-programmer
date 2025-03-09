#1. Make a list of your favourite musicians

fav_musicians = ["JVG", "Rekami", "Gettomasa"]
print(fav_musicians)
fav_musicians.append("Tohtori Getto")
fav_musicians.pop(0)
print(fav_musicians)

#2. Make a list of tuples, each tuple contains magnitude & lognitude
#of place you have visited

Suolahti = ("62°33′50N", "025°51′10E")
Madeira = ("32°22'17.99N", "-16°16'30.00W")

places_visited = [Suolahti]
places_visited.append(Madeira)
print(places_visited)

#3. Create a dictionary that includes three attributes of you
#for example: height, weight, eye color

jhk_attributes = {"Height":"178", "Weight": "78", "Eye color": "Blue"}
print(jhk_attributes)
height = jhk_attributes["Height"]
print(height)

#4. Create program that allows user to ask your height, weight or eye color.
#Use the dictionary made in the previous challenge.

question = "empty"
while question not in jhk_attributes:
    question = input("Do you want to know my Height, Weight or Eye color?")
answer = jhk_attributes[question]
print(answer)
print(jhk_attributes[question])

#5. Create a dictionary mapping your favourite musicians
#to a list of your favourite songs by them

rekamisongs = [1, 2, "kolmonen"]
jvgsongs = [4, 5, "kuus"]
gettosongs = [7, 8, "ysi"]

fav_music = {"Rekami": rekamisongs, "JVG": jvgsongs, "Gettomasa": gettosongs}
print(fav_music["Rekami"][1])
for i in range(len(rekamisongs)):
    print(fav_music["Rekami"][i])
