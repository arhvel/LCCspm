# LCCspm
l-Length Closed Contiguous Sequential Pattern Mining Algorithm.

This algorithm is for mining closed contiguous patterns using a sliding window (i.e. maximal length) and an absolute support threshold. 

The algorithm has three main module for candidate generation, pruning and for checking closed contiguous patterns.

The candidate generation module uses a snippet growth method to generate all contiguous patterns from 1 to the user-specified length.

The pruning module uses the support threshold to select patterns that meets the criterion and stores them in a dictionary data structure which ensures uniqueness.

The closed contiguous patterns module check for closed patterns among the pruned patterns.

LCCspm is empirically proven to be faster than CCSpan algorithm and also uses lesser memory space.
