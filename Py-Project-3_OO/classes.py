import random

class Clothing:
  def __init__(self,type,subtype=False,color=False):
    self.type = type
    self.subtype = subtype
    self.color = color
    self.__favoriteColor = "None"
  
  def setColor(self, color):
    self.color = color

  def getColor(self):
    return self.color

  def setSubtype(self, subtype):
    self.subtype = subtype

  def getSubtype(self):
    return self.subtype

  def getType(self):
    return self.type

  def randomizeClothing(self):
    print("randomizing clothes")
    possibleColors = ["red","green","blue","orange","purple","indigo","violet","cyan","magenta","pink","pale blue", "white","lavender","rainbow","silver","gold","copper","goldenrod","khaki","pearl","bronze","coral","muave","salmon","lime","plum","black","grey"]
    possibleTops = ["T-shirt","blouse","sweater","blazer","halter top","coat","poncho","sweater vest","vest"]
    possibleBottoms = ["pants","jeans","skirt","hoop skirt","tights","leggings","cargo pants","pencil skirt","skort"]
    possibleShoes = ["sneakers","high heels","rainboots","clogs","crocs","flip flops","socks","slippers","dress shoes"]
    possibleHats = ["beanie","crown","bonnet","headband","top hat","balaclava"]
    newColor = random.choice(possibleColors)
    print(newColor)
    newSubtype =""
    if (self.getType() == "top"):
      newSubtype = random.choice(possibleTops)
    elif self.getType() == "bottom":
      newSubtype = random.choice(possibleBottoms)
    elif self.getType() == "hat":
      newSubtype = random.choice(possibleHats)
    elif self.getType() == "shoes":
      newSubtype = random.choice(possibleShoes)
    self.setSubtype(newSubtype)
    self.setColor(newColor)

class Character:
  def __init__(self):
    self.name = ""
    #this is a secret and is only set once the program asks for the favColor
    self.__favColor = ""
    self.money = 100
    self.hat = Clothing("hat")
    self.top = Clothing("top")
    self.bottom = Clothing("bottom")
    self.shoes = Clothing("shoes")
    self.age = 0

  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name

  def setAge(self, age):
    self.age = age

  def getAge(self):
    return self.age

  def changeTop(self, newTop):
    self.top = newTop

  def changeBottom(self, newBottom):
    self.bottom = newBottom

  def changeHat(self, newHat):
    self.shoes = newHat

  def changeShoes(self, newShoes):
    self.shoes = newShoes

  def setFavColor(self, color):
    self.__favColor = color

  def setTopColor(self, color):
    self.top.setColor(color)

  def setBottomColor(self, color):
    self.bottom.setColor(color)

  def setShoesColor(self, color):
    self.shoes.setColor(color)

  def setHatColor(self, color):
    self.hat.setColor(color)

  def setTopSubtype(self, subtype):
    self.top.setSubtype(subtype)

  def setBottomSubtype(self, subtype):
    self.bottom.setSubtype(subtype)

  def setShoesSubtype(self, subtype):
    self.shoes.setSubtype(subtype)

  def setHatSubtype(self, subtype):
    self.hat.setSubtype(subtype)

  def removeShoes(self):
    self.shoes = False

  def removeHat(self):
    self.hat = False

  def noHat(self):
    if self.hat == False:
      return True
    else:
      return False
    
  def noShoes(self):
    if self.shoes == False:
      return True
    else:
      return False
    
  def needsShoes(self):
    if self.shoes == False:
      return False
    elif self.shoes.getSubtype() == False:
      return True
    
  def needsBottoms(self):
    if self.bottom == False:
      return False
    elif self.bottom.getSubtype() == False:
      return True

  def needsTop(self):
    if self.top == False:
      return False
    elif self.top.getSubtype() == False:
      return True

  def needsHat(self):
    if self.hat == False:
      return False
    elif self.hat.getSubtype() == False:
      return True

  def hasTop(self):
    return(self.top != False)

  def hasBottom(self):
    return(self.bottom != False)

  def hasShoes(self):
    return(self.shoes != False)

  def hasHat(self):
    return(self.hat != False)

  def needsClothes(self):
    return self.needsHat() and self.needsTop() and self.needsBottoms() and self.needsShoes()

  def describeTop(self):
    if self.hasTop():
      return(self.top.getColor() +" " +self.top.getSubtype())

  def describeHat(self):
    if self.hasHat():
      return(self.hat.getColor() +" "+ self.hat.getSubtype())

  def describeBottom(self):
    if self.hasBottom():
      return(self.bottom.getColor() +" " +self.bottom.getSubtype())

  def describeShoes(self):
    if self.hasShoes():
      return(self.shoes.getColor() +" " +self.shoes.getSubtype())

  def addClothing(self, clothing):
    if (clothing.getType() == "top"):
      self.changeTop(clothing)
    elif clothing.getType() == "bottom":
      self.changeBottom(clothing)
    elif clothing.getType() == "hat":
      self.changeHat(clothing)
    elif clothing.getType() == "shoes":
      self.changeShoes(clothing)