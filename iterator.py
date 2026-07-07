from book import Book
class AvailableBookIterator:
    def __init__(self,books:list[Book])->None:
        self.books=[book
                    for book in books 
                    if not book.is_issued]
        self.index=0
    def __iter__(self):
        return self
    def __next__(self)->Book:
        if self.index>=len(self.books):
            raise StopIteration
        book=self.books[self.index]
        self.index+=1
        return book