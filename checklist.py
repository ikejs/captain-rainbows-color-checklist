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
    checklist[index] = "√ " + checklist[index]

# USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# SELECT
def select(function_code):
    # Ignore Case
    function_code = function_code.upper()

    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number: ")
        read(item_index)

    # Update item
    elif function_code == "U":
        item_index = user_input("Index Number to Update: ")
        changeTo = user_input("New Item Name: ")
        update(item_index, changeTo)

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
    print("Press C to add to list, R to Read from list, P to display list, U to update an item, D to delete an item, and Q to quit")
    selection = user_input("")
    running = select(selection)
