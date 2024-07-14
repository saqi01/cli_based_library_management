def return_book():
    import search_book_file
    x=search_book_file.search_book()
    import main
    library=main.restore()

    while True:
        x=input("Enter number to return: ")
        try:
            x = int(x)
            break
        except :
            print("That's not a valid number. Please try again.")
    while True:
        name=input("Enter your name: ")
        try:
            if name!="":
                break
        except:
            print("That's not a valid name. Please try again.")
    
 
    main.restore()
    lb=main.restore_lb()

    for a in lb:
        if a["isbn"]==library[x-1]['isbn']:
            if name in a["name"]:
                a["name"].remove(name)
                library[x-1]['quantity']+=1
                main.upgrade()
            else:
                print("Name not found")
                return
            main.upgrade_lb()
            print("Book returned successfully!")
            return
    print("Book not found")