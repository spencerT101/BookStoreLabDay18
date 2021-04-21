from db.run_sql import run_sql
from model.author import Author
from model.book import Book


def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)