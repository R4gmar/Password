from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": username,
        "password": password

    }
    }
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail {username}"
                               f"\nPassword: {password} \nis it OK to save? ")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #reading old data
                    data = json.load(data_file)
                    # Saving updated data
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # update old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data found for {website}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website: ")
website.grid(column=0, row=1)
username = Label(text="Email/Username: ")
username.grid(column=0, row=2)
password = Label(text="Password: ")
password.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w", padx=5, pady=5)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w", padx=5, pady=5)
username_entry.insert(0, "xlubaxandreyx@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, sticky="w", padx=5, pady=5)

#Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=1, sticky="w", padx=5, pady=5)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, columnspan=1, sticky="w", padx=5, pady=5)


window.mainloop()