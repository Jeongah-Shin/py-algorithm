# Best -  O(n)
# Average -  O(n^2)
# Worst - O(n^2)

def bubble_sort(seq):
    length = len(seq)-1
    for num in range(length, 0, -1):
        for i in range(num):
            if (seq[i] > seq[i+1]):
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq