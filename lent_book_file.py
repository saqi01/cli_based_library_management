def lent_book():
    import search_book_file
    search_book_file.search_book()
    import main
    library=main.restore()

    while True:
        x=input("Enter number to lend: ")
        try:
            x = int(x)
            break
        except :
            print("That's not a valid number. Please try again.")
    if library[x-1]['quantity']>0:
        while True:
            name=input("Enter your name: ")
            try:
                if name!="":
                    break
            except :
                print("That's not a valid name. Please try again.")
        library[x-1]['quantity']-=1
        main.upgrade()
        main.restore()
        lb=main.restore_lb()
      
  
        isbns=[list(d.values())[1] for d in lb]
        if library[x-1]["isbn"] in isbns:
            lb[isbns.index(library[x-1]["isbn"])]["name"].append(name)
            main.upgrade_lb()
        else:
            with open("lend_book.csv",'a') as fp:
                l=f"{library[x-1]['title']},{library[x-1]['isbn']},\"{name}\"\n"
                fp.write(l)

        print("Book lent to",name)
    else:
        print("Book not available to lend")