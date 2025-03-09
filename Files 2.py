import os

with open(os.path.join("C:\\", "Users", "juuso", "Documents", "file2.txt"), "w") as f:
    answer = input("Whats your favourite color?")
    f.write(answer)
    


