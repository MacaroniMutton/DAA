import heapq 

class node: 
    def __init__(self, freq, symbol): 
        self.freq = freq 
        self.symbol = symbol 
        self.left = None
        self.right = None
        self.huff = '' 

    def __lt__(self, nxt): 
        return self.freq < nxt.freq 

def printNodes(node, val=''): 
    newVal = val + str(node.huff) 
    if(node.left): 
        printNodes(node.left, newVal) 
    if(node.right): 
        printNodes(node.right, newVal) 
    if(not node.left and not node.right): 
        print(f"{node.symbol}:{node.freq} -> {newVal}") 
        
def huffman(chars, freq):
	nodes = [] 

	for x in range(len(chars)): 
		heapq.heappush(nodes, node(freq[x], chars[x])) 

	while len(nodes) > 1: 
		left = heapq.heappop(nodes) 
		right = heapq.heappop(nodes) 
		left.huff = 0
		right.huff = 1
		newNode = node(left.freq+right.freq, left.symbol+right.symbol)
		newNode.left = left
		newNode.right = right
		heapq.heappush(nodes, newNode) 
	return nodes[0]

def main():
	chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
	freq = [5, 9, 12, 13, 16, 45] 
	root = huffman(chars, freq)
	printNodes(root)
     
if __name__=='__main__':
     main()
