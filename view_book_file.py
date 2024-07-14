
def view_book():
    import main
    library = main.restore()
    for i,book in enumerate(library):
        #print(i,book)
        print(f"{i+1}. Title: {book['title']}\n{' '*(len(str(i))+2)}Author(s): {', '.join(book['author'])}\n{' '*(len(str(i))+2)}ISBN: {book['isbn']}\n{' '*(len(str(i))+2)}Year: {book['year']}\n{' '*(len(str(i))+2)}Price: {book['price']}\n{' '*(len(str(i))+2)}Quantity: {book['quantity']}")
