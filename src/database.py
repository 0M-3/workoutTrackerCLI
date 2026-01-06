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
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS EXERCISES (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                EXERCISE_NAME TEXT NOT NULL UNIQUE,
                DATE TIMESTAMP NOT NULL
            )
        ''')
        # Table for general workout info
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS WORKOUTS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DATE TIMESTAMP NOT NULL,
                EXERCISE_ID INTEGER NOT NULL,
                FOREIGN KEY (EXERCISE_ID) REFERENCES EXERCISES (ID) ON DELETE CASCADE
            )
        ''')
        
        # Table for specific sets (One-to-Many relationship)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SETS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                WORKOUT_ID INTEGER NOT NULL,
                SET_NUMBER INTEGER NOT NULL,
                REPS INTEGER NOT NULL,
                WEIGHT INTEGER NOT NULL,
                DATE TIMESTAMP NOT NULL,
                FOREIGN KEY (WORKOUT_ID) REFERENCES WORKOUTS (ID) ON DELETE CASCADE,
                UNIQUE (WORKOUT_ID, SET_NUMBER)
            )
        ''')

        conn.commit()

# --- CRUD OPERATIONS ---
#FIX: Make sure to debug the logic below
"""
Basically what it needs to do is take exercise name and count the number of sets for the exercise already executed in the past 12 hours and add 1 to it to get the set number.
The current logic is rather flawed in comparison.
Also the inputs should remove the sets_list and include reps instead.
"""
def add_workout(date: datetime, exercise: str, weight: int, reps: int):
    """
    Inserts a workout and its sets.
    """
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO EXERCISES (EXERCISE_NAME, DATE)
            VALUES (?, ?)
            ON CONFLICT (EXERCISE_NAME) DO NOTHING
        """, (exercise, date))

        cursor.execute("SELECT ID FROM EXERCISES WHERE EXERCISE_NAME = ?", [exercise])
        exercise_row = cursor.fetchone()
        if exercise_row:
            exercise_id = exercise_row[0]

        
        # 1. Insert into workouts
        cursor.execute("""
            INSERT INTO WORKOUTS (DATE, EXERCISE_ID)
            SELECT ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM WORKOUTS
                WHERE date(DATE) = date(?)
                AND EXERCISE_ID = (?)
            )
            """,
            (date, exercise_id, date, exercise_id))
        cursor.execute(
            "SELECT ID FROM WORKOUTS WHERE EXERCISE_ID = ?",
            (exercise_id,))
        workout_id = cursor.fetchone()

        # 2. Insert each set
        cursor.execute("SELECT COUNT(*) FROM SETS WHERE WORKOUT_ID = ?", (workout_id))
        set_row= cursor.fetchone()
        if set_row:
            set_number = set_row[0]
        cursor.execute("""
            INSERT INTO SETS (WORKOUT_ID, SET_NUMBER, REPS, WEIGHT, DATE)
            VALUES (?, ?, ?, ?, ?)
        """, (workout_id[0], set_number+1, reps, weight, date))
        conn.commit()

def get_workouts():
    """
    Get all the unique workouts in a list and return that list along with an option to insert a new workout.
    """
    with get_connection() as conn:
        cursor = conn.cursor()

    # 1. Select all distinct workouts
    cursor.execute("SELECT DISTINCT EXERCISE_NAME FROM EXERCISES")
    workouts = [row[0] for row in cursor.fetchall()]
    # 2. Add the "other" option
    # workouts.append("other")
    return workouts

def get_dates(date_format= "%Y-%m-%d"):
    """
    Get the 5 most recent distinct dates from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        
    cursor.execute("SELECT date(DATE) FROM WORKOUTS")
    datetimes = [row[0] for row in cursor.fetchall()]
    distinct_dates = set()
    for dt_str in datetimes:
        dt_obj = datetime.strptime(dt_str, date_format)
        distinct_dates.add(dt_obj.strftime("%Y-%m-%d"))
    return sorted(list(distinct_dates))
    

def update_workout_weight(workout_id, new_weight):
    """Updates the weight for a specific workout entry."""
    with get_connection() as conn:
        conn.execute("UPDATE WORKOUTS SET WEIGHT = ? WHERE ID = ?", (new_weight, workout_id))
        conn.commit()

def delete_workout(workout_id):
    """Deletes a workout (and its sets via CASCADE)."""
    with get_connection() as conn:
        conn.execute("DELETE FROM WORKOUTS WHERE ID = ?", (workout_id,))
        conn.commit()
        conn.close()

def delete_workout_by_date(date):
    "Delete all workouts on a provided date"
    with get_connection() as conn:
        cursor = conn.cursor()
    cursor.execute("DELETE FROM WORKOUTS WHERE date(DATE) =?", (f'%{date}%',))
    conn.commit()
    conn.close()
    
if __name__=='__main__':
    init_db()
    add_workout("x", "abc", 100, 10)
    add_workout("x", "xyz", 100, 10)
    print(get_workouts())
