def normalize_text(text:str)->str:
    return"".join(text.strip().title().split())
def normalize_for_search(text:str)->str:
    return"".join(text.strip().lower().split())