from english_words import get_english_words_set as ews
import random as r
from colorama import Back, Fore
from tabulate import tabulate as t
import time

won = 0

keyboard = '''Q W E R T Y U I O P
 A S D F G H J K L
  Z X C V B N M'''

nums = '1  2  3  4  5  6  7  8  9  0'


wordss = ews(['web2'])
twow = []
for x in wordss:
  if len(x) == 2 and x.isalpha():
    twow.append(x.upper())
threew = []
for x in wordss:
  if len(x) == 3 and x.isalpha():
    threew.append(x.upper())
fourw = []
for x in wordss:
  if len(x) == 4 and x.isalpha():
    fourw.append(x.upper())
fivew = []
for x in wordss:
  if len(x) == 5 and x.isalpha():
    fivew.append(x.upper())
sixw = []
for x in wordss:
  if len(x) == 6 and x.isalpha():
    sixw.append(x.upper())
sevenw = []
for x in wordss:
  if len(x) == 7 and x.isalpha():
    sevenw.append(x.upper())
eightw = []
for x in wordss:
  if len(x) == 8 and x.isalpha():
    eightw.append(x.upper())
ninew = []
for x in wordss:
  if len(x) == 9 and x.isalpha():
    ninew.append(x.upper())
tenw = []
for x in wordss:
  if len(x) == 10 and x.isalpha():
    tenw.append(x.upper())


def twoword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(twow)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(twow)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in twow:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)
          

        
  else:

    
    gword = input("Enter a 2-letter word (case-insensitive): ").upper()
    while len(gword) != 2 or not (gword.isalpha()) or gword not in twow:
      gword = input("Enter a 2-letter word: ").upper()
  
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 2-letter word: ").upper()
      while len(gword) != 2 or not (gword.isalpha()) or gword not in twow:
        gword = input("Enter a 2-letter word: ").upper()
  return [green, yellow, none, tries]


def threeword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(threew)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(threew)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in threew:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)

  else:
    gword = input("Enter a 3-letter word (case-insensitive): ").upper()
    while len(gword) != 3 or not (gword.isalpha()) or gword not in threew:
      gword = input("Enter a 3-letter word: ").upper()
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 3):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 3-letter word: ").upper()
      while len(gword) != 3 or not (gword.isalpha()) or gword not in threew:
        gword = input("Enter a 3-letter word: ").upper()
  return [green, yellow, none, tries]


def fourword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(fourw)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(fourw)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in fourw:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)
  else:
    gword = input("Enter a 4-letter word (case-insensitive): ").upper()
    while len(gword) != 4 or not (gword.isalpha()) or gword not in fourw:
      gword = input("Enter a 4-letter word: ").upper()
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 4):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 4-letter word: ").upper()
      while len(gword) != 4 or not (gword.isalpha()) or gword not in fourw:
        gword = input("Enter a 4-letter word: ").upper()
  return [green, yellow, none, tries]


def fiveword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(fivew)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))

  if bot == 1:
    gword = r.choice(fivew)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in fivew:
        ls = 0
        count = 1
        for y in x:
          if y in gword:
            ls +=1
          if ls>count:
            plaus.append(x)
      gword=r.choice(plaus)
  else:
    gword = input("Enter a 5-letter word (case-insensitive): ").upper()
    while len(gword) != 5 or not (gword.isalpha()) or gword not in fivew:
      gword = input("Enter a 5-letter word: ").upper()
  
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 5):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 5-letter word: ").upper()
      while len(gword) != 5 or not (gword.isalpha()) or gword not in fivew:
        gword = input("Enter a 5-letter word: ").upper()
  return [green, yellow, none, tries]


def sixword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(sixw)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(sixw)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in sixw:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)
  else:
    gword = input("Enter a 6-letter word (case-insensitive): ").upper()
    while len(gword) != 6 or not (gword.isalpha()) or gword not in sixw:
      gword = input("Enter a 6-letter word: ").upper()
  
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 6):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 6-letter word: ").upper()
      while len(gword) != 6 or not (gword.isalpha()) or gword not in sixw:
        gword = input("Enter a 6-letter word: ").upper()
  return [green, yellow, none, tries]


def sevenword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(sevenw)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(sevenw)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in sevenw:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)
  else:
    gword = input("Enter a 7-letter word (case-insensitive): ").upper()
    while len(gword) != 7 or not (gword.isalpha()) or gword not in sevenw:
      gword = input("Enter a 7-letter word: ").upper()
  
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 7):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 7-letter word: ").upper()
      while len(gword) != 7 or not (gword.isalpha()) or gword not in sevenw:
        gword = input("Enter a 7-letter word: ").upper()
  return [green, yellow, none, tries]


def eightword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(eightw)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(eightw)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in eightw:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)
  else:
    gword = input("Enter a 8-letter word (case-insensitive): ").upper()
    while len(gword) != 8 or not (gword.isalpha()) or gword not in eightw:
      gword = input("Enter a 8-letter word: ").upper()
  
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 8):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 8-letter word: ").upper()
      while len(gword) != 8 or not (gword.isalpha()) or gword not in eightw:
        gword = input("Enter a 8-letter word: ").upper()
  return [green, yellow, none, tries]


def nineword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(ninew)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(ninew)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in ninew:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)
  else:
    gword = input("Enter a 9-letter word (case-insensitive): ").upper()
    while len(gword) != 9 or not (gword.isalpha()) or gword not in ninew:
      gword = input("Enter a 9-letter word: ").upper()
  
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 9):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 9-letter word: ").upper()
      while len(gword) != 9 or not (gword.isalpha()) or gword not in ninew:
        gword = input("Enter a 9-letter word: ").upper()
  return [green, yellow, none, tries]


def tenword(keyboard=keyboard, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0

  rword = r.choice(tenw)
  row = 1
  tries = 1

  rows = [[
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ], [
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
    '  ',
  ]]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(tenw)
    ls = 0
    plaus = []
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 2):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
          '''ls used for letter counter'''
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
          '''ls used for letter counter'''
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      for x in tenw:
        ls = 0
        for y in x:
          if y in gword:
            ls +=1
          if ls>1:
            plaus.append(x)
      gword=r.choice(plaus)
  else:
    gword = input("Enter a 10-letter word (case-insensitive): ").upper()
    while len(gword) != 10 or not (gword.isalpha()) or gword not in tenw:
      gword = input("Enter a 10-letter word: ").upper()
  
    while 1:
      gwords = list(gword)
      rwords = list(rword)
      for x in range(0, 10):
        gwords[x] += f"{x+1}"
        rwords[x] += f"{x+1}"
  
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.GREEN + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.GREEN + x[0].upper() + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(rword) and x not in rwords:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + Back.YELLOW + x[0].upper(
          ) + Back.BLACK + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.YELLOW + x[0].upper() + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0].upper() + Fore.WHITE
          keyboard = keyboard.replace(
            x[0].upper(),
            Fore.WHITE + Back.RED + x[0].upper() + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      print(keyboard)
      print()
      if gword.upper() == rword.upper():
        print(f"You got the word in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The word was {''.join(rword)}.")
        break
      gword = input("Enter a 10-letter word: ").upper()
      while len(gword) != 10 or not (gword.isalpha()) or gword not in tenw:
        gword = input("Enter a 10-letter word: ").upper()
  return [green, yellow, none, tries]


def numberwordle(length, nums=nums, bot=0, won=won):
  green = 0
  yellow = 0
  none = 0
  end = int("9" + ("9" * (int(length) - 1)))
  end += 1
  start = int("1" + ("0" * (int(length) - 1)))
  print(f"Number start from: {start}")
  print(f"And ends from: {end}")
  print(
    f"A number may have {length} digits, but if it's not in between those two numbers, it shall'n't be accepted, i.g., the supposed 5-digit number {('0'*(length-1))+'4'}."
  )
  numberw = r.choice(range(start, end))
  row = 1
  tries = 1

  rows = [[' '] * int(length), [' '] * int(length), [' '] * int(length),
          [' '] * int(length), [' '] * int(length), [' '] * int(length)]

  print(t(rows, tablefmt="fancy_grid"))
  if bot == 1:
    gword = r.choice(range(start, end))
    while 1:
      gword = str(gword)
      numberw = str(numberw)
      gwords = list(gword)
      rwords = list(numberw)
      rvals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      y = 0
      for x in rvals[:len(gword)]:
        gwords[y] += x
        rwords[y] += x
        y += 1
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(
            x)] = Fore.WHITE + Back.GREEN + x[0] + Back.BLACK + Fore.WHITE
          nums = nums.replace(
            x[0], Fore.WHITE + Back.GREEN + x[0] + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(numberw) and x not in rwords:
          rows[row - 1][gwords.index(
            x)] = Fore.WHITE + Back.YELLOW + x[0] + Back.BLACK + Fore.WHITE
          nums = nums.replace(
            x[0], Fore.WHITE + Back.YELLOW + x[0] + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0] + Fore.WHITE
          nums = nums.replace(
            x[0], Fore.WHITE + Back.RED + x[0] + Back.BLACK + Fore.WHITE)
          none += 1

      print(t(rows, tablefmt="fancy_grid"))
      time.sleep(1)
      #print(nums)
      print()
      if gword == numberw:
        print(f"It got the number in {tries} tries!")
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"It lost! The number was {''.join(numberw)}.")
        print("(if it lost sorry about that the bot is pretty badly programmed so)")
        break
      rnums = []
      rnum = 0
      rc = 0
      rnumss = []
      Max =0
      for x in gword:
        if x in numberw:
          rnums.append(x)
      for x in range(start,end):
        for y in rnums:
          if str(y) in str(x):
            rc +=1
          rnumss.append([x,rc])
      for x in rnumss:
        if x[-1]>Max:
          if gword == Max:
            continue
          else:
            Max = x[0]
      gword = Max
  else:
    gword = input(f"Enter a number of length {length}: ")
    while len(gword) != int(length) or not (
        gword.isnumeric()) or int(gword) not in range(start, end):
      gword = input(f"Enter a number of length {length}: ")

    while 1:
      gword = str(gword)
      numberw = str(numberw)
      gwords = list(gword)
      rwords = list(numberw)
      rvals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      y = 0
      for x in rvals[:len(gword)]:
        gwords[y] += x
        rwords[y] += x
        y += 1
      for x in gwords:
        if x in rwords:
          rows[row - 1][gwords.index(
            x)] = Fore.WHITE + Back.GREEN + x[0] + Back.BLACK + Fore.WHITE
          nums = nums.replace(
            x[0], Fore.WHITE + Back.GREEN + x[0] + Back.BLACK + Fore.WHITE)
          green += 1
        elif x[0] in list(numberw) and x not in rwords:
          rows[row - 1][gwords.index(
            x)] = Fore.WHITE + Back.YELLOW + x[0] + Back.BLACK + Fore.WHITE
          nums = nums.replace(
            x[0], Fore.WHITE + Back.YELLOW + x[0] + Back.BLACK + Fore.WHITE)
          yellow += 1
        else:
          rows[row - 1][gwords.index(x)] = Fore.WHITE + x[0] + Fore.WHITE
          nums = nums.replace(
            x[0], Fore.WHITE + Back.RED + x[0] + Back.BLACK + Fore.WHITE)
          none += 1
  
      print(t(rows, tablefmt="fancy_grid"))
      #print(nums)
      print()
      if gword == numberw:
        print(f"You got the number in {tries} tries!")
        won+=1
        break
      row += 1
      tries += 1
      if tries == 7:
        print(f"You lose! The number was {''.join(numberw)}.")
        break
      gword = input(f"Enter a number of length {length}: ")
      while len(gword) != int(length) or not (
          gword.isnumeric()) or int(gword) not in range(1, end):
        gword = input(f"Enter a number of length {length}: ")
  return [green, yellow, none, tries]


def vsmode(length, num, keyboard=keyboard, nums=nums, won=won):
  if num == "Y":
    print("alright you're up first my guy")
    play1 = numberwordle(length)
    print("alright now it's the bot's turn, let's see how it did")
    play2 = numberwordle(length, bot=1)
  elif length == 2:
    print("alright you're up first my guy")
    play1 = twoword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = twoword(bot=1)
  elif length == 3:
    print("alright you're up first my guy")
    play1 = threeword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = threeword(bot=1)
  elif length == 4:
    print("alright you're up first my guy")
    play1 = fourword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = fourword(bot=1)
  elif length == 5:
    print("alright you're up first my guy")
    play1 = fiveword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = fiveword(bot=1)
  elif length == 6:
    print("alright you're up first my guy")
    play1 = sixword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = sixword(bot=1)
  elif length == 7:
    print("alright you're up first my guy")
    play1 = sevenword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = sevenword(bot=1)
  elif length == 8:
    print("alright you're up first my guy")
    play1 = eightword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = eightword(bot=1)
  elif length == 9:
    print("alright you're up first my guy")
    play1 = nineword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = nineword(bot=1)
  elif length == 10:
    print("alright you're up first my guy")
    play1 = tenword()
    print("alright now it's the bot's turn, let's see how it did")
    play2 = tenword(bot=1)

  print("all right here are the results")
  print("\n Seeing who took the least amount of tries to finish the wordle...")
  if play1[-1] > play2[-1]:
    print(f"You won, with {play1[-1]} tries to guess their word!")
  elif play1[-1] < play2[-1]:
    print(f"The bot won with {play2[-1]} tries to guess their word!")
  else:
    print(
      "It was pretty much a tie. Both players had the same amount of tries.")
    print("\n Looking at how many letters got highlighted, however...")
    if play1 == play2:
      print(
        "It was a absolute tie! Both players got the same exact amount of letters highlighted!"
      )
      print(f"Green letters: {play1[0]}")
      print(f"Yellow letters: {play1[1]}")
      print(f"Not highlighted letters: {play1[2]}")
    elif play1[0] > play2[0]:
      print(f'''You won, having the most green letters.
      Green letters: {play1[0]}
      Yellow letters: {play1[1]}
      Not highlighted letters: {play1[2]}''')
    elif play1[0] < play2[0]:
      print(f'''The bot won, having the most green letters.
      Green letters: {play2[0]}
      Yellow letters: {play2[1]}
      Not highlighted letters: {play2[2]}''')
    elif play1[1] > play2[1]:
      print(f'''{play1[-1]} won, having the most yellow letters.
      Green letters: {play1[0]}
      Yellow letters: {play1[1]}
      Not highlighted letters: {play1[2]}''')
    elif play1[1] < play2[1]:
      print(f'''The bot won, having the most yellow letters.
      Green letters: {play2[0]}
      Yellow letters: {play2[1]}
      Not highlighted letters: {play2[2]}''')
    elif play1[2] < play2[2]:
      print(
        f'''You won, having the least amount of not-highlighted letters.
      Green letters: {play1[0]}
      Yellow letters: {play1[1]}
      Not highlighted letters: {play1[2]}''')
    else:
      print(
        f'''The bot won, having the least amount of not-highlighted letters.
      Green letters: {play2[0]}
      Yellow letters: {play2[1]}
      Not highlighted letters: {play2[2]}''')
  


def oomode(bots, num, length, player, keyboard=keyboard, nums=nums, won=won):
  if bots == "Y":
    print(f"leggo {player} you're up first")
    play1 = [vsmode(length, num), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [vsmode(length, num), player]

  elif num == "Y" and bots == 'n':
    print(f"leggo {player} you're up first")
    play1 = [numberwordle(length), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [numberwordle(length), player]

  elif length == 2:
    print(f"leggo {player} you're up first")
    play1 = [twoword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [twoword(), player]

  elif length == 3:
    print(f"leggo {player} you're up first")
    play1 = [threeword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [threeword(), player]

  elif length == 4:
    print(f"leggo {player} you're up first")
    play1 = [fourword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [fourword(), player]

  elif length == 5:
    print(f"leggo {player} you're up first")
    play1 = [fiveword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [fiveword(), player]

  elif length == 6:
    print(f"leggo {player} you're up first")
    play1 = [sixword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [sixword(), player]

  elif length == 7:
    print(f"leggo {player} you're up first")
    play1 = [sevenword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [sevenword(), player]

  elif length == 8:
    print(f"leggo {player} you're up first")
    play1 = [eightword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [eightword(), player]

  elif length == 9:
    print(f"leggo {player} you're up first")
    play1 = [nineword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [nineword(), player]

  elif length == 10:
    print(f"leggo {player} you're up first")
    play1 = [tenword(), player]
    if player == "Player One":
      player = players[-1]
    else:
      player = players[0]
    print(f"anyways leggo {player} you're next")
    play2 = [tenword(), player]

  print("\n Seeing who took the least amount of tries to finish the wordle...")
  if play1[0][3] > play2[0][3]:
    print(f"{play1[-1]} won, with {play1[0][3]} tries to guess their word!")
  elif play1[0][3] < play2[0][3]:
    print(f"{play2[-1]} won, with {play2[0][3]} tries to guess their word!")
  else:
    print(
      "It was pretty much a tie. Both players had the same amount of tries.")
    print("\n Looking at how many letters got highlighted, however...")
    if play1[0] == play2[0]:
      print(
        "It was a absolute tie! Both players got the same exact amount of letters highlighted!"
      )
      print(f"Green letters: {play1[0][0]}")
      print(f"Yellow letters: {play1[0][1]}")
      print(f"Not highlighted letters: {play1[0][2]}")
    elif play1[0][0] > play2[0][0]:
      print(f'''{play1[-1]} won, having the most green letters.
      Green letters: {play1[0][0]}
      Yellow letters: {play1[0][1]}
      Not highlighted letters: {play1[0][2]}''')
    elif play1[0][0] < play2[0][0]:
      print(f'''{play2[-1]} won, having the most green letters.
      Green letters: {play2[0][0]}
      Yellow letters: {play2[0][1]}
      Not highlighted letters: {play2[0][2]}''')
    elif play1[0][1] > play2[0][1]:
      print(f'''{play1[-1]} won, having the most yellow letters.
      Green letters: {play1[0][0]}
      Yellow letters: {play1[0][1]}
      Not highlighted letters: {play1[0][2]}''')
    elif play1[0][1] < play2[0][1]:
      print(f'''{play2[-1]} won, having the most yellow letters.
      Green letters: {play2[0][0]}
      Yellow letters: {play2[0][1]}
      Not highlighted letters: {play2[0][2]}''')
    elif play1[0][2] < play2[0][2]:
      print(
        f'''{play2[-1]} won, having the least amount of not-highlighted letters.
      Green letters: {play2[0][0]}
      Yellow letters: {play2[0][1]}
      Not highlighted letters: {play2[0][2]}''')
    else:
      print(
        f'''{play1[-1]} won, having the least amount of not-highlighted letters.
      Green letters: {play1[0][0]}
      Yellow letters: {play1[0][1]}
      Not highlighted letters: {play1[0][2]}''')


mode = int(
  input('''Choose a mode to play:
1: Instructions Mode (learn how to play the game (if needed))

2: Two Letter Mode
3: Three Letter Mode
4: Four Letter Mode
5: Five Letter Mode (normal wordle)
6: Six Letter Mode
7: Seven Letter Mode
8: Eight Letter Mode
9: Nine Letter Mode
10: Ten Letter Mode
11: Custom Numbers Mode (wordle, but with numbers) (you choose the number's length as well)
12: 1v1 Mode (play against your friends) (bots, number mode, word/number length)
13: VS Mode (optimized bot) (play against a bot that uses simple logic to get to its word/number) (number mode, word/number length)
Enter 1 / 2/3/4/5/6/7/8/9/10/11/12/13: '''))
while mode not in range(1, 14):
  mode = int(input("Enter a valid mode: "))

if mode == 1:
  print(f'''ok so basically
  Wordle is a simple digital word game (owned by the Times New York Papers) in which, normally, you'd have a word of length 5 and you'd have to guess, 6 times, what that word is. You'd have a table that's size is 5x6, and starting from the top row, you have to guess each word one by one, where if you don't get the word even after the last bottom row, you lose. Your word must be a real word in the English Dictionary, thereby making your choices a little limited.
  The hints you get to guess your word are as follows:
  - If some letter of the word is highlighted {Back.GREEN + "green" + Back.BLACK}, then that letter is in the randomly selected word you're trying to guess, and the letter is  in the same exact position it would be if that word were the randomly selected word.
  - If some letter of the word is highlighted {Back.YELLOW + "yellow" + Back.BLACK}, then that letter is indeed in the randomly selected word but isn't in that exact same position.
  - Lastly, if some letter of the word isn't highlighted at all, then that letter isn't in the randomly selected word at all.

  If you're still confused, you could also try it out at https://www.nytimes.com/games/wordle/index.html.
  
  With that out of the way, go try it out!''')
  mode = int(
    input('''Choose a mode to play:
2: Two Letter Mode
3: Three Letter Mode
4: Four Letter Mode
5: Five Letter Mode (normal wordle)
6: Six Letter Mode
7: Seven Letter Mode
8: Eight Letter Mode
9: Nine Letter Mode
10: Ten Letter Mode
11: Custom Numbers Mode (wordle, but with numbers) (you choose the number's length as well)
12: 1v1 Mode (play against your friends) (bots, number mode, word/number length)
13: VS Mode (optimized bot) (play against a bot that uses simple logic to get to its word/number) (number mode, word/number length)
Enter 2/3/4/5/6/7/8/9/10/11/12/13: '''))
if mode not in range(2, 14):
  mode = int(input("Enter a valid mode: "))

if mode == 2:
  while 1:
    twoword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 3:
  while 1:
    threeword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 4:
  while 1:
    fourword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 5:
  while 1:
    fiveword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 6:
  while 1:
    sixword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 7:
  while 1:
    sevenword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 8:
  while 1:
    eightword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 9:
  while 1:
    nineword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 10:
  while 1:
    tenword()
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break
elif mode == 11:
  length = input("How long should your number be? (1-10): ")
  while not (length.isnumeric()) or len(length) > 10 or len(length) < 1:
    length = input("How long should your number be? (1-10): ")
  while 1:
    numberwordle(length)
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
    else:
      print(f"You won {won} times so far")
      break

elif mode == 12:
  players = ["Player One", "Player Two"]
  player = r.choice(players)
  bot = input("Would ya like to play against the optimized bots? (Y/n): ")
  wn = input("Would ya like to play with numbers instead of words? (Y/n): ")
  length = int(input("How long should you number/word be? (1-10): "))

  print(
    "Choose who's Player One and Player Two between the two of you rill quick while I decide who goes first..."
  )
  for x in range(1, 6):
    print("\n .")
    time.sleep(1)
  print(f"{player} goes first!")
  while 1:
    oomode(bot, wn, length, player)
    play = input(
      "Would ya like to play this mode again? (to play another mode re-run the program) (Y/n): "
    )
    if play == "Y":
      print(f"You won {won} times so far!")
      player = r.choice(players)
    else:
      print(f"You won {won} times so far")
      break

elif mode == 13:
  num = input("Would you like to play with numbers? (Y/n): ")
  length = int(input("Enter your word/number's length: "))
  vsmode(length, num)
