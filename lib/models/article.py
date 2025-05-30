from lib.db.connection import get_connection
from .author import Author
from .magazine import Magazine

class Article:
def init(self, title, author, magazine, id=None):
self._id = id
self._title = None
self._author = None
self._magazine = None
self.title = title
self.author = author
self.magazine = magazine
if id is None:
self._save()

@property
def id(self):
return self._id

@property
def title(self):
return self._title

@title.setter
def title(self, value):
if not isinstance(value, str) or not value.strip():
raise ValueError("Title must be a non-empty string")
self._title = value

@property
def author(self):
return self._author

@author.setter
def author(self, value):
if not isinstance(value, Author):
raise ValueError("Author must be an instance of Author")
self._author = value

@property
def magazine(self):
return self._magazine

@magazine.setter
def magazine(self, value):
if not isinstance(value, Magazine):
raise ValueError("Magazine must be an instance of Magazine")
self._magazine = value

def _save(self):
conn = get_connection()
cursor = conn.cursor()
try:
conn.execute("BEGIN TRANSACTION")
cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) RETURNING id",
(self.title, self.author.id, self.magazine.id))
self._id = cursor.fetchone()['id']
conn.execute("COMMIT")
except Exception as e:
conn.execute("ROLLBACK")
raise Exception(f"Error saving article: {e}")
finally:
conn.close()

@classmethod
def find_by_id(cls, id):
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
row = cursor.fetchone()
conn.close()
if row:
author = Author.find_by_id(row['author_id'])
magazine = Magazine.find_by_id(row['magazine_id'])
return cls(row['title'], author, magazine, row['id'])
return None

@classmethod
def find_by_title(cls, title):
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
row = cursor.fetchone()
conn.close()
if row:
author = Author.find_by_id(row['author_id'])
magazine = Magazine.find_by_id(row['magazine_id'])
return cls(row['title'], author, magazine, row['id'])
return None
