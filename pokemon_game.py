# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:15:48 2023

@author: drsau
"""
from tkinter import *
from PIL import ImageTk,Image
import random
root = Tk()

root.title("Endless pokemon Game")
root.geometry("600x600")

root.configure(background="chocolate1")

pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
abra= ImageTk.PhotoImage(Image.open("abra.jpg"))
balbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))


pokemon_list = [pikachu,abra,balbasour, kadabra,nidoking,jigglypuff,paras,persion,ratata,squirtle,Iyvasour,charmender]
power_list  = [200,30,60,70,90,70,40,70,40,50,100,50]


player1 = Label(root,text = "Player 1" , bg = "royal blue",fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor = CENTER)

player2 = Label(root, text = "Player 2" , bg = "royal blue" , fg = "white")
player2.place(relx = 0.9 , rely=0.3 , anchor=CENTER)

player_1_score_label  = Label(root , bg = "red",fg = "white")
player_1_score_label.place(relx=0.1 , rely=0.4 , anchor=CENTER)

player_2_score_label = Label(root , bg = "red",fg = "white")
player_2_score_label.place(relx=0.9 , rely=0.4 , anchor=CENTER)

random_pokemon_card = Label(root , bg ="white",fg = "black")
random_pokemon_card.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

player1_score = 0
def player1():
    global player1_score
    random_pokemon = random.randint(0,11)
    pokemon_name = pokemon_list[random_pokemon]
    random_pokemon_card["image"] = pokemon_name 
    power = power_list[random_pokemon]
    player1_score = player1_score + power
    player_1_score_label["text"] = str(player1_score)
    
player_1_btn = Button(root , image = button, command = player1)
player_1_btn.place(relx = 0.1 , rely  =0.6 , anchor  =CENTER)

player2_score = 0

def player2():
   
    global player2_score
    random_pokemon = random.randint(0,11)
    pokemon_name2 = pokemon_list[random_pokemon]
    random_pokemon_card["image"] = pokemon_name2 
    power2 = power_list[random_pokemon]
    player2_score = player2_score + power2
    player_2_score_label["text"] = str(player2_score)

player_2_btn = Button(root, image = button  ,  command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor = CENTER)
root.mainloop()