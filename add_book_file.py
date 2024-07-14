def add_book():
    
    title=input("Enter title of the book: ")
    author=list(input("Enter name of author\n(seperated by comma(,) for multiple authors): ").split(","))
    for i in range(len(author)):
        author[i]=author[i].strip()
    
    while True:
        isbn=int(input("Enter ISBN: "))
        try:
            isbn = int(isbn)
            break
        except ValueError:
            print("That's not a valid ISBN. Please try again.")
    
    while True:
        year=input("Enter publishing year: ")
        try:
            year = int(year)
            break
        except ValueError:
            print("That's not a valid year. Please try again.")

    while True:
        price=input("Enter Price: ")
        try:
            price = float(price)
            break
        except ValueError:
            print("That's not a valid price. Please try again.")
    
    
    while True:
        quantity=(input("Enter quantity: "))
        try:
            quantity = int(quantity)
            break
        except ValueError:
            print("That's not a valid quantity. Please try again.")
    

    book={
        "title":title,
        "author":author,
        "isbn": isbn,
        "year":year,
        "price":price,
        "quantity":quantity
        }
    with open("book_list.csv",'a') as fp:
        
        au=','.join(book['author'])
        line=f"{book['title']},\"{au}\",{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
        fp.write(line)

    print("Book added successfully!")