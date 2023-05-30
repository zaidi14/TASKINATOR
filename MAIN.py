import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TASKINATOR")
        self.root.geometry("400x300")
        self.root.configure(bg="#1E1E1E")  # Set the background color

        self.task_list = []

        # Create GUI elements
        self.task_entry = ttk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        self.add_frame = tk.Frame(root, bg="#292929")  # Set the background color of the frame
        self.add_frame.pack(pady=5)

        self.add_button = ttk.Button(self.add_frame, text="Add Task", command=self.add_task, style="Accent.TButton")
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.task_listbox = tk.Listbox(root, width=30, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        self.remove_frame = tk.Frame(root, bg="#292929")  # Set the background color of the frame
        self.remove_frame.pack(pady=5)

        self.remove_button = ttk.Button(self.remove_frame, text="Remove Task", command=self.remove_task, style="Accent.TButton")
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.style = ttk.Style()
        self.style.configure("Accent.TButton", background="light gray", foreground="BLACK")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Invalid Input", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            confirmed = messagebox.askyesno("Confirm", "Are you sure you want to remove this task?")
            if confirmed:
                task = self.task_list.pop(selected_index[0])
                self.task_listbox.delete(selected_index)
                messagebox.showinfo("Task Removed", f"The task '{task}' has been removed.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#1E1E1E")  # Set the background color of the root window
    app = TaskManagerApp(root)
    root.mainloop()
