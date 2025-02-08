# alan chande ?

This project is a simple Python-based application that displays real-time prices of gold and currency. It uses the `tkinter` library to create a graphical user interface (GUI) and fetches data from an API.

## Features
- Displays live prices for various gold items (Global Gold Ounce, Gold Mesghal, 18 Karat Gold Gram, etc.).
- Displays live currency exchange rates for Dollar, Euro, Emirati Dirham, and Pound.
- Automatically refreshes the data every 10 seconds.
- Drag the window around your screen with ease.
- Lightweight and runs in the background with a semi-transparent window.

## Libraries Used
- `tkinter`: For creating the GUI.
- `requests`: For fetching data from the API.
- `threading`: For running the data fetching process in the background.
- `time`: For setting the interval between data updates.

## API
The data is fetched from the following API:
https://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency.json

## How to Run
1. Clone this repository or download the script.
2. Install the required libraries:
   ```bash
   pip install tkinter requests

3. Run the Python script:
    python main.py
    
The application will launch and display a semi-transparent window with real-time gold and currency prices.
