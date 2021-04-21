import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Steven", "Erikson")
author_repository.save(author_1)

book_1 = Book("Gardens of the Moon", "Sci Fi", author_1)
book_repository.save(book_1)

book_2 = Book("Dead house gates", "Sci Fi", author_1)
book_repository.save(book_2)

pdb.set_trace()


