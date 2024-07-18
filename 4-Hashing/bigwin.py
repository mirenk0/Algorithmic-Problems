def count(prices):
  """
  This function counts the number of ways to buy and sell a stock
  such that the selling price is exactly double the buying price.

  Args:
      prices: A list of stock prices for n days.

  Returns:
      The number of ways to buy and sell the stock.
  """
  n = len(prices)
  prices_dict = {}
  ways_to_buy_count = 0
    
  for i in range(n):
    price = prices[i]

    if price > 1 and price % 2 == 0:
        buy_price = price // 2
        if buy_price in prices_dict:
            ways_to_buy_count += prices_dict[buy_price]

    prices_dict[price] = prices_dict.get(price, 0) + 1 

  return ways_to_buy_count


if __name__ == "__main__":
  print(count([1, 2, 3, 4])) # 2
  print(count([1, 1, 1, 1])) # 0
  print(count([1, 2, 1, 2, 1, 2])) # 1
  print(count([5, 1, 3, 4, 1, 6])) # 6
