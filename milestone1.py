import tkinter as tk
# from PIL import ImageTk
import sqlite3
import csv
import random

bg_color = "#C3ACD0"

book_history = []

def clear_all(frames):
    for items in frame.winfo_children():
        items.destroy()

def fetch_csv():
   # Open file  
    with open('randombook.csv') as file_obj: 
        
        book_number = 50
        # Generator random number
        random_number = random.randint(0, book_number - 1)
        
        # Create reader object
        reader_obj = csv.reader(file_obj) 
        
        # Iterate over each row in the csv  
        # store it in list
        database = []
        for row in reader_obj: 
            database.append(row)

        all_books = database[random_number]
    return all_books

def recommendation_history(book):
    book_history.append(book)
    with open('recommendations.csv', 'a', newline= '') as file:
        books = csv.writer(file)
        books.writerow(book)

def load_book1():
    clear_all(frame2)
    frame1.tkraise()
    frame1.propagate(False)
    # book widget
    # book_img = ImageTk.PhotoImage(file="pictures/books_img.png")
    # book_widget = tk.Label(frame1, image=book_img, bg=bg_color)
    # book_widget.image = book_img
    # book_widget.pack()

    tk.Label(frame1, text ="Random Book Recommendation",
        bg=bg_color,
        fg="white",
        font=("TkMenuFont", 14)).pack(pady=20)
    tk.Label(frame1, text ="Hi! Welcome to the Book Recommender! I have gathered the 50 most popular books from Barnes and Noble and complied them into a database to recommend books to you! Please Press the button to get a book recommendation from many different genres.",
        bg=bg_color,
        fg="white",
        font=("TkMenuFont", 14), wraplength=400).pack(pady=20)
    tk.Label(frame1, text="",
        bg=bg_color,
        fg="white",
        font=("TkMenuFont", 14)).pack(pady=20)
    

        # button widget
    tk.Button(
        frame1, 
        text="Book Generator",
        font=("TkHeadingFont", 20), 
        bg="#4B527E", 
        fg="white",
        cursor="hand2",
        activebackground="#DFCCFB", 
        activeforeground="black", 
        command=lambda:load_book2()).pack(pady=20)

def load_book2():
    clear_all(frame1)
    frame2.tkraise()

    idx = random.randint(0, 49)
    
    with open('randombook.csv') as file_obj: 
        book_obj = csv.reader(file_obj) 
      
        # Iterate over each row in the csv  
        # store it in list
        database = []
        for row in book_obj: 
            database.append(row)

     # book widget
    # book_img = ImageTk.PhotoImage(file="pictures/books_img.png")
    # book_widget = tk.Label(frame2, image=book_img, bg=bg_color)
    # book_widget.image = book_img
    # book_widget.pack(pady=20)
    tk.Label(frame2, text="Here is your book recommendation! If you want another book, please press the button again!",
        bg=bg_color,
        fg="white",
        font=("TkMenuFont", 14), wraplength=400).pack(pady=20)
    
    book_title = database[idx][1]
    tk.Label(frame2, text =book_title,
        bg=bg_color,
        fg="white",
        font=("TkHeadingFont", 20)).pack(pady=20)
    
    # for i in items:
    #     tk.Label(frame2, text ="i",
    #         bg=bg_color,
    #         fg="white",
    #         font=("TkMenuFont", 14)).pack(pady=20)

        # button widget
    tk.Button(
        frame2, 
        text="Get another Book Text",
        font=("TkHeadingFont", 20), 
        bg="#4B527E", 
        fg="white",
        cursor="hand2",
        activebackground="#DFCCFB", 
        activeforeground="black", 
        command=lambda:load_another_book(book_title)).pack(pady=20)
    

def load_another_book(previous_book):
    load_book1()
    recommendation_history([previous_book])

    


root = tk.Tk()
root.title("Book Recommender")
root.eval("tk::PlaceWindow . center")
# root.geometry("700x700")

frame1 = tk.Frame(root, width=600, height=400, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)
# frame1.grid(row = 0, column=0)
# frame2.grid(row = 0, column=0)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

load_book1()

#run app
root.mainloop()