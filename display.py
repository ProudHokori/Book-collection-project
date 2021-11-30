from turtle import *
from bookdatabase import BookDB
from book import Book
from color import ScreenColor
import os

# path of gif folder that store all book's cover
path = os.path.abspath('gif')


class Display:
    def __init__(self):
        self.writer = Pen()
        self.screen = Screen()
        self.database = BookDB()

    # ------------------------- Used for FRONT-END decoration ------------------------- #
    def show_text_while(self, text, time, size):
        self.writer.clear()
        self.set_turtle_pointer()
        self.writer.pen(pencolor=ScreenColor.baseText1)
        for i in range(time):
            self.writer.write(text, move=False, align='center',
                              font=('Consolas', size, 'bold'))
        self.writer.penup()

    def show_text(self, text, pos_y, size):
        self.writer.goto(0, pos_y)
        self.writer.pen(pencolor=ScreenColor.baseText1)
        self.writer.write(text, move=False, align='center',
                          font=('Consolas', size, 'bold'))
        self.writer.penup()

    def draw_border_fill(self, x, y, height, wide):
        self.writer.pen(pencolor=ScreenColor.decorate, pensize=2)
        self.writer.goto(x, y)
        self.writer.pendown()
        self.writer.fillcolor(ScreenColor.baseScreen2)
        self.writer.begin_fill()
        self.writer.goto(x, y + height)
        self.writer.goto(x + wide, y + height)
        self.writer.goto(x + wide, y)
        self.writer.goto(x, y)
        self.writer.end_fill()
        self.writer.penup()

    def draw_border(self, x, y, height, wide):
        self.writer.pen(pencolor=ScreenColor.decorate, pensize=2)
        self.writer.goto(x, y)
        self.writer.pendown()
        self.writer.goto(x, y + height)
        self.writer.goto(x + wide, y + height)
        self.writer.goto(x + wide, y)
        self.writer.goto(x, y)
        self.writer.penup()

    def write_list(self, a_list, x, y, spacing, textsize, textcolor, form):
        self.writer.pen(pencolor=textcolor)
        for i in range(len(a_list)):
            self.writer.penup()
            self.writer.goto(x, y - (i * spacing))
            self.writer.write(f"{a_list[i]}", move=False, align='left',
                              font=('Consolas', textsize, form))
            self.writer.penup()

    def set_turtle_pointer(self):
        self.screen.addshape('pointer_.gif')
        self.writer.shape('pointer_.gif')
        self.writer.goto(0, 0)

    def decorate_book_pic(self,x, y):
        self.writer.goto(x, y)
        self.screen.addshape('book.gif')
        self.writer.shape('book.gif')

    # ------------------------- Main Graphic ------------------------- #
    def init_screen(self):
        bgcolor(ScreenColor.baseScreen1)
        self.show_text_while("Welcome to My Book Collection ;)", 200, 20)
        self.writer.penup()

    def show_choice(self):
        self.writer.clear()
        self.set_turtle_pointer()
        self.draw_border(-330, -70, 235, 660)
        self.show_text("Which choice do you prefer to do to your collection?", 120, 15)
        choices = ['1. Add book', '2. Find book', '3. Filter book',
                   '4. Show all book', '5. Update book\'s detail']
        self.write_list(choices, 0, 80, 30, 14, ScreenColor.baseText2, 'bold')
        self.decorate_book_pic(-130,30)
        choice = textinput("Choices", "Please select a choice (or press q to exit)")
        return choice

    def add_book_graphic(self):
        self.set_turtle_pointer()
        self.writer.clear()
        self.draw_border_fill(-180, -20, 170, 360)

        pos_y = 100
        self.show_text("Please put all required", pos_y, 15)
        self.show_text("details to collect your book", pos_y - 25, 15)

        req1 = ['* nameTH', '* nameEN', '* author']
        req2 = ['* publisher', '* status', '* isbn']
        self.write_list(req1, -110, pos_y - 60, 20, 13, ScreenColor.baseText2, 'bold')
        self.write_list(req2, 5, pos_y - 60, 20, 13, ScreenColor.baseText2, 'bold')
        self.decorate_book_pic(0,-120)

        nameTH, nameEN, author, publisher, isbn, status, category, rating, location = self.input_all_details()

        confirm, cover = self.check_book(nameTH=nameTH, nameEN=nameEN, author=author,
                                         publisher=publisher, status=status, isbn=isbn,
                                         category=category, rating=rating, location=location)

        if confirm == 'c':
            book = Book(database=self.database, nameTH=nameTH, nameEN=nameEN, author=author,
                        publisher=publisher, status=status, isbn=isbn, category=category,
                        rating=rating, location=location, cover=cover)
            self.show_text_while(f"{book.id} | {nameEN} by {author} is Added.", 200, 20)
        else:
            self.show_text_while("A book adding is already canceled.", 200, 20)
        self.set_turtle_pointer()

    def find_book_graphic(self):
        while True:
            self.set_turtle_pointer()
            self.writer.clear()
            self.draw_border_fill(-250, 20, 130, 500)
            pos_y = 100
            self.show_text("Which detail do you have to find the book?", pos_y, 15)
            findable1 = ['1. book ID', '2. NameTH']
            findable2 = ['3. NameEN', '4. ISBN']
            self.write_list(findable1, -130, pos_y - 35, 25, 13, ScreenColor.baseText2, 'bold')
            self.write_list(findable2, 20, pos_y - 35, 25, 13, ScreenColor.baseText2, 'bold')
            self.decorate_book_pic(0,-80)
            selected = textinput("Book Detail", "Please select a choice(or press q to exit)")
            if selected in ['1', '2', '3', '4']:
                break
            if selected == 'q':
                return
            self.show_text_while("Something went wrong, Please try again. :(", 100, 20)

        findable_list = ['bookID', 'nameTH', 'nameEN', 'isbn']
        findable = findable_list[int(selected) - 1]
        detail = textinput("Book Detail", f"Please input your {findable} that you want to find")
        if findable == 'bookID':
            bookID = detail
        else:
            bookID = self.database.find_book_detail(findable, detail)

        if self.check_id(bookID):
            self.show_each_book(bookID)
            textinput('Continue', 'press Enter to continue')
        else:
            self.show_text_while(f"Don't have this book in collection :(", 200, 20)

    def update_whole_book(self):
        self.set_turtle_pointer()
        self.writer.clear()

        pos_y = 50
        self.show_text("Update all of your book's details", pos_y, 17)
        self.show_text("Please input Book ID to update", pos_y - 35, 15)
        self.decorate_book_pic(0,-120)

        bookID = textinput("Book Detail", "Book ID")
        if self.check_id(bookID):
            self.show_each_book(bookID)
            nameTH, nameEN, author, publisher, isbn, status, category, rating, location = self.input_all_details()

            confirm, cover = self.check_book(nameTH=nameTH, nameEN=nameEN, author=author,
                                             publisher=publisher, status=status, isbn=isbn,
                                             category=category, rating=rating, location=location)
            if confirm == 'c':
                self.database.update_whole(bookID, nameTH=nameTH, nameEN=nameEN,
                                           author=author, publisher=publisher,
                                           status=status, isbn=isbn,
                                           category=category, rating=rating,
                                           location=location, cover=cover)
                self.show_text_while(f"{bookID} | {nameEN} by {author} is Updated.", 200, 20)
            else:
                self.show_text_while("A book updating is already canceled.", 200, 20)
            self.set_turtle_pointer()
        else:
            self.show_text_while(f"There is no book ID named '{bookID}' in collection :(", 200, 15)

    def update_each_detail(self):
        self.set_turtle_pointer()
        self.writer.clear()
        pos_y = 50
        self.show_text("Update the detail you want", pos_y, 17)
        self.show_text("Please input Book ID to update", pos_y - 35, 15)
        self.decorate_book_pic(0,-120)

        bookID = textinput("Book Detail", "Book ID")
        if self.check_id(bookID):
            self.show_each_book(bookID)
            for i in range(300):
                self.writer.write('  ')
            while True:
                self.set_turtle_pointer()
                self.draw_border_fill(-210, 70, 120, 420)
                pos_y = 150
                self.show_text("Which detail do you want to update?", pos_y, 15)
                updatable1 = ['1. Status', '2. Rating']
                updatable2 = ['3. Location', '4. Cover']
                self.write_list(updatable1, -130, pos_y - 35, 25, 13, ScreenColor.baseText2, 'bold')
                self.write_list(updatable2, 20, pos_y - 35, 25, 13, ScreenColor.baseText2, 'bold')
                self.decorate_book_pic(0,-35)
                updatable_list = ['status', 'rating', 'location', 'isbn']
                selected = textinput("Book Detail", "Please select a choice(or press q to exit)")
                if selected in ['1', '2', '3', '4']:
                    break
                if selected == 'q':
                    return
                self.show_text_while("Something went wrong, Please try again. :(", 100, 20)

            updatable = updatable_list[int(selected) - 1]
            detail = textinput("Book Detail", f"{updatable}")
            if updatable == 'isbn':
                cover = self.check_shape(detail)
                self.database.update_each_detail(bookID, 'cover', cover)
                self.database.update_each_detail(bookID, updatable, detail)
                self.show_text_while(f"Book's cover is Updated.", 150, 17)
            else:
                self.database.update_each_detail(bookID, updatable, detail)
                self.show_text_while(f'{updatable.capitalize()} is Updated.', 150, 17)
        else:
            self.show_text_while(f"There is no book ID named '{bookID}' in collection :(", 150, 15)

    def update_book_graphic(self):
        while True:
            self.set_turtle_pointer()
            self.writer.clear()
            self.draw_border_fill(-220, 20, 130, 450)
            pos_y = 100
            self.show_text("Which choice do you like to update?", pos_y, 15)
            update_choice = ['1.Update whole book.', '2.Update selected detail.']
            self.write_list(update_choice, -120, pos_y - 35, 30, 13, ScreenColor.baseText2, 'bold')
            self.decorate_book_pic(0,-80)

            selected = textinput("Book Detail", "Please select a choice(or press q to exit)")
            if selected == '1':
                self.update_whole_book()
                break
            elif selected == '2':
                self.update_each_detail()
                break
            elif selected == 'q':
                return
            self.show_text_while("Something went wrong, Please try again. :(", 100, 20)

    def show_all_book_graphic(self):
        self.set_turtle_pointer()
        self.writer.clear()
        self.show_text('Look at your console to see all book in table', 60, 20)
        self.decorate_book_pic(0,-50)
        self.database.show_all_book()
        textinput('Continue', 'press Enter to continue')
        self.clear_console()

    def filter_book_graphic(self):
        while True:
            self.set_turtle_pointer()
            self.writer.clear()
            self.draw_border_fill(-250, 0, 180, 500)
            pos_y = 140

            self.show_text("Filter book by", pos_y, 15)
            findable1 = ['1. NameEN', '2. Author', '3. Publisher', '4. Status']
            findable2 = ['5. Category', '6. Rating', '7. Location', '8. Cover']
            self.write_list(findable1, -130, pos_y - 35, 25, 13, ScreenColor.baseText2, 'bold')
            self.write_list(findable2, 30, pos_y - 35, 25, 13, ScreenColor.baseText2, 'bold')
            self.decorate_book_pic(0,-120)
            selected = textinput("Book Detail", "Please select a choice(or press q to exit)")
            if selected in [str(i) for i in range(1, 9)]:
                break
            if selected == 'q':
                return
            self.show_text_while("Something went wrong, Please try again. :(", 100, 20)

        filterable_list = ["nameEN", "author", "publisher", "status",
                           "category", "rating", "location", "cover"]
        filterable = filterable_list[int(selected) - 1]
        detail = textinput("Book Detail", f"Please input your {filterable} that you want to filter")
        self.database.filter(filterable, detail)
        self.set_turtle_pointer()
        self.writer.clear()
        self.show_text('Look at your console to see all book in table', 60, 20)
        self.decorate_book_pic(0,-50)
        textinput('Continue', 'press Enter to continue')
        self.clear_console()

    def main_graphic(self):
        while True:
            choice = self.show_choice()
            if choice == 'q':
                self.ending()
                break
            elif choice == '1':
                self.add_book_graphic()
            elif choice == '2':
                self.find_book_graphic()
            elif choice == '3':
                self.filter_book_graphic()
            elif choice == '4':
                self.show_all_book_graphic()
            elif choice == '5':
                self.update_book_graphic()
            else:
                self.show_text_while("Something went wrong, Please try again. :(", 150, 20)

    def ending(self):
        self.show_text_while("Hope you got a great experience. Thank you. ^^", 400, 20)
        exit()

    # ------------------------- Used for check book's detail ------------------------- #
    def check_book(self, **detail):
        self.writer.clear()
        self.writer.shape('pointer_.gif')
        self.show_text("Please confirm all book's details", 250, 14)

        cover = self.check_shape(detail["isbn"])
        details1 = [f'NameTH : {detail["nameTH"]}', f'NameEN : {detail["nameEN"]}',
                    f'Author : {detail["author"]}', f'Publisher : {detail["publisher"]}',
                    f'ISBN : {detail["isbn"]}']
        details2 = [f'Status : {detail["status"]}', f'Category : {detail["category"]}',
                    f'Rating : {detail["rating"]}', f'Location : {detail["location"]}',
                    f'Cover : {cover}']
        self.writer.goto(0, 0)
        self.write_list(details1, -250, -170, 25, 13, ScreenColor.baseText1, 'bold')
        self.write_list(details2, 40, -170, 25, 13, ScreenColor.baseText1, 'bold')

        self.writer.goto(0, 50)
        self.writer.shape(f"{path}\\{cover}")
        confirm = textinput("Confirm", "please press c to confirm")
        return confirm, cover

    def show_each_book(self, bookID):
        self.writer.clear()
        self.writer.shape('pointer_.gif')
        detail = self.database.get_book_from_json(bookID)
        details1 = [f'NameTH : {detail["nameTH"]}', f'NameEN : {detail["nameEN"]}',
                    f'Author : {detail["author"]}', f'Publisher : {detail["publisher"]}',
                    f'ISBN : {detail["isbn"]}']
        details2 = [f'Status : {detail["status"]}', f'Category : {detail["category"]}',
                    f'Rating : {detail["rating"]}', f'Location : {detail["location"]}',
                    f'Cover : {detail["cover"]}']

        self.show_text(f"This is {bookID} | {detail['nameEN']} by {detail['author']}", 250, 14)
        self.writer.goto(0, 0)
        self.write_list(details1, -250, -170, 25, 13, ScreenColor.baseText1, 'bold')
        self.write_list(details2, 40, -170, 25, 13, ScreenColor.baseText1, 'bold')

        self.writer.goto(0, 50)
        cover = self.check_shape(detail["isbn"])
        self.writer.shape(f"{path}\\{cover}")

    def check_id(self, bookID):
        detail = self.database.get_book_from_json(bookID)
        if detail:
            return True
        else:
            return False

    def check_shape(self, isbn):
        try:
            shape_ = f"{path}\\{isbn}.gif"
            self.screen.addshape(shape_)
            return f'{isbn}.gif'
        except Exception:
            shape_ = f"{path}\empty.gif"
            self.screen.addshape(shape_)
            return f'empty.gif'

    @staticmethod
    def input_all_details():
        nameTH = textinput("Book Detail", "NameTH")
        nameEN = textinput("Book Detail", "NameEN")
        author = textinput("Book Detail", "Author")
        publisher = textinput("Book Detail", "Publisher")
        isbn = textinput("Book Detail", "ISBN")
        status = textinput("Book Detail", "Status")
        category = textinput("Book Detail", "Category")
        rating = textinput("Book Detail", "Rating")
        location = textinput("Book Detail", "Location")
        return nameTH, nameEN, author, publisher, isbn, status, category, rating, location

    @staticmethod
    def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)


if __name__ == '__main__':
    display = Display()
    print(display.check_shape('9784832291249'))
