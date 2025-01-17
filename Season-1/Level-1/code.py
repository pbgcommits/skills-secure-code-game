'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0

    # Test 8 - shouldn't be able to make an order worth more than 99999
    MAX_AMOUNT_PAYABLE = 99999
    amount_payable = 0

    for item in order.items:
        if item.type == 'payment':
            if item.amount + net >= 1e16:
                ... # idk how to deal with this (underflow?)
            net += item.amount
        elif item.type == 'product':
            product_cost = item.amount * item.quantity
            net -= product_cost
            amount_payable += product_cost
        else:
            return "Invalid item type: %s" % item.type
        if amount_payable > MAX_AMOUNT_PAYABLE:
            return "Total amount payable for an order exceeded"
        # Test 7 - floating point error
        net = round(net, ndigits=2)

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id