from hashtable import HashTable, Node

def test1():
    data = [("user1", "password"), ("ios", "superior"), ("android", "meh"), ("windows", "lol")]
    table = HashTable()
    for item in data:
        k, v = item[0], item[1]
        N = Node(k, v)
        table[k] = N

    print("Table: ", table)
    print("Get Item: ", table["ios"])
    node = Node("blackberry", "huh?")
    table.setitem(node.key(), node)
    print("Updated Table: ", table)


def test2():
    data = [("user2", "password"), ("Facebook", "NSA"), ("Chevron", "DrillBabyDrill"), ("Intel", "TSMC"), ("Amazon", "Seattle")]
    table = HashTable()
    for item in data:
        k, v = item[0], item[1]
        N = Node(k, v)
        table[k] = N

    print("Table: ", table)
    print("Get Item: ", table.get("Chevron"))
    print("Get Item: ", table["Facebook"])
    print("Get Item: ", table["intel"])
    table.delete("Chevron")
    table.delete("Facebook")
    print("Updated Table: ", table)

def test3():
    data = [("user3", "password3"), ("Brittney", "LeaveHerAlone"), ("Elvis", "HeyMama"), ("Hawkings", "Radiation"),\
            ("Obama", "Drones"), ("Trump", "Drumpf"), ("ChrisBrown", "Rhianna"), ("Bond", "James"), ("Nixon", "Watergate")]
    table = HashTable()
    for item in data:
        k, v = item[0], item[1]
        N = Node(k, v)
        table[k] = N


    print("Table: ", table)
    print("Get Item: ", table.get("Nixon"))
    print("Get Item: ", table.get("Elvis"))
    table.delete("user3")
    del(table["Trump"])
    del(table["Brittney"])
    del(table["obama"])
    print("Updated Table: ", table)

def test4():
    data = [("user4", "password4"), ("Brittney", "LeaveHerAlone"), ("Elvis", "HeyMama"), ("Hawkings", "Radiation"),\
            ("Obama", "Drones"), ("Trump", "Drumpf"), ("ChrisBrown", "Rhianna"), ("Bond", "James"), ("Nixon", "Watergate")]
    table = HashTable()
    for item in data:
        k, v = item[0], item[1]
        N = Node(k, v)
        table.setitem(k, N)

    for item in table:
        print(item)
    print(table)

def test5():
    data = [("user2", "password"), ("Facebook", "NSA"), ("Chevron", "DrillBabyDrill"), ("Intel", "TSMC"), ("Amazon", "Seattle")]
    table = HashTable()
    for item in data:
        k, v = item[0], item[1]
        N = Node(k, v)
        table[k] = N
    print("Table: ", table)
    del(table["user2"])
    del (table["Facebook"])
    del (table["Chevron"])
    del (table["Intel"])
    del (table["Amazon"])
    print("Updated Table: ", table)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()