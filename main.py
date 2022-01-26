import choose as c
import time as t
cool = c.NewAdventure("Epic story","Info Crant")
(adname,admaker)  = cool.getInfo()

# Modify This to create choices
choices = ["Yes","No","Yes","No"]
#modify this for reactions in order
reactions = ["Ok. Meet you on the other side.","Well, do you have an idea then?","You jump up and hit them with a wrench. Luckily no one notices.","You continue on."]

e = "NotFinish"
current = 0
hap = 5
print("-----------DEMOGAME-----------")
introtext = ["The scene: The beggening of the end.","The aircraft hanger, where it all started.","@23 : 'I go in to the left, while you go right. Take out anyone near.'"]

# DEMO GAME START
c.scroll(introtext)
while e == "NotFinish":
  
  e = c.ChooseAndReact("@23: So, do you agree?","h",reactions[current],reactions[current+1],choices[current],choices[current+1])
  
if e == "1":
  print("You begin to make your way throgh.")
elif e == "2":
  print("...")
  t.sleep(1)
  hap -= 2
  print("Didn't think so.")
t.sleep(0.5)
print("You begin to move.")
t.sleep(1)
print("A gaurd is in front of you.")
e = "NotFinish"
while e == "NotFinish":
  current = 2
  e = c.ChooseAndReact("Do you attack?","h",reactions[current],reactions[current+1],choices[current],choices[current+1])

print("There are two doors")
  