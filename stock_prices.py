def get_max_profit(stock_prices):
    """
    Takes in a list of stock prices, with the index position as the time of price,
    and returns what prices you should have purchased/sold the stock
    """
    low_index = low_price(stock_prices)

    sell_price = high_price(stock_prices[low_index:])

    buy_price = stock_prices[low_index]

    max_profit = sell_price - buy_price

    return max_profit



def low_price(stock_prices):
    """
    Takes in list of stock prices and returns the index position of the lowest
    price
    """

    lowest = (stock_prices[0], 0)

    for i, price in enumerate(stock_prices):
        if price < lowest[0]:
            lowest = (price, i)

    return lowest[1]



def high_price(stock_prices):
    """
    Takes in a list of stock prices and returns the highest price
    """

    highest = stock_prices[0]

    for price in stock_prices:
        if price > highest:
            highest = price

    return highest



stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(stock_prices_yesterday)