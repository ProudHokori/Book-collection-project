from bookdatabase import BookDB


class Book:
    """
        This class is used to represent a book and each book will have
    their own details which was used to create attributes.
    In addition, each book will have their own ID that was created
    automatically. this class is have 12 attributes as you can see below
    """

    def __init__(self, database, nameTH, nameEN, author, publisher,
                 isbn, status, category, rating, location, cover):
        """ Initialize all details of book
        :param database: object of BookDB
        :param nameTH: string of book's thai name
        :param nameEN: string of book's english name
        :param author: string of book's author
        :param publisher: string of book's publisher
        :param isbn: string of book's ISBN
        :param status: string of book's status (read/unread)
        :param category: string of book's author (many stories/once story/set story)
        :param rating: string of book's rating (out of 5)
        :param location: string of book's (shelved/unshelved)
        :param cover: string of filename of book's cover picture
        """
        # book's details
        self.__nameTH = nameTH
        self.__nameEN = nameEN
        self.__author = author
        self.__publisher = publisher
        self.__isbn = isbn
        self.__status = status
        self.__category = category
        self.__rating = rating
        self.__location = location
        self.__cover = cover

        # own book database
        self.__database = database
        # get the latest book ID from given file
        ID = BookDB.get_last_id(database)
        ID += 1  # create new book ID
        self.__id = str(ID).zfill(3)
        database.manage_id(ID)

        # add self book to database
        database.add_book(self)

    @property
    def database(self):
        """ Get or set value of book's database """
        return self.__database

    @database.setter
    def database(self, value):
        if not isinstance(value, BookDB):
            raise TypeError("database must be a BookDB object")
        self.__database = value

    @property
    def nameTH(self):
        """ Get or set value of book's nameTH """
        return self.__nameTH

    @nameTH.setter
    def nameTH(self, value):
        if not isinstance(value, str):
            raise TypeError("nameTH must be a string")
        self.__nameTH = value

    @property
    def nameEN(self):
        """ Get or set value of book's nameEN """
        return self.__nameEN

    @nameEN.setter
    def nameEN(self, value):
        if not isinstance(value, str):
            raise TypeError("nameEN must be a string")
        self.__nameEN = value

    @property
    def author(self):
        """ Get or set value of book's author """
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("author must be a string")
        self.__author = value

    @property
    def publisher(self):
        """ Get or set value of book's publisher """
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        if not isinstance(value, str):
            raise TypeError("publisher must be a string")
        self.__publisher = value

    @property
    def isbn(self):
        """ Get or set value of book's isbn """
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str):
            raise TypeError("isbn must be a string")
        self.__isbn = value

    @property
    def status(self):
        """ Get or set value of book's status """
        return self.__status

    @status.setter
    def status(self, value):
        if not isinstance(value, str):
            raise TypeError("status must be a string")
        if value not in ['read', 'unread']:
            raise ValueError("status have only 2 option "
                             ": read or unread")
        self.__status = value

    @property
    def category(self):
        """ Get or set value of book's category """
        return self.__category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        if value not in ['many stories', 'once story', 'set story']:
            raise ValueError("status have only 3 option : "
                             "many stories or once story or set story")
        self.__category = value

    @property
    def rating(self):
        """ Get or set value of book's rating """
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, str):
            raise TypeError("rating must be a string")
        self.__rating = value

    @property
    def location(self):
        """ Get or set value of book's location """
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError("location must be a string")
        if value not in ['shelved', 'unshelved']:
            raise ValueError("status have only 2 option "
                             ": shelved or unshelved")
        self.__location = value

    @property
    def cover(self):
        """ Get or set value of book's cover """
        return self.__cover

    @property
    def id(self):
        """ Get or set value of book's cover """
        return self.__id

    def __repr__(self):
        return f"{self.__id} | {self.nameEN} by {self.author}"
