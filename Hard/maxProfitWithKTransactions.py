def maxProfitWithKTransactions(prices, k):
    if len(prices) < 2:
		return 0
    
    previousTransactions = maxProfitWithOneTransaction(prices)
    
    if k == 1:
        return previousTransactions[-1]
    
    for j in range(k - 1):
        transactions = [0] * len(prices)
        
        for i in range(1, len(prices)):
            profit = max(previousTransactions[i - 1], transactions[i - 1]) + prices[i] - prices[i - 1]
            transactions[i] = profit
            
        maxProfit = transactions[0]
            
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, transactions[i])
            transactions[i] = maxProfit
            
		previousTransactions = transactions[:]
        
    return previousTransactions[-1]

def maxProfitWithOneTransaction(prices):
    transaction = [0] * len(prices)
    low = prices[0]
    maxProfit = 0
    
    for i in range(len(prices)):
        low = min(low, prices[i])
        maxProfit = max(maxProfit, prices[i] - low)
        transaction[i] = maxProfit
    
    return transaction
