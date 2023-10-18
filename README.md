# transactionSorting
Creates an efficient Left Leaning Red-Black Binary Search Tree to sort streams of transactions based upon trade value. This program was for a University CWK and achieved some of the highest speeds from those who did the course - in our tests inputting 1M data points in only 5 seconds.

This program was written to handle a large number of transactions in a minimal complexity. The time complexity for adding transactions is therefore O(2log2(N)) and the space complexity O(N) with an additional O(1) stored.
