def search_author():
    import main
    library=main.restore()
    found=False
    k=input("Enter full name of author: ").strip().lower()
    for i,book in enumerate(library):
        a=book["author"]
        if k in a:
            found=True
            print(f"{i+1}. Title: {book['title']}\n{' '*(len(str(i))+2)}Author(s): {', '.join(book['author'])}\n{' '*(len(str(i))+2)}ISBN: {book['isbn']}\n{' '*(len(str(i))+2)}Year: {book['year']}\n{' '*(len(str(i))+2)}Price: {book['price']}\n{' '*(len(str(i))+2)}Quantity: {book['quantity']}")
    if not found:
        print("NO Author Found!")