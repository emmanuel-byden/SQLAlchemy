from lib.db.connection import get_connection

def setup_database():
conn = get_connection()
with open('lib/db/schema.sql', 'r') as f:
conn.executescript(f.read())
conn.commit()
conn.close()
print("Database setup completed.")

if name == "main":
setup_database()
