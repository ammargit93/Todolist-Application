import tkinter as tk
from tasks import Task
import smtplib
from tkinter import messagebox

class Menu:
    def __init__(self, w):
        self.button1 = tk.Button(text="Add a Task", height=5, width=25, command=self.on_button1_click)
        self.button1.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.submit1 = tk.Button(text="submit", height=1, width=5, command=self.submit1)

        self.button2 = tk.Button(text="Delete Task", height=5, width=25, command=self.on_button2_click)
        self.button2.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.submit2 = tk.Button(text="submit", height=1, width=5, command=self.submit2)

        self.button3 = tk.Button(text="Update Task", height=5, width=25, command=self.on_button3_click)
        self.button3.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.submit3 = tk.Button(text="change", height=1, width=5, command=self.submit3)

        self.button4 = tk.Button(text="View Tasks", height=5, width=25, command=self.on_button4_click)
        self.button4.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        self.button5 = tk.Button(text="Clear All", height=5, width=25, command=self.on_button5_click)
        self.button5.grid(row=4, column=0, padx=20, pady=20, sticky="w")

        self.email_button = tk.Button(text="Save to email", height=3, width=10, command=self.save_to_email)
        self.email_button.place(x=410,y=550)

        self.submit_email = tk.Button(text="save", height=1, width=5, command=self.submit_email)

    def on_button1_click(self):
        l = tk.Label(text="Add a Task ")
        l.grid(column=1, row=0)
        self.add_text = tk.Text(height=5, width=30)
        self.add_text.grid(column=2, row=0)
        self.submit1.grid(row=0, column=3, padx=10, pady=10, sticky="w")

    def submit1(self):
        task_content = self.add_text.get("1.0", tk.END)
        task = Task()
        task.add_tasks(task_content)

    def on_button4_click(self):
        task = Task()
        task.view()
        listbox = tk.Listbox(height=40, width=50)
        for item in task.task_list:
            listbox.insert(task.task_list.index(item), item)
        listbox.place(x=800, y=0)

    def on_button2_click(self):
        l = tk.Label(text="Enter Id")
        l.grid(column=1, row=1)
        self.input = tk.Entry(width=10)
        self.input.grid(column=2, row=1)
        self.submit2.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    def submit2(self):
        id = self.input.get()
        task = Task()
        task.delete_tasks(int(id))

    def on_button5_click(self):
        task = Task()
        task.clear_all()

    def on_button3_click(self):
        l = tk.Label(text="Enter id to change")
        l.grid(column=1, row=2)
        self.input = tk.Entry(width=10)
        self.input.grid(column=2, row=2)
        self.submit3.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    def submit3(self):
        id = int(self.input.get())
        task = Task()
        task.update_task(id)

    def save_to_email(self):
        email_label = tk.Label(text="email")
        email_label.place(x=510, y=550)
        self.email = tk.Entry(width=20)
        self.email.place(x=565, y=550)

        password_label = tk.Label(text="password")
        password_label.place(x=510, y=580)

        self.password = tk.Entry(width=20)
        self.password.place(x=565, y=580)

        self.submit_email.place(x=600,y=610)

    def submit_email(self):
        task = Task()
        task.view()
        message = ""
        for item in task.task_list:
            item = item.replace("\n","")
            message += item+"\n"
        if self.email.get() == "" or self.password.get() == "":
            messagebox.showwarning("field is empty", "Please fill all the fields before submitting")
        else:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.email.get(), password=self.password.get())
                connection.sendmail(
                    from_addr=self.email.get(),
                    to_addrs="ammar.ice98@gmail.com",
                    msg=message)
