import requests
import random
# import similar_text

response = requests.get('https://random-data-api.com/api/v2/appliances').json()

# print(response)


def consultant():
  print(
    "'Hello, I am here to help you design the most wonderful beauteous living space, as I heard you are remodeling your home and wish to experience a room unlike any other.'"
  )
  print("")
  userFurniture = askFurniture([])
  if (len(userFurniture) == 0):
    print("So dissapointing that I could be of no help to you")
  else:
    message = "'Okay, I think we have pulled together a lovely array of appropriately astonishing appliances. You have "
    if (len(userFurniture) == 1):
      message += "a(n) " + userFurniture[0]["equipment"] + '. It may just be one thing, but it is the best thing you could have chosen.'
    elif( len(userFurniture) == 2):
      message += "a(n) " + userFurniture[0]["equipment"] + " and a(n) " + userFurniture[0]["equipment"] + "."
    else:
      for i in range(0, len(userFurniture) - 1):
        message += "a(n) " + userFurniture[i]["equipment"] + ", "
      message += "and finally a " + userFurniture[-1]["equipment"] + "."
    print(message)
  print("")
  print("")
  print("Do you have another home you need to furnish?")
  print("")
  print("1. 'Yes!!!'")
  print("2. 'No!!!!'")
  print("")
  print("Note: Please type in '1' or '2' to continue.")
  userChoice = askChoice(input())

  if (userChoice == 1):
    print("'Great! Let's get to it!''")
    print("")
    print("")
    print("")
    consultant()
  else:
    print("")
    print("")
    print("")
    print("Well, you know where to find me next time! Goodbye for now")


def askFurniture(userFurniture):
  possibleAppliance = requests.get(
    'https://random-data-api.com/api/v2/appliances').json()
  possibleAppliance["equipment"] = possibleAppliance["equipment"].casefold()
  appName = possibleAppliance["equipment"]
  message = ""
  message += random.choice([
    "Okay, I think that this might be the perfect fit. How do you feel about a %s?",
    "My friends at the office just told me about the miraculous %s, would you like one?",
    "We just got a fine fresh shipment of %s(s), and I think they would look so good in your room.",
    "I can only preach about how much you'll absolutely love a %s in your home. What do you say?",
    "My mother always swore by her %s. You should buy one, just to be safe.",
    "A house without a(n) %s is not yet a home. You won't regret adding this.",
    "A(n) %s. This item speaks for itself.",
    "Johnny just rang me on the phone and told me about this %s. This could be your once-in-a-lifetime chance to purchase one!",
    "You might have heard of this next item before. Its a(n) %s."
  ]) % appName
  print(message)
  print("")
  print("1. " + yesMessage())
  print("2. " + noMessage())
  print(
    "3. 'No, I think I'm actually done, my space has everything it needs now.''"
  )
  print("")
  print("Note: Please type in '1', '2', or '3' to continue.")
  userChoice = askChoice(input())

  if (userChoice == 1):
    print("'Great! Let's see what else I've got!'")
    print("")
    userFurniture.append(possibleAppliance)
    return askFurniture(userFurniture)
  elif (userChoice == 2):
    print("'Oh... Let's find something you'll like more.'")
    print("")
    return askFurniture(userFurniture)
  elif (userChoice == 3):
    return userFurniture
  else:
    print("")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("ERROR: Sorry, that response was invalid. Please do better next time.")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("")
    return askFurniture(userFurniture)
    
def yesMessage():
  return random.choice([
    "'Yes! I'd love to add that to my home!'",
    "'Wow!!! I've never seen something that I loved as much as this! I need one'",
    "'That is an offer I can't pass up!",
    "'I have always wanted one of those!'",
    "'I've oft dreamed of the days when I would have one of these in my humble abode.'",
    "'Adding this to my home will surely make my dreams come true'",
    "'I never realized exactly how much I needed one of these. You are correct.'"
  ])


def noMessage():
  return random.choice([
    "'No! But I'd love to add something else, what are my other options?'",
    "'I absolutely would not like to purchase that.'",
    "'No thank you, it is hideous.'",
    "'I already had one of those and did not like them.'",
    "'I just dont see that as a necessity.'", "'I would never buy that'",
    "'That is the last thing I would furnish my home with.'",
    "'Absolutely not...'"
  ])


def askChoice(userResponse):
  if userResponse.isdigit():
    return int(userResponse)
  else:
    return 0


consultant()