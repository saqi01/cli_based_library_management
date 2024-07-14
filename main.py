import add_book_file
import view_book_file
import search_book_file
import search_author_file
import remove_book_file
import lent_book_file
import return_book_file

library=[]
lb=[]

def restore():
    library.clear()
    with open("book_list.csv","r") as fp:
        for line in fp:
            t,*a,i,y,p,q=line.split(",")
            
            a[0]=a[0].lstrip('"')
            a[-1]=a[-1].rstrip('"')

            book={
                "title":t,
                "author":a,
                "isbn": int(i),
                "year":y,
                "price":float(p),
                "quantity":int(q)
            }
            library.append(book)
    return library

def restore_lb():
    lb.clear()
    with open("lend_book.csv","a") as fp:
        with open("lend_book.csv","r") as fp:
            # if len(fp.read())!=0:
            c=fp.read()
            if len(c)>0:
                fp.seek(0)
                for line in fp:
                    line=line.strip()
                    t,i,*n=line.split(",")
                    n[0]=n[0].lstrip('"')
                    n[-1]=n[-1].rstrip('"\n')
                    book={
                        "title":t,
                        "isbn": int(i),
                        "name":list(n)
                    }
                    lb.append(book)
    return lb


def upgrade():
    with open("book_list.csv",'r+') as fp:
        fp.seek(0)
        for book in library:
            au=','.join(book['author'])
            line=f"{book['title']},\"{au}\",{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            fp.write(line)
        fp.truncate()

def upgrade_lb():
    with open("lend_book.csv",'r+') as fp:
        fp.seek(0)
        for book in lb:
            au=','.join(book['name'])
            line=f"{book['title']},{book['isbn']},\"{au}\"\n"
            fp.write(line)
        fp.truncate()

print("Welcome!")

menu_text = """
Your options:
1. Add Book
2. View All Book
3. Search Book
4. Search Author
5. Remove Book
6. Lend Book
7. Return Book
0. Exit
"""
while True:
    print(menu_text)
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book_file.add_book()
    elif choice == "2":
        view_book_file.view_book()
    elif choice == "3":
        search_book_file.search_book()
    elif choice == "4":
        search_author_file.search_author()
    elif choice == "5":
        remove_book_file.remove_book()
    elif choice == "6":
        lent_book_file.lent_book()
    elif choice == "7":
        return_book_file.return_book()
    elif choice == "0":
        break
    else:
        print("Wrong Choice!")