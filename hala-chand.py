import tkinter as tk
from tkinter import ttk
import requests
import threading
import time
from tkinter import font

# API Settings
API_URL = "https://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency.json"

# Function to fetch data from the API
def fetch_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error in fetching data")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


english_gold_label = ["Global Gold Ounce", "Gold Mesghal", "18 Karat Gold Gram", "24 Karat Gold Gram", "Bahare Azadi Coin", "Imami Coin", "Half Coin", "Quarter Coin", "Gram Coin"]
english_currency_label = ["Dollar", "Euro", "Emirati Dirham", "Pound"]
units = [""]

# Function to update data in the GUI
def update_data():
    while True:
        data = fetch_data()
        if data:
            # Updating gold data
            for index, item in enumerate(data.get("gold", [])):
                if index < len(english_gold_label):  # Ensure the index is valid
                    name = english_gold_label[index]
                    price = f"{item['price']:,} {'Rial' if item['unit'] == 'ریال' else 'Toman'}"  # Format price with thousand separators
                    if name in gold_labels:
                        gold_labels[name].config(text=f"{name} => {price}")

            # Updating currency data
            for index, item in enumerate(data.get("currency", [])):
                if index < len(english_currency_label):  # Ensure the index is valid
                    name = english_currency_label[index]
                    price = f"{item['price']:,} Toman"  # Format price with thousand separators
                    if name in currency_labels:
                        currency_labels[name].config(text=f"{name} => {price}")

        time.sleep(10)  # Update every 10 seconds

# Create the main window with a dark theme
root = tk.Tk()
root.title("Real-time Prices of Gold and Currency")
root.overrideredirect(True)
root.wm_attributes("-alpha", 0.7)

# Set the window position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 400
x_position = screen_width - window_width
y_position = 0
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

x_offset = 0
y_offset = 0

def start_drag(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def drag_window(event):
    x = root.winfo_pointerx() - x_offset
    y = root.winfo_pointery() - y_offset
    root.geometry(f"+{x}+{y}")

root.bind("<Button-1>", start_drag) 
root.bind("<B1-Motion>", drag_window)

# Style for buttons and labels
style = ttk.Style()
style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF")
style.configure("TFrame", background="#2E2E2E")

# Create frames for better organization
gold_frame = ttk.LabelFrame(root, style="TFrame")
gold_frame.pack(pady=0, padx=0, fill="x")

currency_frame = ttk.LabelFrame(root, style="TFrame")
currency_frame.pack(pady=0, padx=0, fill="x")

gold_labels = {}
currency_labels = {}

# Gold labels
for item in english_gold_label:
    label = ttk.Label(gold_frame, text=f"{item} => Fetching data...", style="TLabel")
    label.pack(pady=5, anchor="w")
    gold_labels[item] = label

# Currency labels
for item in english_currency_label:
    label = ttk.Label(currency_frame, text=f"{item} => Fetching data...", style="TLabel")
    label.pack(pady=0, anchor="w")
    currency_labels[item] = label

# Start a thread to update data
update_thread = threading.Thread(target=update_data)
update_thread.daemon = True
update_thread.start()

# Run the main GUI loop
root.mainloop()
