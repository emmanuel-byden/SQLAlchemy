import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
from scripts.setup_db import setup_database
setup_database()
seed_database()

def test_article_creation():
author = Author.find_by_id(1)
magazine = Magazine.find_by_id(1)
article = Article("Test Article", author, magazine)
assert article.id is not None
assert article.title == "Test Article"
assert article.author.id == author.id
assert article.magazine.id == magazine.id

def test_article_validation():
author = Author.find_by_id(1)
magazine = Magazine.find_by_id(1)
with pytest.raises(ValueError):
Article("", author, magazine)
with pytest.raises(ValueError):
Article("Title", None, magazine)
with pytest.raises(ValueError):
Article("Title", author, None)

def test_find_by_id():
article = Article.find_by_id(1)
assert article.title == "Tech Trends 2025"
assert article.author.name == "Jane Doe"
assert article.magazine.name == "Tech Today"

def test_find_by_title():
article = Article.find_by_title("Tech Trends 2025")
assert article.id == 1
assert article.author.name == "Jane Doe"
