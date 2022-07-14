# Monthly expenses
monthly_expenses = {
    'rent': 1200,
    'utilities': 300,
    'transport': 450,
    'food': 600,
    'entertainment': 110,
    'clothing': 220,
    'health': 30,
    'internet': 60,
    'education': 200,
    'other': 100
}


# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    summa = 0
    for v in monthly_expenses.values():
        summa += v
    return summa

# Find the least expensive expense
def least_expensive(monthly_expenses: dict) -> str:
    """
    Find the least expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        least_expensive: least expensive expense
    """
    key = list(monthly_expenses.keys())[0]
    min_v = list(monthly_expenses.values())[0]
    for k,v in monthly_expenses.items():
        if min_v > v:
            min_v = v
            key = k
            
        
    return key,min_v

# Find the most expensive expense
def most_expensive(monthly_expenses: dict) -> str:
    """
    Find the most expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        most_expensive: most expensive expense
    """
    key = list(monthly_expenses.keys())[0]
    max_v = list(monthly_expenses.values())[0]
    for k,v in monthly_expenses.items():
        if max_v < v:
            max_v = v
            key = k
            
        
    return key,max_v
print(total_expenses(monthly_expenses))
print(least_expensive(monthly_expenses))
print(most_expensive(monthly_expenses))