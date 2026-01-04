import sqlite3
import os
from datetime import datetime

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
                reps INTEGER NOT NULL,
                FOREIGN KEY (workout_id) REFERENCES workouts (id) ON DELETE CASCADE
            )
        ''')
        conn.commit()

# --- CRUD OPERATIONS ---
#HACK: This function needs to be reworked it currently doesn't work the way we want it to.
"""
Basically what it needs to do is take exercise name and count the number of sets for the exercise already executed in the past 12 hours and add 1 to it to get the set number.
The current logic is rather flawed in comparison.
Also the inputs should remove the sets_list and include reps instead.
"""
def add_workout(date, exercise, weight, sets_list):
    """
    Inserts a workout and its sets.
    sets_list should be a list of tuples: [rep1, rep2, ...]
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
        for i, r in enumerate(sets_list, start=1):
            cursor.execute(
                "INSERT INTO sets (workout_id, set_number, reps) VALUES (?, ?, ?)",
                (workout_id, i, r)
            )
        conn.commit()
        return workout_id

def get_workouts():
    """
    Get all the unique workouts in a list and return that list along with an option to insert a new workout.
    """
    with get_connection() as conn:
        cursor = conn.cursor()

    # 1. Select all distinct workouts
    cursor.execute("SELECT DISTINCT exercise_name FROM workouts")
    workouts = [row[0] for row in cursor.fetchall()]
    # 2. Add the "other" option
    workouts.append("other")
    return workouts

def get_dates(date_format= "%Y-%m-%d %H:%M:%S"):
    """
    Get the 5 most recent distinct dates from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        
    cursor.execute("SELECT date from workouts")
    datetimes = [row[0] for row in cursor.fetchall()]
    distinct_dates = set()
    for dt_str in datetimes:
        dt_obj = datetime.strptime(dt_str, date_format)
        distinct_dates.add(dt_obj.strftime("%Y-%m-%d"))
    return sorted(list(distinct_dates))
    

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
        conn.close()

def delete_workout_by_date(date):
    "Delete all workouts on a provided date"
    with get_connection() as conn:
        cursor = conn.cursor()
    cursor.execute("DELETE * from workouts WHERE date LIKE ?", (f'%{date}%',))
    conn.commit()
    conn.close()
    
if __name__=='__main__':
    init_db()
    add_workout("x", "abc", 100, [(7,12)])
    add_workout("x", "xyz", 100, [(7,12)])
    print(get_workouts())
