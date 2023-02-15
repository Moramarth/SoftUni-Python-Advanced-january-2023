def stock_availability(inventory_list, *args):
    if args:
        if args[0] == "delivery":
            for i in range(1, len(args)):
                inventory_list.append(args[i])

        elif args[0] == "sell":
            if len(args) == 1:
                inventory_list.pop(0)
            elif type(args[1]) is int:
                for _ in range(args[1]):
                    inventory_list.pop(0)
            else:
                for i in range(1, len(args)):
                    if args[i] in inventory_list:
                        inventory_list = [item for item in inventory_list if item != args[i]]

    return inventory_list
