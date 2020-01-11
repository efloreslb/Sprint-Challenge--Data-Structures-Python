class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'V: {self.value}, Left: {self.left}, Right: {self.right}'
        # return "hello"

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than curr node
        if value < self.value:
            # is there already a value at self.left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # the new value is greater than the curr node then go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if root node is target value
        if target == self.value:
            # print("True")
            return True
        
        # target is smaller, go left
        if target < self.value:
            if not self.left:
               #  print("False")
                return False
            else: 
                return self.left.contains(target)

        # target is greater, go right
        else:
            if not self.right:
               #  print("False")
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        #return when there is no larger number, cant go right
        if not self.right:
            print(self.value)
            return self.value

        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)