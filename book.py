# create a book program


# find book
# book name number of copies
# sort author names based on sold data

class Book:
    books = {
        "alchemist": {"book_name": "alchemist", "author": "paulo", "price": 200, "av_copies": 100, "sold": 10},
        "hgf": {"book_name": "hgf", "author": "heathen", "price": 100, "av_copies": 200, "sold": 100},
        "xyz": {"book_name": "Balch", "author": "paul", "price": 300, "av_copies": 0, "sold": 150}
    }

    def all_book_details(self):
        for book_name in self.books:
            bkname = self.books[book_name]["book_name"]
            author = self.books[book_name]["author"]
            price = self.books[book_name]["price"]
            av_stock = self.books[book_name]["av_copies"]
            sold = self.books[book_name]["sold"]
            print(f"book name : {bkname} author : {author} price : {price} available copies : {av_stock} sold : {sold}")

    def book_available(self, book_name):
        if book_name in self.books:
            return True
        else:
            return False

    def book_details(self, book_name):
        available = self.book_available(book_name)
        if available:
            print("book name", self.books[book_name]["book_name"])
            print("author", self.books[book_name]["author"])
            print("price", self.books[book_name]["price"])
            print("available copies", self.books[book_name]["av_copies"])
            print("sold", self.books[book_name]["sold"])
        else:
            print(f"The {book_name} not available here")

    def buy_book(self, **kwargs):
        book_name = kwargs["book_name"]
        no_of_copies = kwargs["no_of_copies"]
        available = self.book_available(book_name)
        print(available)
        if available:
            if self.books[book_name]["av_copies"] != 0:
                if no_of_copies > self.books[book_name]["av_copies"]:
                    var = self.books[book_name]["av_copies"]
                    print(f"our stock have only {var} left")
                else:
                    self.books[book_name]["av_copies"] -= no_of_copies
                    self.books[book_name]["sold"] += no_of_copies
            else:
                print("out of stock")
        else:
            print("out of stock")


    def author(self):
        
        author = []
        rev = sorted(self.books.items(), key=lambda x: x[1]["sold"], reverse=True)
        for value in rev:
            author.append(value[1]["author"])
        print(author)

    def add_book(self, **kwargs):
        book = kwargs["book"]
        book_name = kwargs["book_name"]
        author = kwargs["author"]
        price = kwargs["price"]
        av_stock = kwargs["av_stocks"]
        self.books[book] = {"book_name": book_name, "author": author, "price": price, "av_copies": av_stock}

    def stock_update(self, book_name, copies):
        self.books[book_name]["av_copies"] += copies

    def remove_book(self, book_name):
        del self.books[book_name]

    def update_price(self, book_name, price):
        self.books[book_name]["price"] = price


obj = Book()
while True:
    print("<====BOOK MANAGEMENT ====>")
    print("1. View All Book Available")
    print("2. Book Details")
    print("3. Add Book")
    print("4. Update price")
    print("5. Update stock")
    print("6. Remove Book")
    print("7. author name based on sold books")
    print("8. Buy Books")
    print("9. exit")
    ch = int(input("enter what you want to perform"))
    if ch == 1:
        obj.all_book_details()
    elif ch == 2:
        book = input("which book details you want")
        obj.book_details(book)
    elif ch == 3:
        book_name = input("enter the name of the book")
        author = input("author name")
        price = input("price of book")
        stock = int(input("number of stock"))
        obj.add_book(book=book_name, book_name=book_name, author=author, price=price, av_stocks=stock)
    elif ch == 4:
        book_name = input("enter the name of the book")
        price = int(input("enter the price"))
        obj.update_price(book_name, price)

    elif ch == 5:
        book = input("enter the name of book")
        stock = int(input("enter the number of copies you want to added"))
        obj.stock_update(book, stock)
    elif ch == 6:
        book = input("enter the name of book u want to delete")
        obj.remove_book(book)
    elif ch == 7:
        obj.author()
    elif ch == 8:
        book = input("book name")
        copies = int(input("no of copies needed"))
        obj.buy_book(book_name=book, no_of_copies=copies)
    else:
        break
