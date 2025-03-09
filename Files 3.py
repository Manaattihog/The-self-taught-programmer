import os
import csv

lists = [["Top Gun", "Risky Business", "Minority report"],
         ["Titanic", "something", "Inception"], ["1 Movie", "2 Movie", "3 Movie"]]

with open(os.path.join("C:\\", "Users", "juuso", "Documents", "files3.csv"), "w") as g:
          w = csv.writer(g, delimiter=",")
          for lista in lists:
              i = 0
              for i in range(len(lists[i])):
                  w.writerow(lists[lista][i])
                  i += 1
              

#Muuten toimii, mutta täytyisi vaihtaa uusi rivi
#eipä toimikkaan
              
            
            
