from colored import fg, bg, attr

checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    item = checklist[int(index)]
    print(item)

# UPDATE
def update(index, newName):
    checklist[int(index)] = newName

# DESTROY
def destroy(index):
    checklist.pop(int(index))

# LIST ALL ITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(int(index), list_item))
        index += 1

# MARK COMPLETED
def mark_completed(index):
    checklist[int(index)] = "√ " + checklist[int(index)]

# UNCHECK
def uncheck(index):
    checklist[int(index)] = checklist[int(index)].replace("√ ", "")

# USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# SELECT
def select(function_code):
    # CLear Terminal
    print(chr(27) + "[2J")

    # Ignore Case
    function_code = function_code.upper()

    # Create item
    if function_code == "A":
        input_item = user_input("Add item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number to Print: ")
        read(item_index)

    # Update item
    elif function_code == "U":
        item_index = user_input("Index Number to Update: ")
        changeTo = user_input("New Item Name: ")
        update(item_index, changeTo)

    # Check item
    elif function_code == "CH":
        item_index = user_input("Index Number to Check: ")
        mark_completed(item_index)

    # Uncheck item
    elif function_code == "UN":
        item_index = user_input("Index Number to Uncheck: ")
        uncheck(item_index)

    # Destroy item
    elif function_code == "D":
        item_index = user_input("Index Number to Delete: ")
        destroy(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Quit
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

running = True
while running:
    print(attr('bold'), fg('white'), bg('green'), "Press A to add to list, R to Read from list, P to display list, U to update an item, D to delete an item, and Q to quit")
    selection = user_input("")
    running = select(selection)
