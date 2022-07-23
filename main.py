def maxProfit(prices):
    left = 0
    right =  1
    max_profit = 0
    while right  < len(prices):
        current_profit = prices[right] - prices[left]
        if current_profit > 0:
            max_profit = max(max_profit, current_profit)
            right += 1            
        else:
            left = right 
            right += 1
    
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))





