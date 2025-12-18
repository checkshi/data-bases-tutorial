# Guestbook App

This repository contains a minimal Flask guestbook that writes submissions to a local SQLite database and renders them on the page.

## Prerequisites
- Python 3.10+
- pip

## Setup
1. (Optional) Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the app locally
1. Start the Flask server (use `python3` if your system defaults `python` to Python 2):
   ```bash
   python3 app.py
   ```
2. Open the app in your browser at [http://localhost:5000](http://localhost:5000).

On first start, a `data.db` file is created in the repository root with a `guests` table. Submissions are stored there and immediately displayed below the form.

## Resetting data
If you want a clean slate, stop the server and delete `data.db`, then start the app again to recreate the database.
