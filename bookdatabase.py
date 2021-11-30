import json
from prettytable import PrettyTable


class BookDB:
    def __init__(self, name='book_database'):
        self.name = name
        self.booklist = []

    def add_book(self, book):
        self.booklist.append(book)
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
            with open(f"{self.name}.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(f"{self.name}.json", "w") as data_file:
                json.dump(new_book, data_file, indent=4)
        else:
            data.update(new_book)
            with open(f"{self.name}.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def update_whole(self, id_, **detail):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print(f"File '{self.name}.json' is Not Found")
        else:
            details = ["nameTH", "nameEN", "author", "publisher", "isbn",
                       "status", "category", "rating", "location", "cover"]
            for each in details:
                data[id_][each] = detail[each]
        with open(f"{self.name}.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    def update_each_detail(self, id_, updatable, detail):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print(f"File '{self.name}.json' is Not Found")
        else:
            data[id_][updatable] = detail
            with open(f"{self.name}.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def get_book_from_json(self, id_):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                return json.load(data_file)[id_]
        except KeyError:
            return False
        except FileNotFoundError:
            print(f"File '{self.name}.json' is Not Found")

    def find_book_detail(self, findable, detail):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print(f"File '{self.name}.json' is Not Found")
        else:
            for bookID, details in data.items():
                try:
                    print(details[findable], detail)

                    if details[findable] == detail:
                        return bookID
                except KeyError:
                    return False

    def show_all_book(self):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                all_book = json.load(data_file)
        except FileNotFoundError:
            print(f"File '{self.name}.json' is Not Found")
        else:
            self.create_table(all_book)

    def filter(self, filterable, detail):
        try:
            with open(f"{self.name}.json", "r") as data_file:
                all_book = json.load(data_file)
        except FileNotFoundError:
            print(f"File '{self.name}.json' is Not Found")
        else:
            filtered = {}
            for bookID, details in all_book.items():
                if details[filterable] == detail:
                    filtered[bookID] = details
            self.create_table(filtered)

    @staticmethod
    def get_last_id(fileID):
        try:
            with open(fileID, "r") as file:
                lastID = file.read().splitlines()

        except Exception:
            with open(fileID, "w") as file:
                lastID = file.write('0' + '\n')
        finally:
            return int(lastID[-1])

    @staticmethod
    def manage_id(fileID, ID):
        with open(fileID, "a") as file:
            file.write(str(ID) + '\n')

    def get_book_from_list(self, id_):
        for book in self.booklist:
            if book.id == id_:
                return book

    @staticmethod
    def create_table(dict_):
        table = PrettyTable()
        table.field_names = ['Book ID', 'Name of Book(EN)', 'Author', 'Publisher',
                             'ISBN', 'Status', 'Category', 'Rating', 'Location', 'Cover']
        for bookID, details in dict_.items():
            table.add_row([bookID, details['nameEN'], details['author'],
                           details['publisher'], details['isbn'], details['status'],
                           details['category'], details['rating'],
                           details['location'], details['cover']])
        print(table)


if __name__ == '__main__':
    database = BookDB('data')
    print(database.get_book_from_list('024'))
    database.show_all_book()
    # database.filter('author', 'proud')
