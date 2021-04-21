from db.run_sql import run_sql
from model.author import Author
from model.book import Book

import repositories.author_repository as author_repository


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)