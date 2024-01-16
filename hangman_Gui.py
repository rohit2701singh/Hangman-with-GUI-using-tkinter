from tkinter import *
import random
from art import stages
from word_data import word_list

THEME_COLOR = "#5684ae"
GREEN = "#53fca1"
RED = "#fd4659"


def random_word():
    """selection of a random word from list"""
    return random.choice(word_list)


selected_word = random_word()
print(selected_word)

letter_in_word = []
lives = 6


def word_selection():
    """function to show underscores '_' on screen"""
    for letter in selected_word:
        letter_in_word.append("_")
    word_label_box.config(text=letter_in_word, font="black", )
    canvas.itemconfig(lives_art, text=stages[lives])


def submit_letter(event=None):
    """function is bound with enter key. Hit enter and this function get executed. Function can be executed with
    submit button also."""
    global selected_word
    user_input = guessed_letter_entry.get().lower()

    if len(user_input) != 0:
        if user_input in selected_word:
            if user_input not in letter_in_word:
                for i in range(len(selected_word)):
                    if user_input == selected_word[i]:
                        letter_in_word[i] = user_input

                word_label_box.config(text=letter_in_word)
                notice_label_box.config(text=f"you guessed right.", bg=GREEN)

                if "_" not in letter_in_word:

                    notice_label_box.config(text=f"YOU WON")
                    word_label_box.config(text=f"Selected letter was: '{selected_word}'",
                                          font=("times new roman", 15, "italic"))
                    canvas.config(bg=GREEN)
                    canvas.itemconfig(hangman_final, text="Hangman Survived")
                    submit_button.config(state="disable", text="disabled")
                    window.unbind('<Return>')

            else:
                notice_label_box.config(text="already guessed, guess again.", bg="white")

        else:
            global lives
            lives -= 1
            notice_label_box.config(text=f"you guessed wrong.", bg=RED)
            lives_label.config(text=f"Lives: {lives}")
            canvas.itemconfig(lives_art, text=stages[lives])

            if lives == 0:
                notice_label_box.config(text="YOU LOST")
                word_label_box.config(text=f"selected letter was: '{selected_word}'", font=("times new roman", 15, "italic"))
                canvas.itemconfig(hangman_final, text="Hangman Died", )
                canvas.config(bg=RED)
                submit_button.config(state="disable", text="disabled", fg=THEME_COLOR)
                window.unbind('<Return>')

        guessed_letter_entry.delete(0, END)
        guessed_letter_entry.focus()

    else:
        notice_label_box.config(text="make guess before submission.", bg="white")


def clear():
    """function to clear previous screen and fresh start"""

    global lives, selected_word
    lives = 6

    letter_in_word.clear()
    selected_word = random_word()  # selecting new word
    print(selected_word)

    lives_label.config(text=f"Lives: {lives}")
    guessed_letter_entry.delete(0, END)
    submit_button.config(state="active", text="submit", fg=THEME_COLOR)
    notice_label_box.config(text="notice will appear here", bg="white")
    word_label_box.config(text="")

    canvas.config(bg="white")
    canvas.itemconfig(hangman_final, text="")
    canvas.itemconfig(lives_art, text=stages[lives])

    word_selection()
    word_label_box.config(text=letter_in_word)
    window.bind('<Return>', submit_letter)


# -------- creating ui ------------

window = Tk()
window.resizable(0, 0)
window.title("Hangman Game")
window.config(pady=30, padx=30, bg=THEME_COLOR)

lives_label = Label(text=f"Lives: {lives} ", bg=THEME_COLOR, fg="white", font=("times new roman", 15, "bold"))
lives_label.grid(row=0, column=0, sticky="e", columnspan=2)

guessed_letter_label = Label(text="guess the letter:", bg=THEME_COLOR, fg="white", font=("times new roman", 15))
guessed_letter_label.grid(row=1, column=0, sticky="w")

guessed_letter_entry = Entry(font=("ariel", 15,), width=27, justify="center")
guessed_letter_entry.focus()
guessed_letter_entry.grid(row=2, column=0, columnspan=2)

notice_label = Label(text="notice:", bg=THEME_COLOR, fg="white", font=("times new roman", 15))
notice_label.grid(row=3, column=0, sticky="w")

notice_label_box = Label(text='notice will appear here', font=("ariel", 13, "italic"), width=30)
notice_label_box.grid(row=4, column=0, columnspan=2)

word_label = Label(text="word:", bg=THEME_COLOR, fg="white", font=("times new roman", 15))
word_label.grid(row=5, column=0, sticky='w')

word_label_box = Label(text="", font=("ariel", 15,), width=27, justify="center")
word_label_box.grid(row=6, column=0, columnspan=2)

canvas = Canvas(width=300, height=250, bg="white")
canvas.create_text((42, 18), text="Hangman", font=("times new roman", 15, "italic"))
hangman_final = canvas.create_text((82, 241), text="", font=("times new roman", 15, "italic"))
lives_art = canvas.create_text((150, 110), text="", fill=THEME_COLOR, font=("ariel", 15, "bold"))
canvas.grid(row=9, column=0, pady=10, columnspan=2)

clear_button = Button(text="clear", width=10, fg=THEME_COLOR, font=8, command=clear)
clear_button.grid(row=7, column=0, pady=10)

submit_button = Button(text="submit", width=10, fg=THEME_COLOR, font=8, command=submit_letter)
submit_button.grid(row=7, column=1, pady=10)

window.bind('<Return>', submit_letter)  # hit enter to execute function

word_selection()

window.mainloop()
