def printInorder(root):
	if root:
				printInorder(root.right)
		print(root.data, end=" ")

		printInorder(root.left) 


def printPostorder(root): 
	if root:
		printPostorder(root.left) 
		printPostorder(root.right)
		print(root.data, end=" "), 


def printPreorder(root): 
	if root:  
		print(root.data, end=" "),
		printPreorder(root.left)
		printPreorder(root.right) 


def traverse(root):
  thisLevel = [root]
  while thisLevel:
    nextLevel = list()
    for node in thisLevel:
      print (node.data, ' ', end = ''),
      if node.left: nextLevel.append(node.left)
      if node.right: nextLevel.append(node.right)
    print(" \n")
    thisLevel = nextLevel

def getLevels(root):
	levels = list()
	thisLevel = [root]
	while thisLevel:
		levels.append(thisLevel)
		nextLevel = list()
		for node in thisLevel:
			if node.left: nextLevel.append(node.left)
			if node.right: nextLevel.append(node.right)
		thisLevel = nextLevel
	return levels