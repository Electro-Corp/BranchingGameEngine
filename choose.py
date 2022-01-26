import os

class NewAdventure:
  def __init__(self,storyname,author):
    self.storyname = storyname
    self.author = author
    print("Welcome to ",storyname)
    print("Created by: ", author)
    print("Runnin on the ChooseYourOwnAdventure engine by Chinmay Tiwari")
  def getInfo(self):
    return(self.storyname,self.author)

def ChooseAndReact(init,choose,react1,react2,option1,option2):
  print("-----------------------")
  print(init)
  print("Choose(presskey):")
  print("1. ",option1)
  print("2.", option2)
  a = str(input("?"))
  if a == "1":
    print(react1)
    return("1")
  elif a == "2":
    print(react2)
    return("2")
  else:
    print("Option not avalible, please try again.")
    return("NotFinish")
  


def scroll(text):
  leng = len(text)
  e = 0
  for e in range(leng):
    print(text[e])
    a = input("...")
    