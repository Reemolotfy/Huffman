Huffman encoding/decoding
Name: Reem Moustafa Lotfy 

The provided code is an implementation of Huffman encoding and decoding in Python. 
Huffman coding is a compression algorithm that assigns variable-length codes to characters based on 
their frequencies in a given data set, with more frequently occurring characters having shorter codes. I 
will provide a brief explanation of the code's functionality and then proceed to write the documentation 
for it.
The code begins by opening a file named "data.txt" and reading its contents into the `data` variable. It 
then defines a class called `NodeTree`, representing nodes in the Huffman tree, with `left` and `right` 
attributes for storing child nodes. The class also provides methods for accessing children and nodes, as 
well as a string representation of the node.
The `huffman_code_tree` function is the main implementation of Huffman coding. It takes a `node` 
parameter, representing a node in the Huffman tree, and recursively generates a dictionary of 
characters and their corresponding binary codes. The function traverses the tree from the given node 
and assigns '0' or '1' to the binary string based on whether it goes to the left or right child. When it 
reaches a leaf node (represented by a string), it adds the character and its binary code to the dictionary. 
The function returns the dictionary containing the Huffman codes.
Next, the code calculates the frequency of each character in the `data` string and sorts them in 
descending order. The frequencies are stored in a list of tuples called `nodes`, where each tuple consists 
of a character and its frequency.
The code then constructs the Huffman tree by repeatedly combining the two nodes with the lowest 
frequencies into a new node until only one node remains. This is achieved by creating a `NodeTree` 
object with the two lowest frequency nodes as its children and adding it back to the `nodes` list with the 
combined frequency. The `nodes` list is sorted after each iteration to maintain the order.
After constructing the Huffman tree, the code generates the Huffman codes for each character by 
calling the `huffman_code_tree` function with the root node of the tree. It then prints the characters 
and their corresponding Huffman codes.
The code further encodes the `data` string using the generated Huffman codes. It opens a file named 
"coded data.txt" in write mode and writes the encoded binary representation of each character to the 
file.
Finally, the code demonstrates decoding by reading the encoded binary data from the file "coded 
data.txt" and attempting to decode it back to the original characters. The decoding process is done by 
traversing the Huffman tree based on each bit of the binary data. When a leaf node (character) is 
reached, it is printed as part of the decoding process.
Please note that the code contains commented-out sections related to printing the Huffman tree 
structure and an alternative decoding function that is not currently active.

This code provides a Python implementation of Huffman encoding and decoding. Huffman coding is a 
compression algorithm that assigns variable-length codes to characters based on their frequencies in a 
given data set, allowing more frequent characters to have shorter codes.
Usage:
1. Ensure the "data.txt" file exists and contains the data to be encoded.
2. Execute the code to perform Huffman encoding and write the encoded data to "coded data.txt".
3. Execute the code to perform Huffman decoding and print the decoded characters.
