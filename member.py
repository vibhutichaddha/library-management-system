from utilities import normalize_text
class Member:
    def __init__(self,name:str,member_id:int)->None:
        self.name=normalize_text(name)
        self.member_id=member_id
        self.issued_books:list[str]=[]
    def __str__(self)->str:
        return(f"Member ID:{self.member_id},"f"Name:{self.name}")