class Node:
    def __init__(self,record,value,isRed = False,parent = None):
        self.records = [record]
        self.value = value
        self.left = None    # left child
        self.right = None   # right child
        self.isRed = isRed  # is colour of link to it red
        self.parent = parent

    def rotateLeft(self):
        # put self's right-child in self's place and realign to fit
        # this keeps the red links on the left while maintaing tree structure
        x = self.right
        if self.parent:
            if self == self.parent.right:
                self.parent.right = x
            else:
                self.parent.left = x
        self.right = x.left
        if self.right:
            self.right.parent = self
        x.left = self
        x.isRed = False
        self.isRed = True   # self to x link still red
        x.parent = self.parent
        self.parent = x

    def rotateRight(self):
        x = self.parent
        if x.parent:
            if x == x.parent.right:
                x.parent.right = self
            else:
                x.parent.left = self
        x.left = self.right
        if x.left:
            x.left.parent = x
        self.right = x
        self.isRed = False
        x.isRed = True
        self.parent = x.parent
        x.parent = self

                
    def recolour(self):
        # flip where the red links are
        if self.parent:
            self.isRed = True
        self.left.isRed = False
        self.right.isRed = False

    def root(self):
        # finds root of tree before functions are called
        current = self
        while current.parent:
            current = current.parent
        return current

    def isColourRed(self,child):
        if child=="left.left":
            if self.left:
                x = self.left.left
            else:
                return False
        if child=="left":  x = self.left
        if child=="right":  x = self.right

        if x is None:
            return False
        else:
            return x.isRed
                    

    def put(self,record,value): # ITERATIVE
        root = self.root()
        current = root
        while True:
            # regular BST input
            if value == current.value:
                current.records.append(record)
            elif value < current.value:
                if current.left is None:
                    current.left = Node(record,value,True,current)
                        # nb. current is the parent of new Node
                else:
                    current = current.left
                    continue
            elif value > current.value:
                if current.right is None:
                    current.right = Node(record,value,True,current)
                else:
                    current = current.right
                    continue
            break
    
        # maintain the structure of a LLRB BST
        while True:
            changes = 0
            if (current.isColourRed("right")) and not (current.isColourRed("left")):
                if not current.isRed:
                    # keep the red links on the left
                    current.rotateLeft()
                else:
                    # change around parents
                    current.rotateLeft()
                    current.parent.rotateRight()
                changes+=1
            if current.isColourRed("left") and current.isRed:
                # no two red links in a row
                current.rotateRight()
                changes+=1
            if current.isColourRed("left") and current.isColourRed("right"):
                # both children have red links -> parent has red link
                current.recolour()
                changes+=1
            if (current.parent is None) or (changes == 0): # reached the root
                break
            else:
                current = current.parent


##    def min(self):          # ITERATIVE
##        # traverse as far leftwards from the root
##        current = self.root()
##        while current.left:
##            current = current.left
##        return current.records
##
##    def max(self):          # ITERATIVE
##        # traverse as far rightwards from the root
##        current = self.root()
##        while current.right:
##            current = current.right
##        return current.records


    def floor(self,value):  # ITERATIVE
        # record with largest value smaller than threshold
        # traverse as far right provided the value is <= Node's value
        current = self.root()
        potentialVal = None
        while True:
            if current.value == value:
                return current.records
            elif current.value > value:
                if current.left:
                    if potentialVal == current.value:
                        potentialVal = current.left.value
                    current = current.left
                    continue
                else:
                    # no records below threshold value
                    return potentialVal
            else:
                if current.right:
                    if current.right.value >= value:
                        # between current and current.right
                        potentialVal = current.value
                        current = current.right
                        continue
                    else:
                        current = current.right
                        potentialVal = current.value
                        continue
                else:
                    return current.records


    def ceiling(self,value):    # ITERATIVE
        # record with smallest value larger than threshold
        # traverse as far left provided the value is >= Node's value
        current = self.root()
        potentialVal = None
        while True:
            if current.value == value:
                return current.records
            elif current.value < value:
                if current.right:
                    if potentialVal == current.value:
                        potentialVal = current.right.value
                    current = current.right
                    continue
                else:
                    # no records above threshold value
                    return potentialVal
            else:
                if current.left:
                    if current.left.value <= value:
                        # between current and current.left
                        potentialVal = current.value
                        current = current.left
                        continue
                    else:
                        current = current.left
                        potentialVal = current.value
                        continue
                else:
                    return current.records
                

    def sorted(self):       # RECURSIVE
        sorted_records = []
        if self.value is None:  # what is all this???
            return None
        else:
            rt = self.root()
            rt.sortedAux(sorted_records)
            return sorted_records
    def sortedAux(self,sorted_records):
        # sort left side of the tree
        if self.left:
            self.left.sortedAux(sorted_records)

        for record in self.records:
            sorted_records.append(record)

        # sort right side of the tree
        if self.right:
            self.right.sortedAux(sorted_records)

            


    def range(self,fromVal,toVal):  # RECURSIVE
        # run a modified sorted() algorithm, discluding values not in range
        range_records = []
        if self.value is None:
            return None
        else:
            rt = self.root()
            rt.rangeAux(fromVal,toVal,range_records)
            return range_records
    def rangeAux(self,fromVal,toVal,range_records):
        
        if fromVal <= self.value <= toVal:
            if self.left:
                self.left.rangeAux(fromVal,toVal,range_records)

            for record in self.records:
                range_records.append(record)

            if self.right:
                self.right.rangeAux(fromVal,toVal,range_records)
        elif toVal < self.value:
            if self.left:
                self.left.rangeAux(fromVal,toVal,range_records)
            else:
                return
        elif self.value < fromVal:
            if self.right:
                self.right.rangeAux(fromVal,toVal,range_records)
            else:
                return
