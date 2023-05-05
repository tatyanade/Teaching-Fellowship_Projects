from classes import *
from helpers import *
import random

listOfColors = [
  'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'white',
  'black', 'brown', 'grey', 'turquoise', 'magenta', 'cyan','lime','auburn','beige']

userCharacter = Character()

def askAge(age):
  if age.isdigit():
    age = int(age)
    userCharacter.setAge(age)
    if(userCharacter.getAge() <= 4):
      print("Aren't you a bit yound to be typing in a console?")
    elif(userCharacter.getAge() > 100):
      print("Wow! You are uncommonly old, very impressive!")
  else:
    questionErrorMesage()
    askAge(input())

  
  
  
def getToKnowUser():
  print("Hello! Welcome. Before we get started, what is your name?")
  userCharacter.setName(input())

  print("Hello %s! How old are you?" % userCharacter.getName())
  askAge( input())



  print( "Thanks for telling me about yourself! To finish building your digital persona, I am going to ask you some questions about what you like to wear, and based off of your answers, I will generate the perfect outfit for you!")

  printFlourish()
  

def outfitQuiz():
  print("What is your favorite color?")
  favColor = input()
  userCharacter.setFavColor(favColor)
  print("What a good color! I think %s is really nice." % favColor)
  userCharacter.setTopColor(favColor)
  userCharacter.setFavColor(favColor)
  askOutfitColors(favColor)

  personalityClothingTest()

  revealOutfit()
  

def askOutfitColors(favColor):
  print("Do you like wearing a monochromatic outfit? please answer with a 'yes' or 'no'")
  likesMonochrome = input()
  if(likesMonochrome == 'yes'):
    userCharacter.setBottomColor(favColor)
    userCharacter.setHatColor(favColor)
    userCharacter.setShoesColor(favColor)
  elif(likesMonochrome == 'no'):
    bottomColor = chooseFromList(listOfColors, "If you had to choose between %s or %s, which color would you prefer? Please type in '%s' or '%s' to proceed.")
    userCharacter.setBottomColor(bottomColor)

    print("Do you like it when your shoes and shirt match? please type in 'yes' or 'no'")
    if(input() == 'yes'):
      userCharacter.setShoesColor(favColor)
    else:
      print("Okay, this next descision is gonna be even harder.")
      shoesColor = chooseFromList(listOfColors, "If you could only see one color for th rest of your life, would you pick %s or %s? Please type in '%s' or '%s' to proceed.")
      userCharacter.setShoesColor(shoesColor)

    print("Alright, this is the final color question.")
    hatColor = chooseFromList(listOfColors, "Lets say someone picks you a bouquet of flowers. Do you wish the flowers where %s or %s? Please type in '%s' or '%s' to proceed.")
    userCharacter.setHatColor(hatColor)
  else:
    questionErrorMesage()
    askOutfitColors(favColor)

def personalityClothingTest():
  printFlourish()
  print("Now I'm going to ask you a few personailty questions")
  printFlourish()
  
  print("It's friday night and everyone is having a night out on the town! How do you want to spend your evening?")
  print("1. I like to go swimming in the ocean, lake, or pond. I can never get enough of the water!")
  print("2. I like to go out and eat a nice dinner with my friends at a restaurant.")
  print("3. I am staying at home and cozying up in front of the fireplace with a good book. I love reading and am always cold, so the fire is a necessity.")
  print("4. I've already packed my bags because I'm flying out to switzerland to start chef school tomorrow!")
  print("5. How do I want to spend my evening? I don't have too many choices because I already fell asleep...")
  print("please type '1', '2', '3', '4', or '5' to proceed")
  userChoice = getUserNumber(5)

  if (userChoice == 1):
    userCharacter.setBottomSubtype("mermaid tale")
    userCharacter.removeShoes()
  elif (userChoice == 2):
    if random.choice([1,2]) == 1:
      userCharacter.setBottomSubtype("fancy pants")
    else:
      userCharacter.setTopSubtype("fancy shirt")
  elif (userChoice == 3):
    if random.choice([1,2]) == 1:
      userCharacter.setBottomSubtype("pajama pants")
    else:
      userCharacter.setTopSubtype("cozy sweater")
  elif (userChoice == 4):
    userCharacter.setHatSubtype("chef's hat")
  else:
    userCharacter.setHatSubtype("sleeping cap")
    if random.choice([1,2]) == 1:
      userCharacter.setTopSubtype("pajama shirt")
    if random.choice([1,2]) == 1:
      userCharacter.setTopSubtype("pajama pants")

      #options are now 
      #1) shoes pants 
      #2)       pants 
      #3)             shirt 
      #4)                   hat 
      #5)             shirt hat
      #6)       pants shirt hat
      #7)       pants       hat
    
      #If they still need shoes we are going to find shoes for them

  printFlourish()
  
  if( userCharacter.needsShoes()):
    print("You just woke and its tuesday afternoon! You are late for work :( How are you getting there? ")
    print("1. I'm going to glide to work - I have to do everthing in my power to right this wrong")
    print("2. Hmm... is there any way I can bounce?")
    print("3. I'm running. I'm a runner, so I'll run there. I run anyways but to work? on the day I'm late? I'm gonna sprint!!")
    print("please type '1', '2', or '3' to proceed")
    userChoice = getUserNumber(3)

    if(userChoice == 1):
      userCharacter.setShoesSubtype("roller blades")
    elif(userChoice == 2):
      userCharacter.setShoesSubtype("moon shoes")
    elif(userChoice == 3):
      userCharacter.setShoesSubtype("running shoes")
    
  #options are now 
  #1) shoes pants 
  #2) shoes       shirt 
  #3) shoes             hat 
  #4) shoes       shirt hat
  #5) shoes pants shirt hat
  #6) shoes pants       hat

  
  #this exits out of the loop early if all the clothing is already defined
  if( userCharacter.needsClothes() == False):
    return
    
  printFlourish()
  print("Which of these do you prefer?")
  print("1. Sports!")
  print("2. Lounging in the Prairie!")
  print("3. Dressing up for fancy fancy things!")
  if(userCharacter.needsHat()):
    print("4. Keeping a clear head.")
    userChoice = getUserNumber(4)
  else:
    userChoice = getUserNumber(3)

  
  if(userChoice == 1):
    if userCharacter.needsHat():
      userCharacter.setHatSubtype("baseball cap")
    elif userCharacter.needsBottoms():
      userCharacter.setBottomSubtype("basketball shorts")
    elif userCharacter.needsTop():
      userCharacter.setTopSubtype("soccer jersey")

  elif(userChoice == 2):
    if userCharacter.needsBottoms():
      userCharacter.setBottomSubtype("summer pants")
    elif userCharacter.needsTop():
      userCharacter.setTopSubtype("linnen shirt")
    elif userCharacter.needsHat():
      userCharacter.setHatSubtype("bonnet")
                                  
  elif(userChoice == 3):
    if userCharacter.needsTop():
      userCharacter.setTopSubtype("extremely fancy shirt")
    elif userCharacter.needsHat():
      userCharacter.setHatSubtype("extremely fancy hat")
    elif userCharacter.needsBottoms():
      userCharacter.setBottomSubtype("extremely fancy pants")      
  elif(userChoice == 4):
    userCharacter.removeHat()

  # #options now
  # #1) shoes pants shirt
  # #2) shoes pants       hat
  # #3) shoes pants shirt  
  # #4) shoes       shirt hat 
  # #5) shoes pants shirt hat

  printFlourish()

  print("Okay! just a couple more questions:")
  if(userCharacter.needsBottoms()):
    print("Do you bike?")
    print("1. yes")
    print("2. no")
    userChoice = getUserNumber(2)

    if userChoice == 1:
      userCharacter.setBottomSubtype("biker shorts")
    else:
      userCharacter.setBottomSubtype(random.choice(["jeans","capris","floral pants","skinny jeans","cargo shorts"]))
  
  # options now
  #1) shoes pants shirt
  #2) shoes pants       hat
  #3) shoes pants shirt  
  #4) shoes pants shirt hat 
  #5) shoes pants shirt hat

  printFlourish()

  if(userCharacter.needsTop()):
    print("What is your style")
    print("1. cool, casual")
    print("2. fancy, exotic, look at me!")
    print("3. businesswear")

    userChoice = getUserNumber(3)

    if userChoice == 1:
      userCharacter.setTopSubtype(random.choice(["t-shirt","sweater","long-sleeved shirt"]))
    elif userChoice == 2:
      userCharacter.setTopSubtype(random.choice(["clown shirt","magical blouse","sparkling electronic remote controlled sweater"]))
    elif userChoice == 3:
      userCharacter.setTopSubtype(random.choice(["button up","suit jacket with a tie","formal blouse"]))

  # options now
  # 1) shoes pants shirt
  # 2) shoes pants shirt hat

  printFlourish()


  if(userCharacter.needsHat() ):
    print("Do you like hats?")
    print("1. Of course")
    print("2. No...")

    userChoice = getUserNumber(2)
    if userChoice == 1:
      userCharacter.setHatSubtype(random.choice(["bowler hat","sun hat","crown","top hat"]))
    elif userChoice == 2:
      userCharacter.removeHat()

  printFlourish()

  # options now
  # 1) shoes pants shirt hat

def revealOutfit():
  print("Okay %s, thanks so much for indulging me by answering all my questions about you!" % userCharacter.getName())
  printFlourish()
  print("Okay I think I have figured out the perfect outfit for you.")
  printFlourish()
  if( userCharacter.hasHat()):
    hatDescription =userCharacter.describeHat()
    print("On your head you would look delightful with a beautiful %s!" % hatDescription)
  if (userCharacter.hasShoes()):
    shoesDescription = userCharacter.describeShoes()
    print("And on your feet, you are wearing only the finest %s." %shoesDescription)
  if (userCharacter.hasTop()):
    topDescrption = userCharacter.describeTop()
    print("You also have on a(n) %s." % topDescrption)
  if(userCharacter.hasTop()):
    bottomDescription = userCharacter.describeBottom()
    print("The finishing touch is that you are wearing your %s, this look is so elegant!" % bottomDescription)
  print("Wow, you look so beautiful! You are so special!")

  printFlourish()

  # print("Thank you so much for letting me help you! I hope you have enjoyed this as much as I have")

  offerToChangeUpOutfit()
  
def offerToChangeUpOutfit():
  printFlourish()
  print("Do you like your outfit? Let me know, I can change it up a bit if you like...")
  print("")
  print("Do you want to switch it up a little?")
  print("1. Yes! Give me something a little different")
  print("2. No! It's perfect!")
  
  userChoice = getUserNumber(2)
  if userChoice == 1:
    printFlourish()
    print("Okay I'm switching something out, I think you will like this a lot better. Yes, this is much more stylish.")
    print("...")
    # newClothingType = 
    newClothingItem = Clothing(random.choice(["top","bottom","hat","shoes"]))
    newClothingItem.randomizeClothing()
    userCharacter.addClothing(newClothingItem)
    revealOutfit()
  elif userChoice == 2:
    printFlourish()
    print("Wow! I'm glad you like it as much as I do!!! Thanks so much for letting me style you, I think you look so swell!")


getToKnowUser()
outfitQuiz()  