# Treasure Island Adventure Game

This is a simple “Choose Your Own Adventure” Flask web game. Players make choices at a crossroad, a lake, and three doors. Depending on their choices they either “win” a treasure or see a dramatic “Game Over” with an image depicting what defeated them.

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/treasure-island-game.git
   cd treasure-island-game


2. Create and activate a virtual environment

python -m venv venv
source venv/Scripts/activate     # (for Git Bash on Windows)
# or on macOS/Linux:
# source venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Run the app

Directly:

python app.py


Use the Flask CLI: 

export FLASK_APP=app.py         # (Git Bash / macOS / Linux)
flask run

5. Open your browser


Navigate to http://127.0.0.1:5000/ to start playing.


