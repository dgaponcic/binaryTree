from collections import defaultdict

class Node:
    def __init__(self, data):
	    self.left = None
	    self.right = None
	    self.data = data
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def searchNode(self, data, arr):
        found = -1
        if self.data:
            if data == self.data:
                found = 1
                arr.append(self)
            elif data < self.data:
                if self.left != None:
                    arr.append(self)
                    return self.left.searchNode(data, arr)
            elif data > self.data:
                if self.right != None:
                    arr.append(self)
                    return self.right.searchNode(data, arr)
        if found == 1: return arr
        return []

    def getParent(self, data):
        parents = self.searchNode(data, [])
        if not parents: return None
        if len(parents) < 2: return None
        return parents[-2]


    def removeNode(self, data):
        parent = self.getParent(data)
        node = self.searchNode(data, [])
        if not node: return self
        if node: node = node[-1]
        if node == self and not node.right and not node.left:
            return None
        elif node == self and not node.right and node.left:
            node = node.left
            return node
        elif node == self and node.right and not node.left:
            node = node.right
            return node
        elif not node.right and not node.left:
            if parent and parent.left == node:
                parent.left = None
                return self
            elif parent and parent.right == node:
                parent.right = None
                return self
        elif node.right and not node.left:
            if parent and parent.left and parent.left == node:
                parent.left = node.right
            if parent and parent.right and parent.right == node:
                parent.right = node.right
            node = node.right
            return self
        elif node.left and not node.right:
            if parent and parent.left and parent.left == node:
                parent.left = node.left
            if parent and parent.right and parent.right == node:
                parent.right = node.left
            node = node.left
            return self
        elif node.left and node.right:
            child = node.left
            while child.right:
                child = child.right
            self = self.removeNode(child.data)
            child.left = node.left
            child.right = node.right
            if parent and parent.left and parent.left == node:
                parent.left = child
            if parent and parent.right and parent.right == node:
                parent.right = child
            if parent: node = child
            else: self = child
            return self
    @property
    def height(self):
        return self.get_height()

    def get_height(self, node=None, level=0):
        if not level:
            node = self
        if not node:
            return 0
        level += 1
        return (
            max(self.get_height(node.left, level), self.get_height(node.right, level))
            + 1
        )

    def tree_stringify(
        self, node=0, level=0, line=0, data=None, height=0, parent_index=None, left=True
    ):
        if not data:
            data = defaultdict(lambda: {})
        if not level:
            node = self
            height = self.height
            parent_index = height * (height + 1) * (2 * height + 1) / 6 + height
        if not node:        # stop condition
            return data
        if left:
            index = parent_index - (height - level) ** 2 - 1
        else:
            index = parent_index + (height - level) ** 2 + 1

        data[line][index] = node.data
        old_line = line
        line += (height - level - 1) ** 2 + 1
        level += 1
        for i in range(old_line + 1, line):
            if node.left:
                data[i][index - (i - old_line)] = "/"
            if node.right:
                data[i][index + (i - old_line)] = "\\"
        data = self.tree_stringify(node.left, level, line, data, height, index)
        data = self.tree_stringify(node.right, level, line, data, height, index, False)
        return data

    def normalize_tree(self):
        lines = self.tree_stringify()
        for value in lines.values():
            correction = 0
            for i in range(0, 100):
                val = value.get(i)
                if val:
                    length = len(str(val))
                    if length > 1:
                        correction = 1
                        value[i] = '' if i else value[i]
                        value[i - correction] = val if (i - correction) else value[i - correction]
        return lines

    def print(self):
        lines = self.normalize_tree()
        for value in lines.values():
            line = ""
            height = self.height + 1
            top = height * (height + 1) * (2 * height + 1) / 6 + height
            for i in range(0, int(top) + 1):
                line += str(value.get(i, " "))
            print(line)