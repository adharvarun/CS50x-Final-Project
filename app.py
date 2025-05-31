from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)
DB_NAME = "habits.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER,
                date TEXT,
                FOREIGN KEY (habit_id) REFERENCES habits(id)
            )
        ''')
        conn.commit()

init_db()

@app.route('/')
def index():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM habits")
        habits = c.fetchall()

        habit_data = []
        for habit in habits:
            c.execute("SELECT date FROM completions WHERE habit_id = ?", (habit[0],))
            dates = [row[0] for row in c.fetchall()]
            habit_data.append((habit[0], habit[1], dates))

    return render_template('index.html', habits=habit_data, today=str(date.today()))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        with sqlite3.connect(DB_NAME) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO habits (name) VALUES (?)", (name,))
            conn.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/complete/<int:habit_id>')
def complete(habit_id):
    today = str(date.today())
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO completions (habit_id, date) VALUES (?, ?)", (habit_id, today))
        conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)