class Item():
    def __init__(self, name, weight, profit):
        self.name = name
        self.weight = weight
        self.profit = profit
        self.value = 0

    def setValue(self, value):
        self.value = value

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getProfit(self):
        return self.profit

    def getValue(self):
        return self.value

# setting up data for testing
cumin = Item("cumin", 2, 6)
saffron = Item("saffron", 2, 8)
pepper = Item("pepper", 5, 10)
nutmeg = Item("nutmeg", 1.5, 4)
turmeric = Item("turmeric", 1, 3)
paprika = Item("paprika", 3, 9)
item_list = [cumin, saffron, pepper, nutmeg, turmeric, paprika]
knapsack = [None, None, None, None, None, None]
# end setting up data for testing

def next_item_with_the_highest_value(item_list, index):
    item_list.sort(key=lambda x: x.getValue(), reverse=True)
    return item_list[index]

# Greedy method
def fracKnapsack(item_list, knapsack, limit):
    '''
    the main idea is, we see what is the item with the most value, 
    we take the most of that, and then see the second most valuable 
    item and try to take the most of that, and so on...
    '''
    current_weight = 0
    for i in range(len(item_list)):
        knapsack[i] = 0
        value = item_list[i].getProfit() / item_list[i].getWeight()
        item_list[i].setValue(value)
    index = 0
    while current_weight < limit:
        item = next_item_with_the_highest_value(item_list, index)
        take_weight = min(item.getWeight(), limit - current_weight)
        knapsack[index] = take_weight
        current_weight = current_weight + take_weight
        index = index + 1