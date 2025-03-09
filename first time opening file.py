import csv
import os

#jostain itselle tuntemattomasta syystä
#ekaan polun osaan piti laittaa mukaan :\\ jotta toimii.
with open (os.path.join( "C:\\", "Users", "juuso", "Documents", "pythontest.csv"),"r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(".".join(row))
