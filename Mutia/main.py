import tkinter as tk
from tkinter import messagebox
from aircon_module import Aircon

# Main app window
root = tk.Tk()
root.title("Air Conditioner Details")
root.geometry("400x300")
root.configure(bg="#E6F0FF")  # Light blue tone

# --- Input fields ---
tk.Label(root, text="Aircon Name:", fg="darkblue", bg="#E6F0FF", font=("Segoe UI", 10, "bold")).pack(pady=(10, 0))
txt_name = tk.Entry(root, font=("Segoe UI", 10))
txt_name.pack()

tk.Label(root, text="Aircon Type:", fg="darkblue", bg="#E6F0FF", font=("Segoe UI", 10, "bold")).pack(pady=(10, 0))
txt_type = tk.Entry(root, font=("Segoe UI", 10))
txt_type.pack()

tk.Label(root, text="Horse Power (HP):", fg="darkblue", bg="#E6F0FF", font=("Segoe UI", 10, "bold")).pack(pady=(10, 0))
txt_hp = tk.Entry(root, font=("Segoe UI", 10))
txt_hp.pack()

# Function to show details
def show_details():
    name = txt_name.get().strip()
    ac_type = txt_type.get().strip()
    hp = txt_hp.get().strip()

    # Validation
    if not name or not ac_type or not hp:
        messagebox.showwarning("Validation", "Please fill in all fields.")
        return

    if not hp.replace(".", "", 1).isdigit():
        messagebox.showwarning("Validation", "Horse Power must be a number.")
        return

    # Create Aircon object
    aircon = Aircon(name, ac_type, hp)
    messagebox.showinfo("Aircon Details", aircon.details())

# Button
btn_show = tk.Button(root, text="Show Details", bg="#3CB371", fg="white", font=("Segoe UI", 10, "bold"),
                    relief="flat", command=show_details)
btn_show.pack(pady=15)

root.mainloop()
