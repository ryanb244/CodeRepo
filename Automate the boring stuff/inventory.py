import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, end=' ')
        print(k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        for j in inventory.keys():
            if j == i:
                inventory[j] = inventory[j] + 1
        inventory.setdefault(i, 1)
    return inventory
        


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

stuff = addToInventory(stuff, dragonLoot)


displayInventory(stuff)
