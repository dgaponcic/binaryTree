from printModule import *
from treeModule import *
import os


def rm_node(root):
    print("Please input node to be removed")
    inp = input("")
    root = root.removeNode(int(inp))
    return (root, False)

def insert_node(root):
    print("Please input node to be inserted")
    inp = input("")
    try:    
        root.insert(int(inp))
    except:
        return (root, False)
    return (root, False)

def traverse_tree_in(root):
    os.system('clear')
    root.print()
    print()
    printInorder(root)
    print()
    inp = input("")
    return (root, False)

def traverse_tree_pre(root):
    os.system('clear')
    root.print()
    print()
    printPreorder(root)
    print()
    inp = input("")
    return (root, False)

def traverse_tree_post(root):
    os.system('clear')
    root.print()
    print()
    printPostorder(root)
    print()
    inp = input("")
    return (root, False)

def search_node(root):
    print("Please input the node you want to search")
    inp = input("")
    try:
        arr = root.searchNode(int(inp), [])
        for element in arr:
            print(element.data, end=" ")
        print()
        inp = input("")
        return (root, False)
    except:
        return (root, False)

def level_traversal(root):
    os.system('clear')
    root.print()
    print()
    traverse(root)
    inp = input("")
    return (root, False)

def menu(root=None, choice=None):
    os.system("clear")
    if root:
        root.print()
    else:
        print("Welcome!\nPlease input values for tree nodes(ex: 4 6 2 1):")

        arr = input("").split()

        root = Node(int(arr[0]))
        arr.pop(0)

        for element in arr:
            root.insert(int(element))

        root.print()
    methods = {
    "1": 'rm_node',
    "2": "insert_node",
    "3": "traverse_tree_in",
    "4": "traverse_tree_pre",
    "5": "traverse_tree_post",
    "6": "search_node",
    "7": "level_traversal",
    }
    if not choice:
        print(' ')
        menu_options = [
            "1.Remove node",
            "2.Insert node",
            "3.Traverse tree in order",
            "4.Traverse tree pre order",
            "5.Traverse tree post order",
            "6.Search a node",
            "7.Level traversal",
            "0.Quit"
        ]

        print(' ')
        for option in menu_options:
            print(option)
    choice = input("")
    if not int(choice):
        return False
    while choice not in methods.keys(): 
        print('Please enter a valid choice:')
        choice = input("")
    else:
        root, choice = globals()[methods[choice]](root)

    menu(root, choice)

menu()