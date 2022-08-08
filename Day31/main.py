from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}
# use the words_to_learn.csv instead of french_words.csv:
# if we remove the words_to_learn.csv file and run the code, we give file not found error for this:
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./Day31/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


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


def is_known():
    words.remove(current_card)

    pandas.DataFrame(words)
    # each time we run the code the number of record is saves in words_to_learn.csv, so we add index= false to don't
    # save these numbers:
    data.to_csv("words_to_learn.csv", index=False)
    random_cards()


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
right_button = Button(image=right_image, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./Day31/wrong.png")
wrong_button = Button(image=wrong_image, command=random_cards)
wrong_button.grid(column=0, row=1)

# back_image = PhotoImage(file="./Day31/card_back.png")
# canvas.create_image(400, 263, image=back_image)

random_cards()
flip_card()
is_known()
window.mainloop()
