# Problem: Best Time to Buy and Sell Stock
# Approach: Loop korar shomoy ekhon porjonto shobcheye kom dam (min_price) mone rakhi. Protidin bechle koto profit hoto seta dekhi, ar shobcheye boro profit rakhi.
# Time: O(n)
# Space: O(1)

def max_profit(prices):
    min_price = float("inf")
    best = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            best = max(best, price - min_price)

    return best


print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit([]))                  # 0