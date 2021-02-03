from exercise.adt.BTree import BTree

if __name__ == '__main__':
    BT = BTree()

    BT.insert(22, 1)
    BT.insert(37, 2)
    BT.insert(46, 3)
    BT.insert(58, 4)
    BT.insert(42, 1)
    BT.insert(65, 6)
    BT.insert(72, 6)
    BT.insert(80, 6)
    BT.insert(93, 6)
    BT.insert(11, 6)
    BT.insert(12, 6)
    BT.insert(24, 6)
    BT.insert(29, 6)
    BT.insert(38, 6)
    BT.insert(40, 6)
    BT.insert(41, 6)
    BT.insert(43, 10)
    BT.insert(45, 10)
    BT.insert(48, 10)
    BT.insert(50, 10)
    BT.insert(51, 10)
    BT.insert(53, 10)
    BT.insert(56, 10)
    BT.insert(59, 10)
    BT.insert(63, 10)
    BT.insert(66, 10)
    BT.insert(70, 10)
    BT.insert(74, 10)
    BT.insert(75, "Zucchero")
    BT.insert(83, 10)
    BT.insert(85, 10)
    BT.insert(86, 10)
    BT.insert(95, 10)
    BT.insert(98, 10)

    print("B-TREE with b =", BT.b_dimension())
    print("\n")
    BT.print_structure_tree()
    print("\n")
    BT.print_tree()

    print("\n")
    key = 64
    value = "Pippo"
    print("Insert element with Key:", key, "and Value: ", value)
    BT.insert(key, value)

    key = 64
    value = "NewValueOfPippo"
    print("Insert element with same Key:", key, ", and Value: ", value, "(Update the previous value)")
    BT.insert(key, value)
    print("B-Tree after Insert operation:")
    BT.print_tree()

    print("\n")
    key = 64
    temp = BT.search(key, BT.root())
    print("Search element with Key:", key)
    if temp is not None:
        print("     -->", temp)
    else:
        print(" Key:", key, " Not Found!")
    key = 1000
    temp = BT.search(key, BT.root())
    print("Search element with Key:", key)
    if temp is not None:
        print("     -->", temp)
    else:
        print(" Key:", key, " Not Found!")

    print("\n")
    key = 64
    print("Delete element with Key:", key)
    if not BT.delete(key):
        print(" Key:", key, " Not Found!")
    else:
        print(" Key:", key, " Deleted!")

    print("")
    key = 1000
    print("Delete element with Key:", key)
    if not BT.delete(key):
        print(" Key:", key, " Not Found!")

    print("")
    key = 70
    print("Delete element with Key:", key)
    if not BT.delete(key):
        print(" Key:", key, " Not Found!")
    BT.print_tree()

    print("")
    key = 66
    print("Delete element with Key:", key, "- TRANSFER operation")
    if not BT.delete(key):
        print(" Key:", key, " Not Found!")
    BT.print_tree()

    print("")
    key = 100
    value = "Pluto"
    print("Insert element with same Key:", key, ", and Value: ", value, "- SPLIT operation")
    BT.insert(key, value)
    print("B-Tree after Insert operation:")
    BT.print_tree()

    print("")
    key = 80
    print("Delete element with Key:", key)
    if not BT.delete(key):
        print(" Key:", key, " Not Found!")
    BT.print_tree()
    print("\n")

    key = 65
    print("Delete element with Key:", key, "- FUSION operation")
    if not BT.delete(key):
        print(" Key:", key, " Not Found!")
    BT.print_tree()
    print("\n")

    key = 53
    print("Delete element with Key:", key, "- ROOT deletion")
    if not BT.delete(key):
        print(" Key:", key, " Not Found!")
    BT.print_tree()
