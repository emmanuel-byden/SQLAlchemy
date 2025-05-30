import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_database

@pytest.fixture(autouse=True)
def setup_database():
from scripts.setup_db import setup_database
setup_database()
seed_database()

def test_author_creation():
author = Author("Test Author")
assert author.id is not None
assert author.name == "Test Author"

def test_author_name_validation():
with pytest.raises(ValueError):
Author("")

def test_find_by_id():
author = Author.find_by_id(1)
assert author.name == "Jane Doe"

def test_articles():
author = Author.find_by_id(1)
articles = author.articles()
assert len(articles) == 2
assert articles[0]['title'] == "Tech Trends 2025"

def test_magazines():
author = Author.find_by_id(1)
magazines = author.magazines()
assert len(magazines) == 1
assert magazines[0]['name'] == "Tech Today"

def test_add_article():
author = Author.find_by_id(1)
magazine = Magazine.find_by_id(1)
article = author.add_article(magazine, "New Article")
assert article.title == "New Article"
assert article.author.id == author.id
assert article.magazine.id == magazine.id

def test_topic_areas():
author = Author.find_by_id(1)
topics = author.topic_areas()
assert "Technology" in topics
