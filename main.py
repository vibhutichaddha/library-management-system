from library import Library
def display_books(books:list)->None:
    if not books:
        print("No books found")
        return
    for book in books:
        print(book)
def main()->None:
    library=Library()
    while True:
        print("\n==== Library Management System ====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Display Available Books")
        print("8. Display Issued Books")
        print("9. Display overdue books")
        print("10. Add member")
        print("11. Exit")
        choice=input("Enter your choice:").strip()
        if choice=="1":
            title=input("Enter book name:").strip()
            author=input("Enter author name:").strip()
            print(library.add_book(title,author))
        elif choice=="2":
            title=input("Enter book name:").strip()
            print(library.remove_book(title))
        elif choice=="3":
            title=input("Enter book name:").strip()
            books=library.search_by_title(title)
            display_books(books)
        elif choice=="4":
            author=input("Enter author name:").strip()
            books=library.search_by_author(author)
            display_books(books)
        elif choice=="5":
            title=input("Enter book title:").strip()
            try:
                member_id=int(input("Enter member ID:"))
            except ValueError:
                print("Member ID must be a number")
                continue
            print(library.issue_book(title,member_id))
        elif choice=="6":
            title=input("Enter book title:").strip()
            try:
                member_id=int(input("Enter member ID:"))
            except ValueError:
                print("Member ID must be a number")
                continue
            print(library.return_book(title,member_id))
        elif choice=="7":
            library.display_available_books()
        elif choice=="8":
            library.display_issued_books()
        elif choice=="9":
            library.display_overdue_books()
        elif choice=="10":
            name=input("Enter member name:").strip()
            try:
                member_id=int(input("Enter member id:"))
            except ValueError:
                print("Member ID must be a number")
                continue
            print(library.add_member(name,member_id))
        elif choice=="11":
            print("Exiting Library Management System")
            break
        else:
            print("Invalid choice. Please try again")
if __name__=="__main__":
    main()