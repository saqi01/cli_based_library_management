def remove_book():
    import main
    library=main.restore()
    while True:
        k=input("Enter book name to remove: ")
        try:
            if k!="":
                break
        except:
            print("That's not a valid name. Please try again.")
    k=k.lower()
    found=False
    for i,book in enumerate(library):
        n=book["title"].lower()
    

        if k in n:
            found=True
            print(f"{i+1}. Title: {book['title']}\n{' '*(len(str(i))+2)}Author(s): {', '.join(book['author'])}\n{' '*(len(str(i))+2)}ISBN: {book['isbn']}\n{' '*(len(str(i))+2)}Year: {book['year']}\n{' '*(len(str(i))+2)}Price: {book['price']}\n{' '*(len(str(i))+2)}Quantity: {book['quantity']}")
        
    if not found:
        print("No match Found!!")
        return
    
    while True:
        r=input("Enter number to lend: ")
        try:
            r = int(r)
            break
        except :
            print("That's not a valid number. Please try again.")

    with open("book_list.csv",'r+') as fp:
        line=fp.readlines()
        line.pop(r-1)
        fp.seek(0)
        for l in line:  
            fp.writelines(l)  
        fp.truncate()
    print("Book removed Successfully!")