import requests
from bs4 import BeautifulSoup
from tkinter import *

window = Tk()
joke_api = "https://icanhazdadjoke.com/"
joke_count = 0

back_img = "images/DAD.png"
nick_img = "images/nicolas.png"
my_img = "images/rahul.png"
vivek_img = "images/vivek.png"
sent_img = "images/senthil.png"

back_file = PhotoImage(file=back_img)
nick_file = PhotoImage(file=nick_img)
my_file = PhotoImage(file=my_img)
vivek_file = PhotoImage(file=vivek_img)
sent_file = PhotoImage(file=sent_img)

back = Canvas(width=1028, height=568)
back.create_image(512,284,image=back_file)
back.create_rectangle(370,285,657,320, fill='red')
count = back.create_text(512,300, text=f"JOKES SEEN : {joke_count}", font=("Verdana",25,'underline'), fill='black')
back.create_rectangle(70,325,980,560, fill='white')
jk = back.create_text(500,440, text="Select the Level of Joke by clicking on the respective buttons", font=("Verdana",25,'bold'), fill='green', width=800)

def generate_joke():
    global joke_count
    joke = requests.get(joke_api)
    joke_count += 1
    html = BeautifulSoup(joke.text, 'html.parser')
    text_of_joke = html.find('p', attrs={'class': 'subtitle'}).text
    back.itemconfig(jk, text=text_of_joke)
    back.itemconfig(count, text=f"JOKES SEEN : {joke_count}")

nick = Button(image=nick_file, width=85, height=107, command=generate_joke)
rahul = Button(image=my_file, width=85, height=108, command=generate_joke)
viv = Button(image=vivek_file, width=85, height=93, command=generate_joke)
sent = Button(image=sent_file, width=85, height=105, command=generate_joke)

back.grid(row=0, column=0)
nick.place(relx=0.01, rely=0.02)
rahul.place(relx=0.90, rely=0.02)
viv.place(relx=0.01, rely=0.38)
sent.place(relx=0.9, rely=0.37)




window.mainloop()