import random

money = 100

#coin_flip game


flip = random.randint(1, 2)

def coin_flip(guess, bet):

 print("Lets play heads or tails game!\n")
 
 if bet <= 0:
    print("Your bet must be greater than zero. Please try again!\n")

 elif bet > money:
    print("You don't have that much money. Please try again!\n")
    

 elif guess.lower() == "heads" and flip == 1:
  print("You won " + str(bet) + " dollars! You have " + str(money + bet) + " dollars money!\n")
  return bet

 elif guess.lower() == "heads" and flip == 2:
  print("You lost " + str(bet) + " dollars! You have " + str(money - bet) + " dollars money!\n")
  return -bet

 elif guess.lower() == "tails" and flip == 1:
  print("You lost " + str(bet) + " dollars! You have " + str(money - bet) + " dollars money!\n")
  return -bet

 elif guess.lower() == "tails" and flip == 2:
    print("You won " + str(bet) + " dollars! You have " + str(money + bet) + " dollars money!\n")
    return bet





# cho-han game

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice_total = dice1 + dice2


def dice_roll(guess, bet):
  print("Lets play Cho-Han game!\n")

  if bet <= 0:
    print("Your bet must be greater than zero. Please try again!\n")

  elif bet > money:
    print("You don't have that much money. Please try again!\n") 

  elif guess.lower() == "even" and dice_total % 2 == 0:
    print("You won " + str(bet) + " dollars! You have " + str(money + bet) + " dollars money!\n")
    return bet

  elif guess.lower() == "even" and dice_total % 2 == 1:
    print("You lost " + str(bet) + " dollars! You have " + str(money - bet) + " dollars money!\n")
    return -bet

  elif guess.lower() == "odd" and dice_total % 2 == 1:
    print("You won " + str(bet) + " dollars! You have " + str(money + bet) + " dollars money!\n")
    return bet

  elif guess.lower() == "odd" and dice_total % 2 == 0:
    print("You lost " + str(bet) + " dollars! You have " + str(money - bet) + " dollars money!\n")
    return -bet






  # card game


player_card = random.randint(1, 10)
opponent_card= random.randint(1, 10)

def card_draw(bet):
    print("Lets play Card game!\n")

    if bet <= 0:
     print("Your bet must be greater than zero. Please try again!\n")

    elif bet > money:
     print("You don't have that much money. Please try again!\n") 

    elif player_card > opponent_card:
      print("Your card is higher!. You won " + str(bet) + " dollars! You have " + str(money + bet) + " dollars money!\n")
      return bet


    elif player_card < opponent_card:
      print("The opponent card is higher! You lost " + str(bet) + " dollars! You have " + str(money - bet) + " dollars money!\n")
      return -bet

    else:
     print("It's in tie! You doesn’t win or lose any money!\n")
     return 0




# Roulette game




def roulette_game(guess, bet):

  print("Lets play Roulette game!")

  if bet <= 0:
     print("Your bet must be greater than zero. Please try again!\n")

  elif bet > money:
     print("You don't have that much money. Please try again!\n") 
  else:
    number = random.randint(0,37)
    if number == 0:
       number = "0"
    elif number == 37:
       number = "00"
     
# Check even/odd results

    if isinstance(guess,str):
  
      if guess.lower() == "even" and number % 2 == 0:
       print ("You won " + str(bet) + " dollars! You have " + str(money + bet) +  " dollars money!\n")
       return bet
  
      elif guess.lower() == "even" and number % 2 == 1:
       print ("You lost " + str(bet) + " dollars! You have " + str(money - bet) +  " dollars money!\n")
       return -bet

      elif guess.lower() == "odd" and number % 2 == 1:
       print ("You won " + str(bet) + " dollars! You have " + str(money + bet) +  " dollars money!\n")
       return bet

      elif guess.lower() == "odd" and number % 2 == 0:
       print ("You lost " + str(bet) + " dollars! You have " + str(money - bet) +  " dollars money!\n")
       return -bet

      elif guess == "00" and number == "00":
       print("You win big! You have " + str(money + (bet * 35)) + " dollars money!\n")
       return bet * 35

      else:
       print ("You lost " + str(bet) + " dollars! You have " + str(money - bet) +  " dollars money!\n")
       return -bet


# Check number results


    elif guess == 0 and number == 0:
      print("You win big! You have " + str(money + (bet * 35)) + " dollars money!\n")
      return bet * 35

    elif guess == number:
     print("You win big! You have " + str(money + (bet * 35)) + " dollars money!\n")
     return bet * 35

    else:
     print ("You lost " + str(bet) + " dollars! You have " + str(money - bet) +  " dollars money!\n")
    return -bet




#Call your game of chance functions here

money += coin_flip("tails",89)
money += coin_flip("Heads",10)
money += dice_roll("odd",65)
money += card_draw(85)
money += roulette_game("0", 100)
money += roulette_game("even", 50)
money += roulette_game(12, 45)


print("You got " + str(money) + " dollars money from the game!\n")



















