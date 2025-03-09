#1. Print everu character of string #camus#

x = "camus"
for i in range(len(x)):
    print(x[i])

#2. Write a program that takes two strings as an input and puts them
#in to a string #yesterday i wrote "first response". I sent it to "2. resp"

original_str = "Yesterday i wrote . I sent it to "
first_part = original_str[0:18]
second_part = original_str[18:]
first_resp = input("first responce: ")
second_resp = input("second responce: ")
original_str = first_part + first_resp + second_part + second_resp
print(original_str)

#3. Use the method to make the string "aldous Huxley was born in 1894."
#grammatically correct by capitalising the first letter in the sentence

sentence = "aldous Huxley was born in 1894."
print(sentence)
sentence = sentence.capitalize()
print(sentence)

#4. Take the string "Where now? Who now? When now?" and call a method that
#returns list that looks like ["Where now?", "Who now?", "When now?"]

sentence2 = "Where now? Who now? When now?"
print(sentence2)
sentence2 = sentence2.split("?")
print(sentence2)

#5. Take the list ["The", "fox", "jumped", "over", "the" "fence", "."]
#and turn it in to grammatically correct string. There should be space between
#every word exept between fence and dot.

alist = ["The", "fox", "jumped", "over", "the", "fence", "."]
astring = " ".join(alist)
astring = astring.replace(" .", ".")
print(alist)
print(astring)

#6. Replace every intance of s in "A screaming comes across the sky"
#with a dollar sign

scream = "A screaming comes across the sky"
scream = scream.replace("s", "$")
print(scream)

#7. Use method to find the first index of the character "m" in the string
#"Hemingway"

hemmari = "Hemingway"
firstind = hemmari.index("m")
print(firstind)

#8. find dialogue of your favourite book (with quotes) and turn it
#in to a string

dialogue = "Hän sanoi: \"mene nukkumaan\""
print(dialogue)

#9. create a string "three three three" using concatenation and then
# again using multiplication

three = "three "
concat = three + three + three
print(concat)
multipl = three * 3
print(multipl)

#10. Slice the string "it was a bright cold day in April, and the clocks
# were striking thirteen." to only include characters before the comma.

bright = """it was a bright cold day in April, and the clocks
            were striking thirteen."""
#comma = bright.index(",")
#bright = bright[0:comma]
bright = bright[0:bright.index(",")]
print(bright)







