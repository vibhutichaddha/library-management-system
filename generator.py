from collections.abc import Generator
from book import Book
from utilities import (calculate_days_difference,get_current_datetime)
def overdue_books(books:list[Book],overdue_days:int=14)->Generator[Book,None,None]:
    current_date=get_current_datetime()
    for book in books:
        if (book.is_issued and book.issue_date is not None):
            days_issued=calculate_days_difference(book.issue_date,current_date)
            if days_issued>overdue_days:
                yield book