class SETTree():
    class _Node():

        def __init__(self, parent=None, left=None, right=None, setnumber=None,
                     setvalue=None):
            """
            Do not modify the constructor.
            """
            self._parent = parent
            self._left = left
            self._right = right
            self._setnumber = setnumber
            self._setvalue = setvalue
            self._size = 0


        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, parent):
            self._parent = parent

        @property
        def left(self):
            return self._left

        @left.setter
        def left(self, left):
            self._left = left

        @property
        def right(self):
            return self._right

        @right.setter
        def right(self, right):
            self._right = right

        @property
        def length(self):
            return self._length

        @length.setter
        def length(self, length):
            self._length = length

        @property
        def size(self):
            return self._size

        @size.setter
        def size(self, size):
            self._size = size

        @property
        def position(self):
            return self._position

        @position.setter
        def position(self, position):
            self._position = position

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        def is_external(self):
            return self.left == None and self.right == None


        # TO DO - Question 1
        def height(self):
            lDepth = 0
            rDepth = 0
            node = self
            while (node is not None):
                lDepth += 1
                node = self._left
            node = self
            while (node is not None):
                rDepth += 1
                node = self._right
                # if node is None:
                #     return 0
                # else:
                #     # Compute the depth of each subtree
                #     lDepth = 1+self.height(node._left)
                #     rDepth = 1+self.height(node._right)

                # Use the larger one
            if (lDepth > rDepth):
                return lDepth
            else:
                return rDepth
        """
            Returns the height of the subtree rooted at this node.
        """

    def __init__(self):
        """
        Do not modify the constructor.
        """
        self._root = self._Node(setnumber=0, setvalue = {" "})
        self._size = 0
        self._min1 = 0
    def count_leaves(self, node):
        if node is None:
            return 0
        if node.is_external():
            return 1
        return self.count_leaves(node._left) + self.count_leaves(node._right)
    def list_leaves(self, node):
        lst1 = []
        if node.is_external():
            lst1.append(node)
        else:
            lst1 += self.list_leaves(node._left)
            lst1 += self.list_leaves(node._right)
        return lst1
    def search_set1(self, set1, node):
        if(node is None):
            return []
        elif((node._setvalue) == set1):
            return [node._setnumber]
        else:
            return self.search_set1(set1, node._left) + self.search_set1(set1, node._right)
    def search_set2(self, set2, node):
        if(node is None):
            return []
        elif((node._setvalue) == set2):
            return [node]
        else:
            return self.search_set2(set2, node._left)+ self.search_set2(set2, node._right)
    def search_sets1(self, node):
        s_n_list = []
        node1 = node
        while(node1 != self._root):
            s_n_list.append(node1._setnumber)
            if((node1 == node1._parent._right) and (node1._parent == self._root)):
                node1 = node1._parent
            elif(node1._parent == node1._parent._parent._right):
                node1 = node1._parent
            elif ((node1 == node1._parent._right) and (node1._parent == node1._parent._parent._left) and (node1._parent._parent == self._root)):
                node1 = self._root
            elif((node1 == node1._parent._right) and (node1._parent == node1._parent._parent._left)):
                while(node1._parent != node1._parent._parent._right):
                        node1 = node1._parent
                        if(node1._parent == self._root):
                            break
                node1 = node1._parent
        return s_n_list
    def search_sets2(self, node_list):
        list1 = []
        for node in node_list:
            list1.append(self.search_sets1(node))
        return list1
    def optimal1(self, lst1):
        if(lst1 == []):
            return "No optimal solution"
        lst2 = []
        lst3= []
        for i in lst1:
            lst2.append(len(i))
        min1 = min(lst2)
        for i in lst1:
            if(len(i) == min1):
                lst3.append(i)
        return lst3

    def insert_set(self, number, value):
        """
        Insert a new point into the tree.

        Walk the tree node by node to find where the new point should be
        inserted.

        There are four possible cases while walking.
        1. The node has two children. Insert the appropriate child node onto
           the stack.
        2. The node does not have children. Made a child for the existing
           point, and re-insert the node onto the stack.
        3. The node has one child and it encloses the new point. Insert the
           child onto the stack.
        4. The node has one child and it does not enclose the new point. Make
           the sibling node for the new point and finish.
        """
        if self._root == None:
            self._root = self._Node(setnumber=0, setvalue={})
        else:
            for leaf in self.list_leaves(self._root):
                leaf._left = self._Node(parent=leaf, setnumber=number, setvalue=leaf._setvalue)
                leaf._right = self._Node(parent=leaf, setnumber=number, setvalue=leaf._setvalue.union(value))
