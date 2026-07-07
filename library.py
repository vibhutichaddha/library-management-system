from book import Book
from decorators import execution_time, log_operation
from generator import overdue_books
from iterator import AvailableBookIterator 
from member import Member
from utilities import (calculate_days_difference,calculate_fine,get_current_datetime,normalize_for_search)
class Library:
    def __init__(self)->None:
        self.books:list[Book]=[]
        self.members:list[Member]=[]
    @log_operation
    def add_book(self,title:str,author:str)->str:
        search_title=normalize_for_search(title)
        search_author=normalize_for_search(author)
        for book in self.books:
            if(
                normalize_for_search(book.title)==search_title and normalize_for_search(book.author)==search_author
            ):
                return "Book already exists:"
        self.books.append(Book(title,author))
        return "Book added successfully"
    @log_operation
    def remove_book(self,title:str)->str:
        search_title=normalize_for_search(title)
        for book in self.books:
            if(normalize_for_search(book.title)==search_title):
                if book.is_issued:
                    return "Issued book cannot be removed"
                self.books.remove(book)
                return "Book removed successfully"
            return "Book not found"
    @execution_time
    def search_by_title(self,title:str)->list[Book]:
        search_title=normalize_for_search(title)
        print("BOOKS IN LIST:",len(self.books))
        for book in self.books:
            print("SEARCHING:",normalize_for_search(book.title),"FOR:",search_title)
        return [book 
                for book in self.books 
                if search_title in normalize_for_search(book.title)
                ]
    @execution_time
    def search_by_author(self,author:str)->list[Book]:
        search_author=normalize_for_search(author)
        return[book
               for book in self.books
               if search_author in normalize_for_search(book.author)]
    @log_operation
    def add_member(self,name:str,member_id:int)->str:
        for member in self.members:
            if member.member_id==member_id:
                return "Member ID already exists"
        self.members.append(Member(name,member_id))
        return "Member added successfully"
    @log_operation
    def issue_book(self, title:str,member_id:int)->str:
        search_title=normalize_for_search(title)
        book=next((book
                   for book in self.books
                   if normalize_for_search(book.title)==search_title),None)
        member=next((member
                     for member in self.members 
                     if member.member_id==member_id),None)
        if book is None:
            return "Book not found"
        if member is None:
            return "Member not found"
        if book.is_issued:
            return "Book is already issued"
        book.is_issued=True
        book.issue_date=get_current_datetime()
        member.issued_books.append(book.title)
        return "Book issued successfully"
    @log_operation
    def return_book(self,title:str,member_id:int)->str:
        search_title=normalize_for_search(title)
        member=next((member 
                     for member in self.members
                     if member.member_id==member_id),None)
        if member is None:
            return "Member not found"
        for book in self.books:
            if(normalize_for_search(book.title)==search_title):
                if not book.is_issued:
                    print("Book is not issued")
                if book.title not in member.issued_books:
                    return("Book was not issued to this member")
                overdue_days=0
                if book.issue_date is not None:
                    days_issued=(calculate_days_difference(book.issue_date,get_current_datetime()))
                    overdue_days=max(0,days_issued-14)
                fine=calculate_fine(overdue_days)
                book.is_issued=False
                book.issue_date=None
            member.issued_books.remove(book.title)
            return ("Book returned successfully." f"Fine: Rs.{fine:.2f}")
        return "Book not found"
    def display_available_books(self)->None:
        book_iterator=AvailableBookIterator(self.books)
        books_found=False
        for book in book_iterator:
            books_found=True
            print(book)
        if not books_found:
            print("No available books")
    def display_issued_books(self)->None:
        issued_books=[book
                      for book in self.books
                      if book.is_issued]
        if not issued_books:
            print("No issued books")
            return
        for book in issued_books:
            print(book)
    def display_overdue_books(self)->None:
        books_found=False
        for book in overdue_books(self.books):
            books_found=True
            days_issued=calculate_days_difference(book.issue_date,get_current_datetime)
            overdue_days=days_issued-14
            fine=calculate_fine(overdue_days)
            print(book)
            print(f"Overdue days:{overdue_days}")
            print(f"Fine:Rs.{fine:.2f}")
        if not books_found:
            print("No overdue books")