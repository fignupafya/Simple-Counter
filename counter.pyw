import tkinter as tk
from tkinter import ttk

def configure_style():
    style = ttk.Style()
    style.theme_use('clam')  
    style.theme_settings("clam", {
        "TLabel": {"configure": {"background": "black", "foreground": "white"}},
        "TButton": {"configure": {"background": "black", "foreground": "white"}},
        "TFrame": {"configure": {"background": "black"}},
        "TEntry": {"configure": {"fieldbackground": "gray", "foreground": "white"}}
    })

def update_counter(value, counter_label):
    if value.strip() and value.strip().lstrip('-').isdigit():
        counter_label.config(text=value.strip())

def create_counter_app():
    root = tk.Tk()
    root.title("Simple Counter")

    win_width = 400
    win_height = 250
    root.geometry(f"{win_width}x{win_height}")
    root.configure(bg='black')

    configure_style()

    counter_label = ttk.Label(root, text="0", font=("Arial", 20))
    counter_label.pack(pady=(60, 10))

    def increment_counter():
        current_value = int(counter_label["text"])
        counter_label.config(text=str(current_value + 1))

    def decrement_counter():
        current_value = int(counter_label["text"])
        counter_label.config(text=str(current_value - 1))

    def reset_counter():
        counter_label.config(text="0")

    def set_counter():
        update_counter(entry.get(), counter_label)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    increment_button = ttk.Button(button_frame, text="+", command=increment_counter, width=10, cursor="hand2")
    increment_button.pack(side=tk.LEFT, padx=10)

    decrement_button = ttk.Button(button_frame, text="-", command=decrement_counter, width=10, cursor="hand2")
    decrement_button.pack(side=tk.LEFT, padx=10)

    entry_frame = ttk.Frame(root)
    entry_frame.pack(pady=10)

    entry = ttk.Entry(entry_frame, font=("Arial", 12))
    entry.pack(side=tk.LEFT, padx=10)

    edit_button = ttk.Button(entry_frame, text="Set", command=set_counter, cursor="hand2")
    edit_button.pack(side=tk.LEFT, padx=10, pady=10)

    reset_button = ttk.Button(root, text="Reset", command=reset_counter, cursor="hand2")
    reset_button.place(relx=1, x=-10, y=10, anchor=tk.NE)

    root.mainloop()

if __name__ == '__main__':
    create_counter_app()
