import json


class BookDB:
    """
        This class is used to manage all about data file in this app.
    and have two attributes that are
    filename : string of name of json filename that store all Book details
    fileID : string of book ID's txt filename that store all number of Book's ID
    book_list : a list of Book object
    """

    def __init__(self, filename='fileBook.json', fileID='fileID.txt'):
        """ Initialize filename of database to store all book data
        and initialize list of book
        :param filename: string of book's json filename
        :param fileID: string of book ID's txt filename
        """
        self.__filename = filename
        self.__fileID = fileID
        self.book_list = []

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        if value[-5:] != '.json':
            raise ValueError('filename must be a json file')
        self.__filename = value

    @property
    def fileID(self):
        return self.__fileID

    @fileID.setter
    def fileID(self, value):
        if value[-4:] != '.txt':
            raise ValueError('fileID must be a txt file')
        self.__fileID = value

    def add_book(self, book):
        """ Use to add a new book data to json database file
        :param book: object of Book class
        """
        # append book object in list
        self.book_list.append(book)
        # create nested dictionary of new book
        new_book = {
            book.id: {
                "nameTH": book.nameTH,
                "nameEN": book.nameEN,
                "author": book.author,
                "publisher": book.publisher,
                "isbn": book.isbn,
                "status": book.status,
                "category": book.category,
                "rating": book.rating,
                "location": book.location,
                "cover": book.cover
            }
        }

        try:
            # try to read file with given filename
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If filename above isn't found let write a new file with given filename
            with open(self.filename, "w") as data_file:
                json.dump(new_book, data_file, indent=4)
        else:
            # update new data and overwrite it into given filename
            data.update(new_book)
            with open(self.filename, "w") as data_file:
                json.dump(data, data_file, indent=4)

    def update_whole(self, bookID, **detail):
        """ Use to update all details of book that given book ID to json file
        :param bookID: string of book's ID
        :param detail: dictionary of string that pack all detail about book
        """
        try:
            # try to read file with given filename
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If filename above isn't found just print it in console
            print(f"File '{self.filename}' is Not Found")
        else:
            # update data and overwrite it into given filename
            details = ["nameTH", "nameEN", "author", "publisher", "isbn",
                       "status", "category", "rating", "location", "cover"]
            for each in details:
                data[bookID][each] = detail[each]
        with open(self.filename, "w") as data_file:
            json.dump(data, data_file, indent=4)

    def update_each_detail(self, bookID, updatable, detail):
        """ Update specific detail of book that given book ID to json file
        :param bookID: string of book's ID
        :param updatable: string of updatable topic detail that user want to update
        :param detail: string of detail of book that user want to update
        """
        try:
            # try to read file with given filename
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If filename above isn't found just print it in console
            print(f"File '{self.filename}' is Not Found")
        else:
            # update specific new data and overwrite it into given filename
            data[bookID][updatable] = detail
            with open(self.filename, "w") as data_file:
                json.dump(data, data_file, indent=4)

    def get_a_book(self, bookID):
        """ Get a book by slicing a dictionary with given book ID
        :param bookID: string of book's ID
        :return: a dictionary of a book
        """
        try:
            # try to read file with given filename and return sliced dictionary
            with open(self.filename, "r") as data_file:
                return json.load(data_file)[bookID]
        except KeyError:
            return False
        except FileNotFoundError:
            # If filename above isn't found just print it in console
            print(f"File '{self.filename}' is Not Found")

    def find_book_detail(self, findable, detail):
        """ Find book by findable detail and return book ID of that book
        :param findable: string of findable topic detail that user want to find
        :param detail: detail of book that user want to find
        :return: string of book's ID if available
        """
        try:
            # try to read file with given filename
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If filename above isn't found just print it in console
            print(f"File '{self.filename}' is Not Found")
        else:
            for bookID, details in data.items():
                try:
                    if details[findable] == detail:
                        return bookID
                except KeyError:
                    return False

    def get_all_book(self):
        """ Get dictionary of all book from json file
        :return: dictionary of all book
        """
        try:
            # try to read file with given filename and return dictionary
            with open(self.filename, "r") as data_file:
                return json.load(data_file)
        except FileNotFoundError:
            # If filename above isn't found just print it in console
            print(f"File '{self.filename}' is Not Found")

    def filter_book(self, filterable, detail):
        """ Filter by the given filterable topic and detail and return filtered dictionary
        :param filterable: string of filterable topic detail that user want to filter
        :param detail: string of detail of book that user want to update
        :return: a dictionary of filtered book detail
        """
        try:
            # try to read file with given filename
            with open(self.filename, "r") as data_file:
                all_book = json.load(data_file)
        except FileNotFoundError:
            # If filename above isn't found just print it in console
            print(f"File '{self.filename}' is Not Found")
        else:
            filtered = {}
            for bookID, details in all_book.items():
                # check condition and store it in filtered dictionary
                if details[filterable] == detail:
                    filtered[bookID] = details
            return filtered

    def get_book_from_list(self, bookID):
        """ Get a book by slicing list of book object with given book ID """
        for book in self.book_list:
            if book.id == bookID:
                return book

    def get_last_id(self):
        """ Use to get last number of fileID """
        try:
            # try to read file with given filename
            with open(self.fileID, "r") as file:
                # get last number from file
                return int(file.read().splitlines()[-1])

        except FileNotFoundError:
            # If file not found just create and write 0 in given filename
            with open(self.fileID, "w") as file:
                file.write('0' + '\n')
            return 0

    def manage_id(self, ID):
        """ Use to append given ID into given fileID name"""
        with open(self.fileID, "a") as file:
            file.write(str(ID) + '\n')


if __name__ == '__main__':
    database = BookDB('data')
    print(database.get_book_from_list('024'))
    database.get_all_book()
    # database.filter('author', 'proud')
