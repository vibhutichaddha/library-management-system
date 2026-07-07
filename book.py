from datetime import datetime
from typing import Optional
from utilities import normalize_text
class Book:
    def __init__(self, title:str, author:str)->None:
        self.title=normalize_text(title)
        self.author=normalize_text(author)
        self.is_issued=False
        self.issue_date:Optional[datetime]=None
    def __str__(self)->str:
        status=("Issued"
                if self.is_issued
                else"Available")
        return(f"Title:{self.title},"
               f"Author:{self.author},"
               f"Status:{status}")