from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./Day31/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.create_text(400, 150, text="title", font=("Arial", 40, "normal"))
canvas.create_text(400, 263, text="apple", font=("Arial", 60, "normal"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="./Day31/right.png")
right_button = Button(image=right_image)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./Day31/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.grid(column=0, row=1)


# back_image = PhotoImage(file="./Day31/card_back.png")
# canvas.create_image(400, 263, image=back_image)



window.mainloop()