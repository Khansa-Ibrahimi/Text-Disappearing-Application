BACKGROUND_COLOR = "#dfafb4"

from tkinter import Tk, Label, Button, Text
import random
from datetime import datetime

# Setting up the window
window = Tk()
window.minsize(800, 600)
window.title("Don't Stop Typing!")
window.config(padx=30, pady=20,background=BACKGROUND_COLOR)

#global variables that stores the time of the last key press and if the typing has started.
key_pressed_time = None
typing_started = False

def on_key_press_time(event):
    """Gets the time of the last key press and starts the word count update.

    Args:
        event (tkinter.Event): The event object containing details of the key press.
    """
    global key_pressed_time
    global typing_started
    key_pressed_time = datetime.now() #Update the time last key was pressed
    word_count_function() #Updates the word count
    if not typing_started: #Check if typing hasn't started yet
        typing_started = True
        get_current_time() #Starts checking the time

def get_current_time():
    """
    Gets the current time and continuously checks the time difference to ensure typing hasn't stopped.
    Calls itself every second to keep checking the time.
    """
    global current_time
    current_time = datetime.now() #Gets the current time
    check_last_keystroke() #Check if the last keystroke was more than 5 seconds ago
    if typing_started:  # Only continue checking if typing has started
        window.after(1000, get_current_time) #Calls itself every second

def check_last_keystroke():
    """
    Checks the time difference between the current time and the last key press.
    If the difference is 5 seconds or more, it deletes the text in the text box and resets the word count.
    """
    global current_time
    global key_pressed_time
    global label_prompt
    global typing_started
    if key_pressed_time and (current_time - key_pressed_time).seconds >= 5:
        #if the difference between the last keystroke and the current time is equal or more than 5 seconds
        text_box.config(state='normal') #enable the textbox
        text_box.delete('1.0', 'end') #delete all the content
        text_box.config(state='disabled') #disable the textbox so that the user can't type in it
        label_prompt.config(text='',background=BACKGROUND_COLOR) #Clear the existing prompt
        word_count_label.config(text="Word Count: 00") #Reset the word counter
        typing_started = False #Reset the typing status

def no_prompt_btn_function():
    """
    Allows the user to start writing without a prompt.
    Deletes any existing text and enables the text box for writing.
    """
    global key_pressed_time, typing_started
    key_pressed_time = None
    typing_started = False
    label_prompt.config(text="",background=BACKGROUND_COLOR) #Clear the existing prompt
    text_box.config(state='normal') #Enable the user to type
    text_box.delete('1.0', 'end') #Delete any existing text

def prompt_btn_function():
    """
    Allows the user to type and provides a random writing prompt.
    Deletes any existing text, enables the text box for writing, and displays a randomly selected prompt.
    """
    global key_pressed_time, typing_started
    key_pressed_time = None
    typing_started = False
    text_box.config(state='normal') #Enable the user to type
    text_box.delete('1.0', 'end') #Delete any existing text
    prompt_list = ["Tell a story from your favorite era. ",
                   "Tell the story of the first time that you learned to do something really well. ",
                   "Describe your perfect day.",
                   "What would you do if you had a million dollars?",
                   "Write about a memorable dream you had.",
                   "What is your favorite childhood memory?",
                   "Imagine you could time travel. Where would you go?",
                   "Write about a time you overcame a challenge.",
                   "If you could have any superpower, what would it be and why?",
                   "Describe a place you feel most at peace.",
                   "What is the most important lesson you’ve learned in life?",
                   "If you could meet any historical figure, who would it be and why?"
                   ]

    select_prompt = random.choice(prompt_list) # Randomly select a prompt
    print(select_prompt)
    label_prompt.config(text=select_prompt,background=BACKGROUND_COLOR) #Display the prompt

def word_count_function():
    """
    Updates the word count label based on the text written in the text box.
    """
    text_written = text_box.get('1.0', 'end-1c') #Gets the text in the textbox
    words = text_written.split() #splits the text into words by spaces
    word_count = len(words) #Count the number of words
    if word_count < 10: #Format the display of the word count
        word_count_label.config(text=f'Word Count: 0{word_count}')
    else:
        word_count_label.config(text=f'Word Count: {word_count}')

#Title Lable
title_label = Label(window,
                    text='If you stop for 5 seconds, your work will disappear!!!',
                    font=('Arial', 18, 'bold'),
                    background=BACKGROUND_COLOR
                    )
title_label.grid(row=0, column=0, columnspan=3)
title_label.config(pady=10)

#Button to generate a prompt
prompt_btn = Button(text='Generate a Prompt', command=prompt_btn_function)
prompt_btn.grid(row=1, column=0)

#Button to write without a prompt
no_prompt_btn = Button(text='Start Writing w/o Prompt', command=no_prompt_btn_function)
no_prompt_btn.grid(row=1, column=1)

#Word count label
word_count_label = Label(text="Word Count: 00",background=BACKGROUND_COLOR)
word_count_label.grid(row=1, column=2)

#text box for writing
text_box = Text(bg='white', font=('Arial', 12, 'normal'), state='disabled')
text_box.grid(pady=10)
text_box.grid(row=3, column=0, columnspan=3)

#label to display the prompt
label_prompt = Label(text='', padx=10, font=('Arial', 15, 'normal'), wraplength=600, background=BACKGROUND_COLOR)
label_prompt.grid(row=2, column=0, columnspan=3)

# Bind key press event to the on_key_press_time function
window.bind('<KeyPress>', on_key_press_time)
word_count_function() # Initialize the word count

#start the mainloop
window.mainloop()
