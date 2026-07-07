def reverse_string(text: str)->str:
    return text[::-1]
def to_uppercase(text: str)->str:
    return text.upper()
def to_lowercase(text: str)->str:
    return text.lower()
def is_palindrome(text: str)->bool:
    return text==text[::-1]