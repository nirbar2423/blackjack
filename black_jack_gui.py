# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:25:19 2021

@author: nir
"""

import random
import time
import PySimpleGUI as sg

sg.SetOptions(element_padding=(5,9),font=('Verdana',14),input_elements_background_color='#272727',input_text_color='#ffffff') # Add a touch of color
class Card:
  def __init__(self,suit,val):
    self.suit = suit
    self.value = val
  def show(self):
    if (self.value == 13):
      return (str ("K") + " " + str (self.suit)  )
    elif (self.value == 12):
      return (str ("Q") + " " + str (self.suit)  )
    elif (self.value == 11):
      return (str ("J") + " " + str (self.suit)  )
    elif (self.value == 1):
      return (str ("A") + " " + str (self.suit)  )
    else:
      return (str (self.value) + " " + str (self.suit)  )
  def get_value(self):
    return self.value
class Deck:
  def __init__(self):
    self.cards = []
    self.build()
  def build(self):
    for value in range(1,14):
      for type in ["♠","♡","♣","♢"]:
        self.cards.append(Card(type,value))
  def show(self):
    for card in self.cards:
      card.show()
  def pick_a_card(self):
    pick = self.cards[int (random.random()*len(self.cards))]
    self.cards.remove(pick)
    pick.show()
    return pick
  def pick_a_hiden_card(self):
    pick = self.cards[int (random.random()*len(self.cards))]
    self.cards.remove(pick)
    return pick
  def add_to_array_val(self,arr,card):
    if card.get_value()>10:
      arr.append(10)
    elif card.get_value()==1:
      arr.append(11)
    else:
      arr.append(card.get_value())
    return arr
  def show_all_cards(arr):
    for i in range(len(arr)):
      i.show()
def window_show(cards,oponnent_first_card):
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your opponent first card is:\t' + oponnent_first_card.show())],
             [sg.Text("what do you want to do?")],
             [sg.Button('take a card',tooltip='take one more card')],[sg.Button('stop',tooltip=("it's good for me"))] ]
    window = sg.Window('choose what to do', layout)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "take a card":
            take_a_card = 1
            break
        if event == "stop":
            take_a_card = 0
            break
    window.close()
    return take_a_card
def window_oponnent_cards_show(cards,oponnent_cards):    
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your opponent cards are:\t' + oponnent_cards)],
             [sg.Button('continue', bind_return_key=True)]]
    window = sg.Window('showing opponents cards', layout,return_keyboard_events=True)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'continue': # if user closes window or clicks cancel
            break
        time.sleep(2)
        break    
    window.close()
def double_window_show(cards,oponnent_cards):
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your opponent first card is:\t' + oponnent_cards)],
             [sg.Button('ok',tooltip='take one more card')] ]
    window = sg.Window('double', layout)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "ok":
            break
    window.close()
def check_result(value):
    if (sum(value)>21):
            for i in range(len(value)):
                if value[i] == 11:
                  value[i] = 1
                  break
    return value
def window_you_win(cards,oponnent_cards,bet):
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your oponnent cards are:\t' + oponnent_cards)],
             [sg.Text("you win!!!!")],
             [sg.Button('play another game',tooltip='start new game', bind_return_key=True)] ]
    window = sg.Window('you win', layout,return_keyboard_events=True)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "play another game":
            break
    window.close()
    return bet
def window_you_lose(cards,oponnent_cards,bet,value):
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your opponent cards are:\t' + oponnent_cards)],
             [sg.Text("you have " + str (sum(value)) + " points, you lose")],
             [sg.Button('ok', bind_return_key=True)] ]
    window = sg.Window('you lose', layout,return_keyboard_events=True)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "ok":
            break
    window.close()
    return -bet
def window_you_win_amount(cards,oponnent_cards,bet,value,oponnent_value):
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your opponent cards are:\t' + oponnent_cards)],
             [sg.Text("you have " + str (sum(value)) + " points")],
             [sg.Text("your opponent have " + str (sum(oponnent_value)) + " points, you win")],
             [sg.Button('ok', bind_return_key=True)] ]
    window = sg.Window('you win', layout,return_keyboard_events=True)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "ok":
            break
    window.close()
    return bet
def window_you_lose_amount(cards,oponnent_cards,bet,value,oponnent_value):
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your opponent cards are:\t' + oponnent_cards)],
             [sg.Text("you have " + str (sum(value)) + " points")],
             [sg.Text("your opponent have " + str (sum(oponnent_value)) + " points, you lose")],
             [sg.Button('ok', bind_return_key=True)] ]
    window = sg.Window('you lose', layout,return_keyboard_events=True)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "ok":
            break
    window.close()
    return -bet
def window_its_draw_amount(cards,oponnent_cards,bet,value,oponnent_value):
    layout = [  [sg.Text("your cards are:\n" + cards) ],
             [sg.Text('your opponent cards are:\t' + oponnent_cards)],
             [sg.Text("you have " + str (sum(value)) + " points")],
             [sg.Text("your opponent have " + str (sum(oponnent_value)) + " points, its draw")],
             [sg.Button('ok', bind_return_key=True)] ]
    window = sg.Window('its draw', layout,return_keyboard_events=True)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "ok":
            break
    window.close()
    return 0
def window_bet(money):
    layout = [  [sg.Text('you have ' + str (money) + " dollars")],
                 [sg.Text('how much do you want to bet on?\t'), sg.InputText()],
                 [sg.Button('Ok', bind_return_key=True)] ]
                 
            # Create the Window
    window = sg.Window('place your bet', layout,return_keyboard_events=True)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "Ok":
           bet =int (values[0]) 
           break
    window.close()
    while bet>money or bet<0:
        layout = [  [sg.Text('not a legal bet!')],
                 [sg.Text('you have ' + str (money) + " dollars")],
                 [sg.Text('how much do you want to bet on?\t'), sg.InputText()],
                 [sg.Button('Ok')] ]
        window = sg.Window('place your bet', layout)
# Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            if event == "Ok":
                bet =int (values[0]) 
            break
        window.close()
    return bet
def double_bet(bet,value,cards,oponnent_cards,oponnent_value,deck,money):
    new_card = deck.pick_a_card()
    value = deck.add_to_array_val(value, new_card)
    cards += "\t" + new_card.show()
    value = check_result(value)
   # if sum(value) == 21:
   #     money += window_you_win(cards,oponnent_cards,bet)
    #    return money
    if sum(value) >21:
        money += window_you_lose(cards,oponnent_cards,bet,value)
        return money
    double_window_show(cards, oponnent_cards)
    #if sum(oponnent_value) == 21:
    #     money += window_you_lose_amount(cards,oponnent_cards,bet,value,oponnent_value)
    if sum(oponnent_value)>=17:
        if sum(oponnent_value) > 21:
            money += window_you_win(cards,oponnent_cards,bet)
        elif sum(oponnent_value) >= 17:
            if sum(oponnent_value) < sum(value):
                money += window_you_win_amount(cards,oponnent_cards,bet,value,oponnent_value)
            elif sum(oponnent_value) > sum(value):
                money += window_you_lose_amount(cards,oponnent_cards,bet,value,oponnent_value)
            else:
                money += window_its_draw_amount(cards,oponnent_cards,bet,value,oponnent_value)
    while sum(oponnent_value)<17:
        new_oponnent_card = deck.pick_a_card()
        oponnent_value = deck.add_to_array_val(oponnent_value, new_oponnent_card)
        oponnent_cards += "\t" + new_oponnent_card.show()
        oponnent_value = check_result(oponnent_value)
        window_oponnent_cards_show(cards,oponnent_cards)
        if sum(oponnent_value) > 21:
            money += window_you_win(cards,oponnent_cards,bet)
        elif sum(oponnent_value) >= 17:
            if sum(oponnent_value) < sum(value):
                money += window_you_win_amount(cards,oponnent_cards,bet,value,oponnent_value)
            elif sum(oponnent_value) > sum(value):
                money += window_you_lose_amount(cards,oponnent_cards,bet,value,oponnent_value)
            else:
                money += window_its_draw_amount(cards,oponnent_cards,bet,value,oponnent_value)
    return money
def window_for_double_without_money(money,bet):
    layout = [  [sg.Text('you have ' + str (money) + " dollars")],
                 [sg.Text('your bet is on ' + str (bet) + "dollars")],
                 [sg.Text('you dont have enough money to bet double')],
                 [sg.Button('Ok')] ]
                 
            # Create the Window
    window = sg.Window('double not posible', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "Ok":
           break
    window.close()
    
def window_creation(money,bet):
    double = 0 
    cards =""
    oponnent_cards = ""
    value = []
    oponnent_value = []
    deck = Deck()
    first_card = deck.pick_a_card()
    value = deck.add_to_array_val(value,first_card)
    second_card = deck.pick_a_card()
    value = deck.add_to_array_val(value,second_card)
    oponnent_first_card = deck.pick_a_card()
    oponnent_value = deck.add_to_array_val(oponnent_value,oponnent_first_card)
    oponnent_cards += oponnent_first_card.show()
    oponnent_second_card = deck.pick_a_card()
    oponnent_value = deck.add_to_array_val(oponnent_value,oponnent_second_card)
    cards += first_card.show() + "\t" + second_card.show()
    oponnent_cards += "\t" + oponnent_second_card.show()
    value = check_result(value)
    if sum(value) == 21:
        money += window_you_win(cards,oponnent_cards,bet)
        return money
    layout = [  [sg.Text("your first two cards are:\n" + first_card.show() + "\t" + second_card.show()) ],
              [sg.Text('your oponnent first card is:\t' + oponnent_first_card.show())],
              [sg.Text("what do you want to do?")],
              [sg.Button('take a card',tooltip='take one more card')],[sg.Button('stop',tooltip=("it's good for me"))],[sg.Button('double',tooltip=("you get only one card and double your bet"))] ]
            # Create the Window
    window = sg.Window('choose what to do' , layout)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "take a card":
            take_a_card = 1
            break
        if event == "stop":
            take_a_card = 0
            break
        if event == "double":
            if bet*2>money:
                window_for_double_without_money(money,bet)
            else:
                double = 1
                take_a_card = 0
                break
    window.close()
    if double == 1:
        money = double_bet(2*bet,value,cards,oponnent_cards,oponnent_value,deck,money)
        return money
    while (take_a_card == 1) and (sum(value) < 21):
        new_card = deck.pick_a_card()
        value = deck.add_to_array_val(value, new_card)
        cards += "\t" + new_card.show()
        value = check_result(value)
        if sum(value) < 21:
            take_a_card = window_show(cards,oponnent_first_card)
        #if sum(value) == 21:
        #    money += window_you_win(cards,oponnent_cards,bet)
        if sum(value) >21:
            money += window_you_lose(cards,oponnent_cards,bet,value)
        if sum(value)==21:
            take_a_card = 0
    if take_a_card ==0:
            window_oponnent_cards_show(cards,oponnent_cards)
         #   if sum(oponnent_value) == 21:
          #       money += window_you_lose_amount(cards,oponnent_cards,bet,value,oponnent_value)
            if sum(oponnent_value)>=17:
                if sum(oponnent_value) > 21:
                    money += window_you_win(cards,oponnent_cards,bet)
                elif sum(oponnent_value) >= 17:
                    if sum(oponnent_value) < sum(value):
                        money += window_you_win_amount(cards,oponnent_cards,bet,value,oponnent_value)
                    elif sum(oponnent_value) > sum(value):
                        money += window_you_lose_amount(cards,oponnent_cards,bet,value,oponnent_value)
                    else:
                        money += window_its_draw_amount(cards,oponnent_cards,bet,value,oponnent_value)
            while sum(oponnent_value)<17:
                new_oponnent_card = deck.pick_a_card()
                oponnent_value = deck.add_to_array_val(oponnent_value, new_oponnent_card)
                oponnent_cards += "\t" + new_oponnent_card.show()
                oponnent_value = check_result(oponnent_value)
                window_oponnent_cards_show(cards,oponnent_cards)
                if sum(oponnent_value) > 21:
                    money += window_you_win(cards,oponnent_cards,bet)
                elif sum(oponnent_value) >= 17:
                    if sum(oponnent_value) < sum(value):
                        money += window_you_win_amount(cards,oponnent_cards,bet,value,oponnent_value)
                    elif sum(oponnent_value) > sum(value):
                        money += window_you_lose_amount(cards,oponnent_cards,bet,value,oponnent_value)
                    else:
                        money += window_its_draw_amount(cards,oponnent_cards,bet,value,oponnent_value)
    return money

money =100
while money>0:
    bet = window_bet(money)
    money = window_creation(money,bet)

layout = [ [sg.Text("you lost all your money you stupied idiot!!!")],
            [sg.Text("what do you want to do now?")],
            [sg.Button("beg for mercy"),sg.Button("rob a bank"),sg.Button("kill yourself"),sg.Button("go home and wait for the wife to kill you")]]
window = sg.Window('you win', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK' or event == "beg for mercy" or event == "rob a bank" or event =="kill yourself" or event =="go home and wait for the wife to kill you": # if user closes window or clicks cancel
        break
window.close()
