from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def debug():
print("Interactive debugging session")
author = Author.find_by_id(1)
print(f"Author: {author.name}")
print(f"Articles: {author.articles()}")
print(f"Magazines: {author.magazines()}")
print(f"Topic Areas: {author.topic_areas()}")

magazine = Magazine.find_by_id(1)
print(f"\nMagazine: {magazine.name}")
print(f"Articles: {magazine.articles()}")
print(f"Contributors: {magazine.contributors()}")
print(f"Article Titles: {magazine.article_titles()}")

if name == "main":
debug()
