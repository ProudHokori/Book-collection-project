from bookdatabase import BookDB


class Book:
    ID = BookDB.get_last_id("fileID.txt")

    def __init__(self, database, nameTH, nameEN, author, publisher,
                 isbn, status, category, rating, location, cover):
        self.database = database
        self.nameTH = nameTH
        self.nameEN = nameEN
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.status = status
        self.category = category
        self.rating = rating
        self.location = location
        self.cover = cover
        Book.ID += 1
        self.id = str(Book.ID).zfill(3)
        database.manage_id("fileID.txt", Book.ID)
        database.add_book(self)

    def __repr__(self):
        return f"{self.id} | {self.nameEN} by {self.author}"
