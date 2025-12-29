import sqlite3
import os

# Path setup
DB_FOLDER = "data"
DB_PATH = os.path.join(DB_FOLDER, "workouts.db")

def get_connection():
    """Returns a connection to the SQLite database with foreign keys enabled."""
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)
    
    conn = sqlite3.connect(DB_PATH)
    # Enable foreign key support (important for cascading deletes)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Creates the tables if they do not exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Table for general workout info
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                exercise_name TEXT NOT NULL,
                weight REAL NOT NULL
            )
        ''')
        
        # Table for specific sets (One-to-Many relationship)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                workout_id INTEGER NOT NULL,
                set_number INTEGER NOT NULL,
                reps_min INTEGER NOT NULL,
                reps_max INTEGER NOT NULL,
                FOREIGN KEY (workout_id) REFERENCES workouts (id) ON DELETE CASCADE
            )
        ''')
        conn.commit()

# --- CRUD OPERATIONS ---

def add_workout(date, exercise, weight, sets_list):
    """
    Inserts a workout and its sets.
    sets_list should be a list of tuples: [(min, max), (min, max), ...]
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Insert into workouts
        cursor.execute(
            "INSERT INTO workouts (date, exercise_name, weight) VALUES (?, ?, ?)",
            (date, exercise, weight)
        )
        workout_id = cursor.lastrowid
        
        # 2. Insert each set
        for i, (r_min, r_max) in enumerate(sets_list, start=1):
            cursor.execute(
                "INSERT INTO sets (workout_id, set_number, reps_min, reps_max) VALUES (?, ?, ?, ?)",
                (workout_id, i, r_min, r_max)
            )
        conn.commit()
        return workout_id

def update_workout_weight(workout_id, new_weight):
    """Updates the weight for a specific workout entry."""
    with get_connection() as conn:
        conn.execute("UPDATE workouts SET weight = ? WHERE id = ?", (new_weight, workout_id))
        conn.commit()

def delete_workout(workout_id):
    """Deletes a workout (and its sets via CASCADE)."""
    with get_connection() as conn:
        conn.execute("DELETE FROM workouts WHERE id = ?", (workout_id,))
        conn.commit()

if __name__=='__main__':
    init_db()
