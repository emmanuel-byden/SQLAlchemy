from lib.db.connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.execute("BEGIN TRANSACTION")
        # Clear existing data
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        cursor.execute("DELETE FROM sqlite_sequence")  # Reset auto-increment IDs
        # Insert seed data
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Doe",))
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Smith",))
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Alice Johnson",))
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Today", "Technology"))
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Fashion Weekly", "Fashion"))
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Matters", "Health"))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Tech Trends 2025", 1, 1))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("AI Revolution", 1, 1))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Summer Styles", 2, 2))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Healthy Eating", 3, 3))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Fitness Tips", 3, 3))
        conn.commit()
        print("Database seeded successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()
