# 274. H-Index
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

def hIndex(citations):
    citations.sort()
    j = len(citations)
    for i in range(len(citations)):
        if citations[i] >= j:
            return len(citations) - i
        j -= 1
    return 0

print(hIndex([3,0,6,1,5]), 'Expected: 3')
print(hIndex([1,3,1]), 'Expected: 1')
print(hIndex([3,3]), 'Expected: 2')