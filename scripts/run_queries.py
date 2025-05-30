from lib.db.connection import get_connection

def run_example_queries():
conn = get_connection()
cursor = conn.cursor()

print("Magazines with at least 2 different authors:")
cursor.execute("""
SELECT m.name, COUNT(DISTINCT a.author_id) as author_count
FROM magazines m
JOIN articles a ON m.id = a.magazine_id
GROUP BY m.id
HAVING author_count >= 2
""")
print([dict(row) for row in cursor.fetchall()])

print("\nArticle count per magazine:")
cursor.execute("""
SELECT m.name, COUNT(a.id) as article_count
FROM magazines m
LEFT JOIN articles a ON m.id = a.magazine_id
GROUP BY m.id
""")
print([dict(row) for row in cursor.fetchall()])

print("\nAuthor with the most articles:")
cursor.execute("""
SELECT au.name, COUNT(a.id) as article_count
FROM authors au
JOIN articles a ON au.id = a.author_id
GROUP BY au.id
ORDER BY article_count DESC
LIMIT 1
""")
print([dict(row) for row in cursor.fetchall()])

conn.close()

if name == "main":
run_example_queries()
