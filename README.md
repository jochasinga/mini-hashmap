# mini-hashmap

An implementation of hashmap based on Python array and deque.

## use

`HashMap.put([key, val])` save the entry to the hashmap. It iterates the underlying queue to find a duplicate and delete that beforehand.

`HashMap.get([key])` retrieve the latest value with the corresponding key.