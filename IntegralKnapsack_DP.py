from FractionalKnapsack import Item

# setting up data for testing
cumin = Item("cumin", 4, 6)
saffron = Item("saffron", 2, 5)
pepper = Item("pepper", 2, 4)
item_list = [cumin, saffron, pepper]
knapsack = [None, None, None]

limit = 5
# end setting up data for testing

# this part is preparing the empty table and
# will not be in the runtime analysis of the algorithm
table = []
for i in range(len(item_list) + 1):
    row = []
    for j in range(limit + 1):
        row.append(None)
    table.append(row)
# end preparing

def integralKnapsack(table, limit, item_list):
    '''
    This function uses DP to solve the knapsack 
    problem. It returns the maximum profit.
    '''
    # fill the first column with 0
    for i in range(len(item_list) + 1):
        table[i][0] = 0
    # fill the first row with 0
    for i in range(limit + 1):
        table[0][i] = 0
    # index run correctly in the table,
    # run 1 ahead of the item_list
    for i in range(1, len(item_list) + 1):
        for space in range(1, limit + 1):
            # temporarily, we fill in the current case
            # as the weight already in the knapsack
            table[i][space] = table[i-1][space]
            # profit of current object
            profit = item_list[i-1].getProfit()
            # weight of current object
            weight = item_list[i-1].getWeight()
            # total profit of other remaining objects if we 
            # remove some to add the current object
            profit_others = table[i-1][space - weight]
            if (space >= weight) and (table[i][space] < profit_others + profit):
                table[i][space] = profit_others + profit
    return table[len(item_list)][limit]