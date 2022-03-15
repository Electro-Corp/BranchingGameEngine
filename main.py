# import choose as c
# import time as t
# import battle as b
x = 0
testing = ["The scene: The beggening of the end.","The aircraft hanger, where it all started.","@23 : 'I go in to the left, while you go right. Take out anyone near.'"]
while x < 101:
  print('\r',"Loading.. [",x,"]",end='')
  x += 1
  import choose as c
  import time as t
  import battle as b
  c.checkItem(testing)
  t.sleep(0.05)
print("         ")

cool = c.NewAdventure("Epic story","Info Crant")
(adname,admaker)  = cool.getInfo()

# Modify This to create choices
choices = ["Yes","No","Yes","No","Left","Right"]
#modify this for reactions in order
reactions = ["Ok. Meet you on the other side.","Well, do you have an idea then?","You jump up and hit them with a wrench. Luckily no one notices.","You continue on.","You go throgh the left door.","You go throgh the right door.",""]

e = "NotFinish"
current = 0
hap = 5
print("-----------DEMOGAME-----------")
introtext = ["The scene: The beggening of the end.","The aircraft hanger, where it all started.","@23 : 'I go in to the left, while you go right. Take out anyone near.'"]

# DEMO GAME START(this is the code for the game)
c.scroll(introtext)
print("----------------------")

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
t.sleep(1)
print("There are two doors")
t.sleep(1)
e = "NotFinish"
while e == "NotFinish":
  current = 4
  e = c.ChooseAndReact("Which door do you use?","h",reactions[current],reactions[current+1],choices[current],choices[current+1])  
if e == "1":
  door = "left"
elif e == "2":
  door = "right"

if door == "left":
  print("The hallway appears to lead to a control room.")
elif door == "right":
  print("The hallway appears to lead to a lab.")
else:
  print("Critcal Exception: Door not found. Exiting")
  exit()
t.sleep(2)
print("As you move.. you see a gaurd moving up.")
t.sleep(1)
b.battle(50,1,"Gaurd",100,0)
print("You move on.")
print("")
