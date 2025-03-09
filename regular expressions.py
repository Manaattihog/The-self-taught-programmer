import re
import os

with open (os.path.join( "C:\\", "Users",
                         "juuso", "AppData", "Local", "Programs",
                         "Python", "Python313", "regularexp.txt"),"r+") as f:
    content = f.read()
    print(content)
    m = re.findall(".oo", content, re.IGNORECASE)
    print(m)


    for match in m:
        new_content = re.sub(match, m[0], content)
    print(new_content)

    f.seek(0)
    f.write(new_content)
    
#haku toimii, seuraavaksi pitäisi varmaan avata tiedosto kirjoitettavaksi
#ja muokata tehtävän mukaan.
