#huffman encoding
data_file = open("data.txt", "r")
data = data_file.read()
data_file.close()

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return  '%s_%s' % (self.left, self.right)


 # Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    d[node] = binString  # Add the current node with its binary string to the dictionary
    return d       

# Calculating frequency
freq = {}
for c in data:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#print(freq)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1] # last item in the array
    (key2, c2) = nodes[-2] # 2nd last item in the array
    nodes = nodes[:-2]     # everything except the last two items
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])


print(' Char | Huffman code ')
print(' ------------------- ')

for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
f = open('coded data.txt', 'w')

for char in data:
    f.write(huffmanCode[char])
f.close()

"""
# Function to print the Huffman tree
def print_huffman_tree(node, prefix=''):
    if type(node) is str:
        print(f"{prefix}└── {node}")
    else:
        print(f"{prefix}└── +")
        print_huffman_tree(node.left, prefix + "    ")
        print_huffman_tree(node.right, prefix + "    ")

# Call the print_huffman_tree function after generating the Huffman tree
print_huffman_tree(nodes[0][0])
"""

print("___________________________decoding_______________________________")
#---------------------------------------------------------------------------
#huffman decoding

f = open("coded data.txt", "r")
binary = f.read()
f.close()
"""
def decodeHuffman(root,binary):
    temp = root
    result = []
    
    for bit in binary:
        # traverse to the left
        if bit == "0":
            temp = temp.left
        
        # traverse to the right
        elif bit == "1":
            temp = temp.right 
        
        # check for leaf node
        #if temp.left == None and temp.right == None:
        if isinstance(temp, str):
            result.append(temp)
    temp=root        
        
    print(result)
    f = open('decoded data.txt', 'w')
    f.write("".join(result))
    f.close()           

decodeHuffman(nodes[0][0],binary)
"""
print("________________________________________________________________________")

# Function to decode the binary string
def huffman_decode(node,bit):
        if bit == "0":
            huffman_decode(node.left,bit)
        elif bit == "1":
            huffman_decode(node.right,bit)  
        if type(node) is str:
            print(node)
        

# Call the print_huffman_tree function after generating the Huffman tree
for bit in binary:
    huffman_decode(nodes[0][0],bit)




"""
Huffman Encoding and Decoding

This code provides a Python implementation of Huffman encoding and decoding. Huffman coding is a compression algorithm that assigns variable-length codes to characters based on their frequencies in a given data set, allowing more frequent characters to have shorter codes.

Usage:
1. Ensure the "data.txt" file exists and contains the data to be encoded.
2. Execute the code to perform Huffman encoding and write the encoded data to "coded data.txt".
3. Execute the code to perform Huffman decoding and print the decoded characters.

Classes:
- NodeTree: Represents a node in the Huffman tree. Each node can have a left and right child node.

Functions:
- huffman_code_tree(node, left=True, binString=''): Implements the main function for generating Huffman codes. Given a node in the Huffman tree, it recursively generates a dictionary of characters and their corresponding binary codes.
- huffman_decode(node, bit): Recursively dec
"""