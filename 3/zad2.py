money_transfers = ["in Steve 20 \"lunch\"", "out Jane 15 \"dinner\""]

expenses = [transfer for transfer in money_transfers if "out" in transfer]
print(expenses)
