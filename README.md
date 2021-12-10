
# <p align='center'> Book Collection Project </p>

The main objectives of this project are for concluding and applying
all lessons of the Computer Programming I course, Kasetsart University.
Another objective is for creating program which can help user to store, find 
and manage the data of their book collection.
<p align='center'>
<img src="https://github.com/ProudHokori/Book-collection-project/blob/main/md/logo_app.png">
</p>

---
## ♥ Overview and features ♥

<p align='center'>
<img src="https://github.com/ProudHokori/Book-collection-project/blob/main/md/menu_page.png">
</p>

This application is used for managing everything about book collection data. 
And these are all features of my application.

### ♥ Add a new book
User can add new books into database.
* Program will generate their own book's ID automatically.
* User can check all details and book's cover before storing it in database.
     
    ![img_2.png](md/add_page.png)
     
### ♥ Find a book
User can find books from database.
* User can find a book by _4 details_ which are 
  * Book ID
  * NameTH
  * NameEN
  * ISBN
* App will show all details and book cover on screen.

    ![img_2.png](md/find_page.png)

### ♥ Filter books
User can filter books from database.
   * User can filter books by 8 details which are
      - NameEN
      - Author
      - Publisher
      - Status
      - Category
      - Rating
      - Location
      - Cover
   * App will show all filtered books in a form of table on console.
  
        ![img_2.png](md/filter_page.png)

### ♥ Update book's details
User can update book's details in database.
   * This feature is capable of 2 things which are
      - updating a whole book : update all details of a book except original ID
      - update specific detail : update a specific details which are
        - Status
        - Rating
        - Location
        - Cover

     ![img_2.png](md/update_page.png)

### ♥ Show all books
App will show all books in collection in a form of table on console.
  
![img.png](md/console_table.png)
  
### ♥ Quit menu
Most of the uses of the button Q are used to quit the menu or to exit the program.

![img_3.png](md/quit.png)

### ♥ Change theme
User can run and choose theme in `app.py` to change 
theme of the application. The themes that are available now :
* Default theme
* Dark theme
* Mono theme
* Peach theme
* Winter theme
* Yaoi theme
    
![img.png](md/all_theme.png)

---
## ♥ Program's Requirements ♥

These are required python version, modules and tools 
that user need to download before running the program.

### ♥ Python version
* [Python 3.9](https://www.python.org/downloads/)
### ♥ Modules
Required modules in `requirements.txt`.
* `turtle` : used for all graphics.
* `prettytable` : used for creating and printing table on console.
* `time` : to use sleep function to delay some graphics.
* `os` : used for accessing picture file in each folder.
* `json` : to generate a json file to store the data

Note : font `Consolas` is required for better experience, 
click [here](https://github.com/tsenart/sight/raw/master/fonts/Consolas.ttf) to download.

---
## ♥ Program's design ♥

My application consists of three main classes which are 
`Book`, `BookDB` and `Display`. It has two classes which are 
ConsoleColor and ScreenColor, for decorating the program.

### ♥ Class `Book` 
Represents a book and each book will have
their own details which are used to create attributes.
In addition, IDs of each book will be created automatically.
### ♥ Class `BookDB`
Used for managing all data files of this app
such as, adding, finding and updating books.
### ♥ Class `Display`
Displays all the features on Python Turtle Graphic screen, and a table of data on console. 
### ♥ Class `ConsoleColor` and `ScreenColor`
These two classes are used for decorating color, format and theme in the application.

### ♥ UML class diagram 
![img_1.png](book_collection_diagram.png)

---
## ♥ Code structure ♥

This program consists of five python files to run the program. 
Two database files, which are a json file and a txt file, 
and three folders of pictures.  
### ♥ Python file
* `app.py ` : Used to start and **running** the program.
* `book.py `: Contains **Book** class.
* `bookdatabase.py` : Contains **BookDB** class.
* `display.py` : Contains **Display** class.
* `color.py` : Contains **ScreenColor** class and **ConsoleColor** class.
### ♥ Database file
* `bookdatabase.json` : Displays an example of a json file which contains all 
  data of books in the collection.
* `fileID.txt` : Displays an example of a txt file which contains IDs of 
  all books which is used for running ID of each book.
### ♥ Picture folder
* `cover folder` : Stores all books' cover files.
* `pointer folder` : Stores pointer's icons, which are parts of the themes' decoration.
* `picture folder` : Stores all pictures for decoration.

---
 ### **Hope you have a great experience. Thank you. ♥**

---   
