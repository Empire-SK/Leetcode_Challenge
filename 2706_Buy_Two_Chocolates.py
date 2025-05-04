class Solution(object):
    def buyChoco(self, prices, money):

        # Initialize variables to track the two smallest prices
        first_min = float('inf')
        second_min = float('inf')
        
        # Find the two smallest prices in the array
        for price in prices:
            if price < first_min:
                second_min = first_min
                first_min = price
            elif price < second_min:
                second_min = price
        
        # Calculate the total cost of the two cheapest chocolates
        total_cost = first_min + second_min
        
        # Return leftover money if affordable, otherwise return original money
        return money - total_cost if total_cost <= money else money