## this is my python homework 


## HW 01 PAO YING CHUB game 
import random
computer_player = ["scissor", "hammer", "paper"]
while True :
  user_player = input("scissor, hammer or paper :? ")
  computer_selected = random.choice(computer_player) ## computer random value
  ## check logic
  print(f"You choose {user_player} and commuter choose {computer_selected}")
  if user_player == computer_selected :
    ## same 
    print("Draw")
    ## not same 
  elif user_player == "hammer":
    if computer_selected == "scissor":
      print("Win")
    else:
      print("Try again")
  elif user_player == "scissor":
    if computer_selected == "paper":
      print("Win")
    else:
      print("Try again")
  elif user_player == "paper":
    if computer_selected == "hammer":
      print("Win")
    else:
      print("Try again")
  
  ## wanna play ?
  play = input("wanna play ? y/n :")
  if play != "y":
    break

#####################################################

## HW 02 class ATM at least 5 methods 
## View money
## Withdraw 
## Deposit 
## Option select

class ATM:
  ## log in 
  ## initial entry
  def __init__(self, password = 123456):
    self.password = password

  def entry_password(self):
    password = input("Entry your password") 
    print(password)
  def option_select(self):
    select_op = input(""" Pick the option you want to have 
                          1) View money
                          2) Withdraw
                          3) Deposit
                          by type number 1) or 2) or 3) :""")
    if select_op == "1":
      ATM.view_money(self)
    elif select_op =="2":
      ATM.withdraw(self)
    elif select_op == "3":
      ATM.deposit(self)
    else:
      print("wrong operation, try again")
    money_own = 0
  
  def view_money(self):
    print(f'your money is {money_own} baht')

  def withdraw(self):
    print(f'now your money is {money_own} baht')
    money_withdraw = input(f'input money to withdraw :')
    if int(money_own) > int(money_withdraw):
      withdraw_decision = input(f'Do you want to withdraw money is baht ? y/n :')
      if withdraw_decision == "Y":
        print(f'This withdraw: {money_withdraw} baht')
        print(f'Now you have money in accout {money_own - money_withdraw} bath')
    else:
      print("You don't have money enough to withdraw")

  def deposit(self):
    global money_own
    print(f'your money now is {money_own} baht')
    money_deposit = input("input your money to deposit")
    update_money = int(money_own) + int(money_deposit)
    print(f'now you deposit money {money_deposit} baht and your account is {update_money} baht')

    money_own = update_money
####
## money is 0
ATM.entry_password(123456)
ATM.option_select(123456)

############################################################
## HW 03 imdb and clean data web scraping
##!pip install gazpacho
from gazpacho import Soup
import requests
url = "https://editorial.rottentomatoes.com/guide/popular-movies/"
html = requests.get(url)

rotten = Soup(html.text)
titles = rotten.find("div", {"class":"article_movie_title"})
clean_titles = [title.strip() for title in titles]
years = rotten.find("span", {"class":"subtle start-year"})
clean_years = [year.strip() for year in years]
#######
import pandas as pd
## create dataframe
rotten_tomato_movie_database = pd.DataFrame(data = {
    "title": clean_titles,
    "years" : clean_years
})
rotten_tomato_movie_database.head()

#############################################################
## HWO4 - find public api use python to get data 

from requests import get
import time 
ship_database = [] 
for i in range(10):
  url = f"https://swapi.dev/api/starships/{i+1}/"
  resp = requests.get(url)
  if resp.status_code == 200:
    ship_json = resp.json()
    ship_database.append((ship_json["name"],
                          ship_json["passengers"]))

  time.sleep(2)

print(ship_database)




