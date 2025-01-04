import tkinter as tk

def add_task():
    task_text = task.get()
    if task_text:
        listbox.insert(tk.END, task_text)
        task.set("")
        save_tasks()

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
        save_tasks()

def save_tasks():
    with open("tasksave.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task_item in tasks:
            file.write(task_item + "\n")

def load_tasks():
    try:
        with open("tasksave.txt", "r") as file:
            tasks = file.readlines()
            for task_item in tasks:
                listbox.insert(tk.END, task_item.strip())
    except FileNotFoundError:
        pass  # Ignore if the file does not exist

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x660+400+100")
root.resizable(False, False)

# icon
iconimg = tk.PhotoImage(file="imgs/task.png")
root.iconphoto(False, iconimg)

# top bar
topimg = tk.PhotoImage(file="imgs/topbar.png")
tk.Label(root, image=topimg).pack()

noteimg = tk.PhotoImage(file="imgs/task.png")
tk.Label(root, image=noteimg, bg="#32405b").place(x=30, y=25)

titlelabel = tk.Label(root, text="TO-DO:", font="freesans 20 bold", fg="white", bg="#32405b")
titlelabel.place(x=150, y=25)

# main
# add task and delete
frame = tk.Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = tk.StringVar()
task_entry = tk.Entry(frame, textvariable=task, width=14, font="freesans 20", bd=0)
task_entry.place(height=50, x=0, y=0)

add_button = tk.Button(frame, text="ADD", command=add_task, font="freesans 20 bold", width=7, bg="#32405b", bd=0)
add_button.place(height=50, x=280, y=0)

delete_button = tk.Button(frame, text="DELETE", command=delete_task, font="freesans 20 bold", width=7, bg="#32405b", bd=0)
delete_button.place(height=50, x=176, y=0)

# list of tasks
listframe = tk.Frame(root, bd=3, width="700", height=500, bg="#32405b")  # Increase height here
listframe.place(relx=0.5, rely=0.5, anchor="center",y=100)  # Center the frame

listbox = tk.Listbox(listframe, font="freesans 12", width=40, height=15, bg="#32405b", fg="white", cursor="hand2",
                     selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Use expand to fill available space

scrollbar = tk.Scrollbar(listframe, command=listbox.yview)  # Increase thickness here
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

# Load tasks from file on startup
load_tasks()

root.mainloop()
