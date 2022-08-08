from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./Day31/french_words.csv")
words = data.to_dict(orient="records")
current_card = {}


def random_cards():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    # to changing card after 3 seconds:
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # to change the canvas image:
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# to changing card after 3 seconds:
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./Day31/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "normal"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "normal"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

back_image = PhotoImage(file="./Day31/card_back.png")

right_image = PhotoImage(file="./Day31/right.png")
right_button = Button(image=right_image, command=random_cards)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./Day31/wrong.png")
wrong_button = Button(image=wrong_image, command=random_cards)
wrong_button.grid(column=0, row=1)

# back_image = PhotoImage(file="./Day31/card_back.png")
# canvas.create_image(400, 263, image=back_image)

random_cards()
flip_card()
window.mainloop()


