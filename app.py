from display import Display
from bookdatabase import BookDB
# run this file to use Book Collection app
database = BookDB('bookdatabase.json')
display = Display(database)
display.init_screen('peach')  # you can change theme in this line
display.menu()
