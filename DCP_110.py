'''
Daily Coding Problem #110

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5

Return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''

class Tree:
    def __init__(self):
        self.first_node = None

class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

class TreeTraverser:
    def __init__(self):
        pass

    def find_all_routes(self, tree):
        routes = []
        self.traverse(tree.first_node, routes)
        return routes

    @staticmethod
    def traverse(node, routes):
        if node.left == None and node.right == None:
            routes.append(TreeTraverser.find_route(node, []))
        if node.left != None:
            TreeTraverser.traverse(node.left, routes)
        if node.right != None:
            TreeTraverser.traverse(node.right, routes)
    
    @staticmethod
    def find_route(node, route):
        route.insert(0, node.value)
        if node.parent != None:
            TreeTraverser.find_route(node.parent, route)
        return route



if __name__ == "__main__":
    tree = Tree()

    # Setup example tree
    tree.first_node = Node(None, 1)
    tmp = tree.first_node
    tmp.left = Node(tmp, 2)
    tmp.right = Node(tmp, 3)
    tmp = tmp.right
    tmp.left = Node(tmp, 4)
    tmp.right = Node(tmp, 5)

    traverser = TreeTraverser()
    routes = traverser.find_all_routes(tree)
    print(routes)
        