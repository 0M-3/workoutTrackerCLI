 # CLI Workout Tracker

A snappy, terminal-based application to track your gym progress. This tool allows you to log exercises, manage set ranges (e.g., 8-12 reps), and visualize your strength gains directly in your CLI using SQLite and Plotext.

## Features

* **Intuitive CLI:** Built with `Textual` for a fast, command-driven experience.
* **Flexible Rep Tracking:** Supports rep ranges (e.g., 8-12) rather than just single numbers.
* **SQLite Backend:** All data is stored locally in a relational database with a one-to-many relationship between workouts and sets.
* **Terminal Visuals:** Generate bar charts of your progress without leaving the terminal.
* **Automatic Volume Calculation:** Understand your total workload per session using weighted averages of rep ranges.

---

## Roadmap

### Phase 1: Data & Logic Foundation

* [x] **Database Schema:** Design `workouts` and `sets` tables with Foreign Key constraints.
* [x] **CRUD Operations:** Basic functions for inserting, updating, and deleting entries.
* [ ] **Rep Parser:** Develop a robust utility to split "min-max" strings into integers.
* [ ] **Volume Engine:** Implement logic to calculate .

### Phase 2: CLI Experience

* [x] **Command Architecture:** Set up `Textual` screens for `add`, `view`, `delete`, and `visualize`.
* [ ] **Smart Prompts:** Implement interactive fallbacks so the app asks for input if flags are missing.
* [ ] **Rich Formatting:** Use the `Rich` library to render exercise history in beautiful, color-coded tables.
* [ ] **Input Validation:** Ensure weight and rep inputs are numeric and logically sound.

### Phase 3: Analytics & Visualization

* [ ] **Plotext Integration:** Create bar charts for weight progression over time.
* [ ] **Exercise Filtering:** Add the ability to view progress for a specific exercise (e.g., `workout graph --exercise "Squat"`).
* [ ] **Summary Statistics:** Display "Personal Bests" (PBs) and total tonnage moved per week.

### Phase 4: Advanced Features

* [ ] **RPE Tracking:** Add a column for Rate of Perceived Exertion (1-10 scale).
* [ ] **Data Export:** Create a command to dump the SQLite database to a CSV or JSON file.
* [ ] **Rest Timer:** Build a simple CLI-based countdown timer to use between sets.
* [ ] **Shell Completion:** Generate auto-completion scripts for Bash/Zsh/Fish users.

---
