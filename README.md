# Habit Tracker  
#### Video Demo: [https://youtu.be/vBavjAye6Pw](https://youtu.be/vBavjAye6Pw)

#### Description:

This was my final project for the CS50x Course by Harvard.

![certificate](certificate.jpg)

Habit Tracker is a **web-based application** developed as the final project for Harvard's [CS50x](https://cs50.harvard.edu/x/) course. The app helps users build positive daily habits by providing an intuitive interface where they can create, track, and maintain progress on their goals.

The project was designed and implemented using **Python (Flask framework)** for the backend, **SQLite** for data persistence, and standard web technologies such as **HTML** and **CSS** for the frontend. It is intentionally lightweight, focusing on core functionality and usability while maintaining a clean and responsive user experience.

---

### Motivation

The idea behind building a habit tracker stems from the understanding that forming consistent habits is a key component of personal growth. Many people struggle with sticking to their goals due to the lack of visual feedback and accountability. I wanted to create a simple tool that anyone can use to:

- define their personal habits  
- track whether they complete them each day  
- visualize their overall progress

This project provided me with the opportunity to apply what I learned in CS50x about databases, server-side programming, and full-stack web development while building something meaningful.

---

### Core Features

✅ **Add Daily Habits**  
Users can add new habits they want to track. These can be simple actions such as "Drink 8 glasses of water", "Exercise for 30 minutes", or "Read 10 pages".

✅ **View and Manage Habits**  
All habits are displayed in a neat list format. The app is optimized for both desktop and mobile views to ensure accessibility.

✅ **Mark Habits as Completed**  
Each habit has a "Mark as Done" button, allowing users to log their daily completion. The interface automatically updates to reflect this.

✅ **Persistent Data Storage**  
Habit data, including daily completion status, is stored in an SQLite database, ensuring that data is preserved across browser sessions.

✅ **Progress Tracking**  
Users can visually track which habits they have completed for the current day and easily identify gaps or consistency in their routines.

---

### Technologies Used

#### Backend

- Python  
- Flask  
- SQLite  

#### Frontend

- HTML5  
- CSS3  

---

### Future Improvements

If I were to continue developing this project beyond CS50x, I would consider adding:

- **User Authentication:** Allow multiple users to create accounts and track their own set of habits  
- **Habit Streaks:** Display a streak counter for each habit to motivate consistency  
- **Historical Reporting:** Provide users with a detailed history of their habit completion across weeks or months  
- **Notifications / Reminders:** Integrate email or browser notifications to remind users to complete their habits  
- **Progress Graphs:** Add visual charts or graphs to track progress over time  

---

### Installation and Usage Instructions

1. Clone the repository  
```git clone <repository-url>```
```cd habit-tracker```

2. Set up a virtual environment and install dependencies  
```python3 -m venv venv```  
```source venv/bin/activate```  
```pip install -r requirements.txt```

3. Run the Flask app  
```flask run```

4. Open your browser and navigate to ```http://127.0.0.1:5000``` to start using the Habit Tracker.

---

### Conclusion

This project was a valuable exercise in **end-to-end web development**, incorporating skills such as database design, server-side scripting, routing, and front-end design. More importantly, it reinforced the concept that **software can improve daily life**, even with a simple tool like a habit tracker.

I hope that this project inspires others to think about the small ways technology can help us build better routines and lead more productive lives.
