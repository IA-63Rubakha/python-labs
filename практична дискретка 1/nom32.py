def calculate_order(pricelist, order):
    pricelist_copy = [[item[0].strip().lower(), item[1], item[2]] for item in pricelist]
    total = 0
    for item_name, qty in order:
        name = item_name.strip().lower()
        found = False
        for i in range(len(pricelist_copy)):
            if pricelist_copy[i][0] == name:
                found = True
                if qty > pricelist_copy[i][2]:
                    return -1
                total += pricelist_copy[i][1] * qty
                pricelist_copy[i][2] -= qty
                break
        if not found:
            return -2
    return total
pricelist = (["ХЛІБ", 20, 10], ["МОЛОКО", 35, 5], ["СИР", 120, 3])
order = (("хліб ", 2), ("молоко", 1))
print(calculate_order(pricelist, order))
order2 = (("хліб", 20),)
print(calculate_order(pricelist, order2))
order3 = (("м'ясо", 1),)
print(calculate_order(pricelist, order3))