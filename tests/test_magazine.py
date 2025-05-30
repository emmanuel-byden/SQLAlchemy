import pytest
from lib.models.magazine import Magazine
from lib.db.seed import seed_database
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_database():
    from scripts.setup_db import setup_database
    # Clear database
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM sqlite_sequence")
    conn.commit()
    conn.close()
    # Set up and seed
    setup_database()
    seed_database()

def test_magazine_creation():
    magazine = Magazine("Test Mag", "Test Category")
    assert magazine.id is not None
    assert magazine.name == "Test Mag"
    assert magazine.category == "Test Category"

def test_magazine_validation():
    with pytest.raises(ValueError):
        Magazine("", "Category")
    with pytest.raises(ValueError):
        Magazine("Name", "")

def test_find_by_id():
    magazine = Magazine.find_by_id(1)
    assert magazine.name == "Tech Today"

def test_find_by_name():
    magazine = Magazine.find_by_name("Tech Today")
    assert magazine.id == 1

def test_articles():
    magazine = Magazine.find_by_id(1)
    articles = magazine.articles()
    assert len(articles) == 2
    assert articles[0]['title'] == "Tech Trends 2025"

def test_contributors():
    magazine = Magazine.find_by_id(1)
    contributors = magazine.contributors()
    assert len(contributors) == 1
    assert contributors[0]['name'] == "Jane Doe"

def test_article_titles():
    magazine = Magazine.find_by_id(1)
    titles = magazine.article_titles()
    assert "Tech Trends 2025" in titles
    assert "AI Revolution" in titles

def test_top_publisher():
    magazine = Magazine.top_publisher()
    assert magazine.name == "Tech Today"
