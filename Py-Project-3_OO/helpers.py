import random
def printFlourish():
  print("\n ---~-~--*^*^*^*^*^--~-~--- \n")


def questionErrorMesage():
  print("Sorry, your answer was not valid. Please try again.")


def chooseFromList(list, message):
  options = random.sample(list, 2)
  print(message % (options[0], options[1], options[0], options[1]))
  chosenOption = input()

  if chosenOption in options:
    print("Great choice! Thanks for sharing!")
    return chosenOption
  else:
    print("Sorry, your answer was not valid. Please try again.")
    return chooseFromList(list, message)

def getUserNumber(max):
  userNumber = input()
  if userNumber.isdigit() == False:
    questionErrorMesage()
    return getUserNumber(max)
  else:
    userNumber = int(userNumber)
    if userNumber <= 0 or userNumber > max or isinstance(userNumber, int) == False :
      questionErrorMesage()
      return getUserNumber(max)
    else:
      return int(userNumber)