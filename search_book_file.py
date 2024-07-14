def search_book():
    import main
    library=main.restore()
    k=input("Enter Title or ISBN: ")
    try:
        k=int(k)
        found=False
        for i,book in enumerate(library):
            if k == book["isbn"]:
                found=True
                print(f"{i+1}. Title: {book['title']}\n{' '*(len(str(i))+2)}Author(s): {', '.join(book['author'])}\n{' '*(len(str(i))+2)}ISBN: {book['isbn']}\n{' '*(len(str(i))+2)}Year: {book['year']}\n{' '*(len(str(i))+2)}Price: {book['price']}\n{' '*(len(str(i))+2)}Quantity: {book['quantity']}")
        if not found:
            print("No Match Found!")
    except :
        k=k.lower()
        found=False
        for i,book in enumerate(library):
            n=book["title"].lower()
            
            if k in n:
                found=True
                print(f"{i+1}. Title: {book['title']}\n{' '*(len(str(i))+2)}Author(s): {', '.join(book['author'])}\n{' '*(len(str(i))+2)}ISBN: {book['isbn']}\n{' '*(len(str(i))+2)}Year: {book['year']}\n{' '*(len(str(i))+2)}Price: {book['price']}\n{' '*(len(str(i))+2)}Quantity: {book['quantity']}")
        if not found:
            print("No match Found!!")