from turtle import Pen, Screen
from book import Book
from color import ScreenColor, ConsoleColor
from os import path, name, system
from time import sleep
from prettytable import PrettyTable


class Display:
    """
        This class is used to display the features on Python Turtle
    Graphic screen and show table of data on console. there are
    8 attributes that is
    writer : object of Pen class that used to write all graphic on screen
    screen : object of Screen class that used to show screen
    database : object of BookDB class that be the database of this class
    colorS : object of ScreenColor class that manage about theme color on screen
    colorC : object of ConsoleColor class that manage about theme color on cosole
    cover_path : string of folder's path that store all book's cover picture
    pointer_path : string of folder's path that store all pointer picture
    pic_path : string of folder's path that store all decorated picture
    """

    def __init__(self, database):
        """ Initialize Pen and Screen from turtle module and BookDB from bookdatabase.
        :param database: BookDB's object
        """
        self.writer = Pen()
        self.screen = Screen()
        self.database = database
        self.colorS = ScreenColor()
        self.colorC = ConsoleColor()

        # path of picture folder that store all pictures in this program
        self.cover_path = path.abspath('cover')
        self.pointer_path = path.abspath('pointer')
        self.pic_path = path.abspath('picture')

    # ------------------------- Used for FRONT-END decoration ------------------------- #

    def show_text_while(self, text, secs, textsize):
        """ Use for show text for while in center of screen.
        :param text: string of text that want to show
        :param secs: a numbers of time that want to remain text
        :param textsize: a numbers of text size
        """
        self.writer.clear()
        self.set_pointer()
        self.writer.pen(pencolor=self.colorS.mainText)
        self.writer.write(text, move=False, align='center',
                          font=('Consolas', textsize, 'bold'))
        self.writer.penup()
        self.writer.goto(0, -20)
        sleep(secs)

    def show_text(self, text, pos_y, textsize):
        """ Use for show text in align center.
        :param text: string of text that want to show
        :param pos_y: a number of text's position in y-axis
        :param textsize: a numbers of text size
        """
        self.writer.goto(0, pos_y)
        self.writer.pen(pencolor=self.colorS.mainText)
        self.writer.write(text, move=False, align='center',
                          font=('Consolas', textsize, 'bold'))
        self.writer.penup()

    def draw_border_fill(self, x, y, height, wide):
        """ Use for draw filled-border in given size and position.
        :param x: a number of bottom left conner position (x-axis)
        :param y: a number of bottom left conner position (y-axis)
        :param height: a number of border's height
        :param wide: a number of border's width
        """
        self.writer.pen(pencolor=self.colorS.decorate, pensize=2)
        self.writer.goto(x, y)
        self.writer.pendown()
        self.writer.fillcolor(self.colorS.popupWindow)
        self.writer.begin_fill()
        self.writer.goto(x, y + height)
        self.writer.goto(x + wide, y + height)
        self.writer.goto(x + wide, y)
        self.writer.goto(x, y)
        self.writer.end_fill()
        self.writer.penup()

    def draw_border(self, x, y, height, wide):
        """ Use for draw border in given size and position.
        :param x: a number of bottom left conner position (x-axis)
        :param y: a number of bottom left conner position (y-axis)
        :param height: a number of border's height
        :param wide: a number of border's width
        """
        self.writer.pen(pencolor=self.colorS.decorate, pensize=2)
        self.writer.goto(x, y)
        self.writer.pendown()
        self.writer.goto(x, y + height)
        self.writer.goto(x + wide, y + height)
        self.writer.goto(x + wide, y)
        self.writer.goto(x, y)
        self.writer.penup()

    def write_list(self, a_list, x, y, spacing, textsize, textcolor, form):
        """ Use for write each text in each line in order
        :param a_list: list of text that want to write in each line
        :param x: start writing position in x-axis
        :param y: start writing position in y-axis
        :param spacing: a number of space between line
        :param textsize: a numbers of text size
        :param textcolor: string of color
        :param form: string of text form
        """
        self.writer.pen(pencolor=textcolor)
        for i in range(len(a_list)):
            self.writer.penup()
            self.writer.goto(x, y - (i * spacing))
            self.writer.write(f"{a_list[i]}", move=False, align='left',
                              font=('Consolas', textsize, form))
            self.writer.penup()

    def set_pointer(self):
        """ Use to initial shape and position of writer """
        self.writer.shape(f"{self.pointer_path}/{self.colorS.pointer}")
        self.writer.goto(0, 0)

    def decorate_book_pic(self, x, y):
        """ Use to change shape in given picture to x,y position
        :param x: x-axis position
        :param y: y-axis position
        """
        self.writer.goto(x, y)
        self.writer.shape(f'{self.pic_path}/{self.colorS.picture}')

    # ------------------------- Main Graphic ------------------------- #

    def init_screen(self, theme='default'):
        """ Setup theme of screen color and writer"""
        self.writer.speed(5)
        self.colorS.select_theme(theme)
        self.screen.bgcolor(self.colorS.baseScreen)
        self.screen.addshape(f'{self.pic_path}/{self.colorS.picture}')
        self.screen.addshape(f"{self.pointer_path}/{self.colorS.pointer}")
        self.show_text_while("❤Welcome to My Book Collection ʕ•́ᴥ•̀ʔ❤", 3, 20)
        self.writer.penup()

    def show_choice(self):
        """ Use to show all choice then allow user to input and return desired choice
        :return: string of desired choice's number from user input
        """
        # show all choice in screen
        self.writer.clear()
        self.set_pointer()
        self.show_text("Book Collection App", 150, 17)
        self.show_text("❤ MENU ❤", 110, 22)
        self.draw_border(-330, -155, 235, 660)
        self.show_text("Which choice do you prefer to do to your collection?", 30, 15)
        choices = ['1. Add a new book', '2. Find a book', '3. Filter book',
                   '4. Update book\'s detail', '5. Show all book in collection']
        self.write_list(choices, 0, -10, 30, 14, self.colorS.subText, 'bold')
        self.decorate_book_pic(-130, -60)

        # return choice that user input
        choice = self.screen.textinput("Choices", "Please select a choice (or press q to exit)")
        return choice

    def add_book_graphic(self):
        """ Allow user to input new book's details to create a new Book object """
        # show what required detail of book that user have to input on screen
        self.set_pointer()
        self.writer.clear()
        self.draw_border_fill(-180, -20, 170, 360)
        pos_y = 100
        self.show_text("Please put all required", pos_y, 15)
        self.show_text("details to collect your book", pos_y - 25, 15)
        req1 = ['* nameTH', '* nameEN', '* author']
        req2 = ['* publisher', '* status', '* isbn']
        self.write_list(req1, -110, pos_y - 60, 20, 13, self.colorS.subText, 'bold')
        self.write_list(req2, 5, pos_y - 60, 20, 13, self.colorS.subText, 'bold')
        self.decorate_book_pic(0, -120)

        # input all details that need to create a new Book object.
        nameTH, nameEN, author, publisher, isbn, status, category, rating, location = self.input_all_details()

        # check the details that user input.
        confirm, cover = self.check_book(nameTH=nameTH, nameEN=nameEN, author=author,
                                         publisher=publisher, status=status, isbn=isbn,
                                         category=category, rating=rating, location=location)
        # check confirm message from user
        if confirm == 'c':
            # create Book object by proven details.
            book = Book(database=self.database, nameTH=nameTH, nameEN=nameEN, author=author,
                        publisher=publisher, status=status, isbn=isbn, category=category,
                        rating=rating, location=location, cover=cover)
            # show to user that book is already added
            self.show_text_while(f"{book.id} | {nameEN} by {author} is Added.", 2, 16)
        else:
            # show to user that the book added is canceled
            self.show_text_while("A book adding is already Canceled.", 2, 20)
        self.set_pointer()

    def find_book_graphic(self):
        """ Find the book by selected element that user input and show a book """
        while True:
            # show what element that user can use to find the book on screen
            self.set_pointer()
            self.writer.clear()
            self.draw_border_fill(-250, 20, 130, 500)
            pos_y = 100
            self.show_text("Which detail do you have to find the book?", pos_y, 15)
            findable1 = ['1. book ID', '2. NameTH']
            findable2 = ['3. NameEN', '4. ISBN']
            self.write_list(findable1, -130, pos_y - 35, 25, 13, self.colorS.subText, 'bold')
            self.write_list(findable2, 20, pos_y - 35, 25, 13, self.colorS.subText, 'bold')
            self.decorate_book_pic(0, -80)

            # Let's user select choice that they want to find by what.
            selected = self.screen.textinput("Find a book", "Please select a choice(or press q to exit)")

            # check if selected choice is selectable or not
            if selected in ['1', '2', '3', '4']:
                break
            elif selected == 'q':
                # quit and back to MENU page
                return
            self.show_text_while("Something went wrong, Please try again. :(", 1, 20)

        # Let's user input the detail that they want to find.
        findable_list = ['bookID', 'nameTH', 'nameEN', 'isbn']
        findable = findable_list[int(selected) - 1]
        detail = self.screen.textinput("Find a book", f"Please input your {findable} that you want to find")
        # check what element that user input to find and match it with BookID
        if findable == 'bookID':
            bookID = detail
        else:
            bookID = self.database.find_book_detail(findable, detail)

        # show the book that user want weather the book ID is found
        if self.check_id(bookID):
            self.show_each_book(bookID)
            self.screen.textinput('Find a book', 'press Enter to continue')
        else:
            self.show_text_while(f"Don't have this book in collection :(", 2, 20)

    def update_whole_book(self):
        """ Update all detail about selected book by using book ID """
        while True:
            # show that user have to input the book ID which they want to update on screen
            self.set_pointer()
            self.writer.clear()
            pos_y = 60
            self.show_text("Update all of your book's details", pos_y, 17)
            self.show_text("Please input Book ID to update", pos_y - 40, 15)
            self.decorate_book_pic(0, -100)

            # allow user to input book ID
            bookID = self.screen.textinput("Update book's detail", "Input Book ID (or press q to exit)")

            # check weather it have this ID in collection or not
            if self.check_id(bookID):
                # Let's show the book that user want to update first
                self.show_each_book(bookID)
                # input all detail that user want to update
                nameTH, nameEN, author, publisher, isbn, status, category, rating, location = self.input_all_details()

                # check the details that user input.
                confirm, cover = self.check_book(nameTH=nameTH, nameEN=nameEN, author=author,
                                                 publisher=publisher, status=status, isbn=isbn,
                                                 category=category, rating=rating, location=location)
                # check confirm message from user
                if confirm == 'c':
                    # update book by proven details.
                    self.database.update_whole(bookID, nameTH=nameTH, nameEN=nameEN,
                                               author=author, publisher=publisher,
                                               status=status, isbn=isbn,
                                               category=category, rating=rating,
                                               location=location, cover=cover)
                    # show to user that book is already updated
                    self.show_text_while(f"{bookID} | {nameEN} by {author} is Updated.", 2, 20)
                else:
                    # show to user that the book updated is canceled
                    self.show_text_while("A book updating is already canceled.", 2, 20)
                    return
            elif bookID == 'q':
                # quit and back to MENU page
                return
            else:
                self.show_text_while(f"There is no book ID named '{bookID}' in collection :(", 2, 15)

    def update_each_detail(self):
        """ Update some detail of selected book by using book ID """
        while True:
            # show that user have to input the book ID which they want to update on screen
            self.set_pointer()
            self.writer.clear()
            pos_y = 60
            self.show_text("Update the detail you want", pos_y, 17)
            self.show_text("Please input Book ID to update", pos_y - 40, 15)
            self.decorate_book_pic(0, -100)

            # allow user to input book ID
            bookID = self.screen.textinput("Update book's detail", "Input Book ID (or press q to exit)")
            # check weather it have this ID in collection or not
            if self.check_id(bookID):
                # Let's show the book that user want to update first
                self.show_each_book(bookID)
                sleep(2)

                while True:
                    # show what element that user can update with the book on screen
                    self.set_pointer()
                    self.draw_border_fill(-210, 70, 120, 420)
                    pos_y = 150
                    self.show_text("Which detail do you want to update?", pos_y, 15)
                    updatable1 = ['1. Status', '2. Rating']
                    updatable2 = ['3. Location', '4. Cover']
                    self.write_list(updatable1, -130, pos_y - 35, 25, 13, self.colorS.subText, 'bold')
                    self.write_list(updatable2, 20, pos_y - 35, 25, 13, self.colorS.subText, 'bold')
                    self.decorate_book_pic(0, -35)

                    # Let's user select choice that they want to update.
                    updatable_list = ['status', 'rating', 'location', 'isbn']
                    selected = self.screen.textinput("Update book's detail",
                                                     "Please select a choice(or press q to exit)")

                    # check if selected choice is selectable or not
                    if selected in ['1', '2', '3', '4']:
                        break
                    if selected == 'q':
                        return
                    self.show_text_while("Something went wrong, Please try again. :(", 1, 20)

                # Let's user input the detail that they want to update.
                updatable = updatable_list[int(selected) - 1]
                detail = self.screen.textinput("Update book's detail", f"{updatable}")
                # check what element that user input to update
                if updatable == 'isbn':
                    # if user want to update cover they have to input ISBN
                    cover = self.check_shape(detail)
                    self.database.update_each_detail(bookID, 'cover', cover)
                    self.database.update_each_detail(bookID, updatable, detail)
                    # show to user that book is already updated
                    self.show_text_while(f"Book's cover is Updated.", 2, 17)
                else:
                    self.database.update_each_detail(bookID, updatable, detail)
                    self.show_text_while(f'{updatable.capitalize()} is Updated.', 2, 17)
            elif bookID == 'q':
                # quit and back to MENU page
                return
            else:
                self.show_text_while(f"There is no book ID named '{bookID}' in collection :(", 2, 15)

    def update_book_graphic(self):
        """ Allow user to choose that they want update whole book or each detail in that book """
        while True:
            # show the choice that user can choose
            self.set_pointer()
            self.writer.clear()
            self.draw_border_fill(-220, 20, 130, 450)
            pos_y = 100
            self.show_text("Which choice do you like to update?", pos_y, 15)
            update_choice = ['1.Update whole book.', '2.Update specific detail.']
            self.write_list(update_choice, -120, pos_y - 35, 30, 13, self.colorS.subText, 'bold')
            self.decorate_book_pic(0, -80)

            # Let's user select choice what feature they want to update.
            selected = self.screen.textinput("Update book's detail", "Please select a choice(or press q to exit)")

            if selected == '1':
                self.update_whole_book()
                break
            elif selected == '2':
                self.update_each_detail()
                break
            elif selected == 'q':
                # quit and back to MENU page
                return
            self.show_text_while("Something went wrong, Please try again. :(", 1, 20)

    def filter_book_graphic(self):
        """
        Filter the book by selected element that user input and
        show filtered book table in console
        """
        while True:
            # show what element that user can use to filter the book on screen
            self.set_pointer()
            self.writer.clear()
            self.draw_border_fill(-250, 0, 180, 500)
            pos_y = 140
            self.show_text("Filter book by", pos_y, 15)
            filterable1 = ['1. NameEN', '2. Author', '3. Publisher', '4. Status']
            filterable2 = ['5. Category', '6. Rating', '7. Location', '8. Cover']
            self.write_list(filterable1, -130, pos_y - 35, 25, 13, self.colorS.subText, 'bold')
            self.write_list(filterable2, 30, pos_y - 35, 25, 13, self.colorS.subText, 'bold')
            self.decorate_book_pic(0, -120)

            # Let's user select choice that they want to filter by what.
            selected = self.screen.textinput("Filter book", "Please select a choice(or press q to exit)")

            # check if selected choice is selectable or not
            if selected in [str(i) for i in range(1, 9)]:
                break
            if selected == 'q':
                # quit and back to MENU page
                return
            self.show_text_while("Something went wrong, Please try again. :(", 1, 20)

        # Let's user input the detail that they want to filter.
        filterable_list = ["nameEN", "author", "publisher", "status",
                           "category", "rating", "location", "cover"]
        filterable = filterable_list[int(selected) - 1]
        detail = self.screen.textinput("Filter book", f"Please input your {filterable} that you want to filter")
        # filter book by inputted detail and create table in console
        filtered = self.database.filter_book(filterable, detail)
        self.create_table(filtered)
        self.set_pointer()
        self.writer.clear()
        # show user to look at the console
        self.show_text('Look at your console to see filtered book in table.❤', 60, 18)
        self.decorate_book_pic(0, -50)
        self.screen.textinput('Filter book', 'press Enter to continue')
        self.clear_console()

    def show_all_book_graphic(self):
        """ Show all book in form of table on console and tell user to look at console """
        self.set_pointer()
        self.writer.clear()
        self.show_text('Look at your console to see all book in table.❤', 60, 20)
        self.decorate_book_pic(0, -50)
        all_book = self.database.get_all_book()
        self.create_table(all_book)
        self.screen.textinput('Continue', 'press Enter to continue')
        self.clear_console()

    def menu(self):
        """ Show and allow user to choose menu that they want to do in this app """
        while True:
            choice = self.show_choice()
            if choice == 'q':
                self.ending_graphic()
                break
            elif choice == '1':
                self.add_book_graphic()
            elif choice == '2':
                self.find_book_graphic()
            elif choice == '3':
                self.filter_book_graphic()
            elif choice == '4':
                self.update_book_graphic()
            elif choice == '5':
                self.show_all_book_graphic()
            else:
                self.show_text_while("Something went wrong, Please try again. :(", 1, 20)

    def ending_graphic(self):
        """ Show the graphic for ending app and exit program """
        self.writer.clear()
        self.set_pointer()
        self.show_text("Hope you had a great experience.", 70, 18)
        self.show_text("❤Thank you. ʕ•́ᴥ•̀ʔ❤", 20, 23)
        self.decorate_book_pic(0, -70)
        sleep(5)
        exit()

    # ------------------------- Used for check book's detail ------------------------- #
    def check_book(self, **detail):
        """ Use to show and check all given detail in that book
        :param detail: dictionary of string that pack all detail about book
        :return: string of confirmation massage and cover that match with book's ISBN
        """
        # Show all details of book that user just input
        self.writer.clear()
        self.set_pointer()
        self.show_text("Please confirm all book's details", 250, 14)
        # check filename of cover's picture
        cover = self.check_shape(detail["isbn"])
        details1 = [f'NameTH : {detail["nameTH"]}', f'NameEN : {detail["nameEN"]}',
                    f'Author : {detail["author"]}', f'Publisher : {detail["publisher"]}',
                    f'ISBN : {detail["isbn"]}']
        details2 = [f'Status : {detail["status"]}', f'Category : {detail["category"]}',
                    f'Rating : {detail["rating"]}', f'Location : {detail["location"]}',
                    f'Cover : {cover}']
        self.writer.goto(0, 0)
        # write all details
        self.write_list(details1, -280, -170, 25, 13, self.colorS.subText, 'bold')
        self.write_list(details2, 80, -170, 25, 13, self.colorS.subText, 'bold')
        # show book's cover
        self.writer.goto(0, 50)
        self.writer.shape(f"{self.cover_path}/{cover}")
        # get confirmation message from user if all detail is correct
        confirm = self.screen.textinput("Confirm", "please press c to confirm")
        # return confirmation message and checked cover's picture filename
        return confirm, cover

    def show_each_book(self, bookID):
        """ Use to show the book details and cover's book by given book ID
        :param bookID: string of book's ID
        """
        # show all detail of book that given ID
        self.writer.clear()
        self.set_pointer()
        # load a book details
        detail = self.database.get_a_book(bookID)
        details1 = [f'NameTH : {detail["nameTH"]}', f'NameEN : {detail["nameEN"]}',
                    f'Author : {detail["author"]}', f'Publisher : {detail["publisher"]}',
                    f'ISBN : {detail["isbn"]}']
        details2 = [f'Status : {detail["status"]}', f'Category : {detail["category"]}',
                    f'Rating : {detail["rating"]}', f'Location : {detail["location"]}',
                    f'Cover : {detail["cover"]}']
        self.show_text(f"This is {bookID} | {detail['nameEN']} by {detail['author']}", 250, 14)
        self.writer.goto(0, 0)
        # write all details
        self.write_list(details1, -280, -170, 25, 13, self.colorS.subText, 'bold')
        self.write_list(details2, 80, -170, 25, 13, self.colorS.subText, 'bold')
        # show book's cover
        self.writer.goto(0, 50)
        cover = self.check_shape(detail["isbn"])
        self.writer.shape(f"{self.cover_path}/{cover}")

    def check_id(self, bookID):
        """ Use to check that have given book ID or not
        :param bookID: string of book ID
        :return: boolean of book ID
        """
        detail = self.database.get_a_book(bookID)
        return bool(detail)

    def check_shape(self, isbn):
        """ Use to check the match between given ISBN and filename of cover's picture
        if have a match, It will return cover's picture name else will return default picture
        :param isbn: string of ISBN
        :return: string of match picture's name with ISBN
        """
        try:
            shape_ = f"{self.cover_path}/{isbn}.gif"
            self.screen.addshape(shape_)
            return f'{isbn}.gif'
        except Exception:
            shape_ = f"{self.cover_path}/empty.gif"
            self.screen.addshape(shape_)
            return 'empty.gif'

    def input_all_details(self):
        """ Use to input and return all details that need for create a book
        :return: string of all details in book
        """
        nameTH = self.screen.textinput("Book Detail", "NameTH")
        nameEN = self.screen.textinput("Book Detail", "NameEN")
        author = self.screen.textinput("Book Detail", "Author")
        publisher = self.screen.textinput("Book Detail", "Publisher")
        isbn = self.screen.textinput("Book Detail", "ISBN")
        status = self.screen.textinput("Book Detail", "Status")
        category = self.screen.textinput("Book Detail", "Category")
        rating = self.screen.textinput("Book Detail", "Rating")
        location = self.screen.textinput("Book Detail", "Location")
        return nameTH, nameEN, author, publisher, isbn, status, category, rating, location

    def create_table(self, dict_):
        """ Use to create and print table with given dictionary on console
        :param dict_:
        """
        table = PrettyTable()

        # create header of table
        headers = ['Book ID', 'Name of Book(EN)', 'Author', 'Publisher',
                   'ISBN', 'Status', 'Category', 'Rating', 'Location', 'Cover']
        table.field_names = [f'{self.colorC.bold}{head}{self.colorC.end}' for head in headers]

        # add every data in dictionary into table
        for bookID, details in dict_.items():
            table.add_row([bookID, details['nameEN'], details['author'],
                           details['publisher'], details['isbn'], details['status'],
                           details['category'], details['rating'],
                           details['location'], details['cover']])

        print(table)  # print it out in console

    @staticmethod
    def clear_console():
        """ Use to clear console after print some table """
        command = 'clear'
        # If Machine is running on Windows, use cls
        if name in ('nt', 'dos'):
            command = 'cls'
        system(command)


if __name__ == '__main__':
    pass
