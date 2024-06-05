import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askquestion, showinfo

class BookReaderUI:
    def __init__(self,button, ):
        self.title = title
        self.author = author
        self.genre = genre
        self.content = content

def show_home_page():
    for widget in right_frame.winfo_children():
        widget.destroy()
    homelbl = tk.Label(right_frame, text="Books are \n my \nSerenity", font=("Times", 42), bg="#948979")
    homelbl.pack(expand=True)

def show_search_page():
    for widget in right_frame.winfo_children():
        widget.destroy()

    search_entry = tk.Entry(right_frame, font=("Arial", 12), width=30)
    search_entry.grid(row=1, column=2, padx=15, pady=10)

    search_button = tk.Button(right_frame, text="Search", font=("Arial", 12), bg="#948979", command=lambda: search_books(search_entry.get(), search_results_listbox))
    search_button.grid(row=1, column=3, padx=10, pady=10)

    availbooks_lbl = tk.Label(right_frame, text="Available Books", font=("Times", 12), bg="#948979")
    availbooks_lbl.grid(row=4, column=2, columnspan=2, pady=(10, 0))

    book_listbox = tk.Listbox(right_frame, font=("Arial", 12), width=50, height=10)
    book_listbox.grid(row=5, column=2, columnspan=2, padx=15, pady=10)
    
def search_books(query, listbox):
    filtered_books = [book for book in books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
    update_listbox(listbox, filtered_books)

def update_listbox(listbox, books):
    listbox.delete(0, tk.END)
    for idx, book in enumerate(books, 1):
        listbox.insert(tk.END, f"{idx}. {book.title}")

def on_book_select(event, listbox):
    selected_index = listbox.curselection()
    if selected_index:
        selected_text = listbox.get(selected_index)
        selected_title = " ".join(selected_text.split(". ")[1:])
        selected_book = next((book for book in books if book.title == selected_title), None)
        if selected_book:
            answer = askquestion("Read Book", f"Do you want to read '{selected_book.title}' by {selected_book.author}?")
            if answer == 'yes':
                show_content(selected_book)

def show_content(book):
    for widget in right_frame.winfo_children():
        widget.destroy()

    content_lbl = tk.Label(right_frame, text=f"Title: {book.title}\n\nContent:\n{book.content}", font=("Arial", 12), bg="#948979", wraplength=500)
    content_lbl.pack(padx=15, pady=10)

window = tk.Tk()
window.title("READ ME")
window.geometry("600x700")
window.resizable(False, False)

right_frame = tk.Frame(window, bg='#948979', highlightbackground='black', highlightthickness=1)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
right_frame.pack_propagate(False)

left_frame = tk.Frame(window, bg="#DFD0B8")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)
left_frame.pack_propagate(False)

home_btn = tk.Button(left_frame, bg="#DFD0B8", text="Home", font=('Lora', 12), width=15, command=show_home_page)
home_btn.grid(row=5, column=0, sticky="ew", padx=10, pady=15)

search_btn = tk.Button(left_frame, bg="#DFD0B8", text="Search", font=('Lora', 12), width=15, command=show_search_page)
search_btn.grid(row=10, column=0, sticky="ew", padx=10, pady=15)

homelbl = tk.Label(right_frame, text="Books are \n my \nSerenity", font=("Times", 42), bg="#948979")
homelbl.pack(expand=True)

window.mainloop()
