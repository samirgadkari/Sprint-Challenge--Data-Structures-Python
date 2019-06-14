Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1)

2. What is the space complexity of your ring buffer's `append` function?

O(1)

3. What is the runtime complexity of your ring buffer's `get` method?

O(n)

4. What is the space complexity of your ring buffer's `get` method?

O(n)

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2)

6. What is the space complexity of the provided code in `names.py`?

O(n) or to be more accurate O(2n), but we usually say O(n), as n gets very large.

7. What is the runtime complexity of your optimized code in `names.py`?

Let's say n is the number of names in the list.

I have implemented a Suffix Tree data structure. If the tree is balanced, the runtime complexity is:
 * O(n) for creating the Suffix Tree
 * O(log n) for searching the tree
So to run this code for both creating and searching the tree is O(n)

I'm thinking, with 10000 proper names, the tree will be balanced.

8. What is the space complexity of your optimized code in `names.py`?

Since we have to save each character, the space complexity is:
O(n * m) where:
 * n is the length of the list of names
 * m is the average length of the name in this list
 
