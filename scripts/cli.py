import cmd
from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

class ArticleCLI(cmd.Cmd):
prompt = "Articles> "

def do_create_author(self, arg):
try:
Author(arg)
print(f"Created author: {arg}")
except Exception as e:
print(f"Error: {e}")

def do_create_magazine(self, arg):
try:
name, category = arg.split()
Magazine(name, category)
print(f"Created magazine: {name} ({category})")
except Exception as e:
print(f"Error: {e}")

def do_create_article(self, arg):
try:
title, author_id, magazine_id = arg.split("|")
author = Author.find_by_id(int(author_id))
magazine = Magazine.find_by_id(int(magazine_id))
Article(title, author, magazine)
print(f"Created article: {title}")
except Exception as e:
print(f"Error: {e}")

def do_list_authors(self, arg):
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM authors")
for row in cursor.fetchall():
print(dict(row))
conn.close()

def do_list_magazines(self, arg):
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM magazines")
for row in cursor.fetchall():
print(dict(row))
conn.close()

def do_quit(self, arg):
return True

if name == "main":
ArticleCLI().cmdloop()
