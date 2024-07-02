import tkinter as tk
from tkinter import messagebox
import os


def logout():
    # Command to log out the current user on macOS
    os.system('osascript -e \'tell application "System Events" to log out\'')


def on_logout_button_click():
    # Confirm the logout action
    result = messagebox.askokcancel("Logout Confirmation", "Are you sure you want to logout?")
    if result:
        logout()


def center_window(root, width=300, height=100):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the geometry of the window
    root.geometry(f'{width}x{height}+{x}+{y}')


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Logout Confirmation")

    # Center the window
    center_window(root, 300, 100)

    # Create a label
    label = tk.Label(root, text="עליך לצאת מן המשתמש ולהתחבר מחדש (logout)", font=("Arial", 12))
    label.pack(pady=10)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    # Create Logout and Cancel buttons
    logout_button = tk.Button(button_frame, text="Logout", command=on_logout_button_click)
    logout_button.pack(side=tk.LEFT, padx=10)

    cancel_button = tk.Button(button_frame, text="Cancel", command=root.destroy)
    cancel_button.pack(side=tk.LEFT, padx=10)

    # Run the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
