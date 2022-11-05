import Node
import RedBlack

class StockTrading:
    # use class instead of array - only change is readability
    def __init__(self):
        self.transactions = {}

    def logTransaction(self,record):
        name = record[0]
        pricePerStock = record[1]
        quantity = record[2]
        timestamp = record[3]


        tradeValue = pricePerStock * quantity
            
            
        recordData = [pricePerStock,quantity,timestamp]
        
        if name in self.transactions:
            self.transactions[name].tree.put(recordData,tradeValue)

            # compare to current min and max. This makes minTransaction() and maxTransaction()
            # linear instead of logarithmic by only storing one extra array for each
            minimum = self.transactions[name].minimum
            maximum = self.transactions[name].maximum

            minVal = minimum[0][1] * minimum[0][2]
            maxVal = maximum[0][1] * maximum[0][2]

            if (minVal > tradeValue):
                # this record becomes the new minimum
                self.transactions[name].minimum = [recordData]
            elif (minVal == tradeValue):
                # ALSO a record with a minimum trade value
                self.transactions[name].minimum.append(recordData)
            if (maxVal < tradeValue):
                # this record becomes the new maximum
                self.transactions[name].maximum = [recordData]
            elif (maxVal == tradeValue):
                # ALSO a record with a maximum trade value
                self.transactions[name].maximum.append(recordData)
            
        else:
            self.transactions[name] = RedBlack(Node(recordData,tradeValue),recordData,recordData)

    def minTransactions(self,stockname):
        # retrieve RedBlack object attribute - constant
        if stockname in self.transactions:
            return self.transactions[stockname].minimum

    def maxTransactions(self,stockname):
        # retrieve RedBlack object attribute - constant
        if stockname in self.transactions:
            return self.transactions[stockname].maximum

    def floorTransactions(self,stockname,thresholdVal):
        if stockname in self.transactions:
            return self.transactions[stockname].tree.floor(thresholdVal)

    def ceilingTransactions(self,stockname,thresholdVal):
        if stockname in self.transactions:
            return self.transactions[stockname].tree.ceiling(thresholdVal)

    def sortedTransactions(self,stockname):
        if stockname in self.transactions:
            return self.transactions[stockname].tree.sorted()

    def rangeTransactions(self,stockname,fromVal,toVal):
        if stockname in self.transactions:
            return self.transactions[stockname].tree.range(fromVal,toVal)
