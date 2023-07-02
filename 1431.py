# 1431. Kids With the Greatest Number of Candies
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

def kidsWithCandies(candies, extraCandies):
    greatest = candies[0]
    for i in range(1, len(candies)):
        if candies[i] > greatest:
            greatest = candies[i]
    for i in range(len(candies)):
        if candies[i] + extraCandies >= greatest:
            candies[i] = True
        else: 
            candies[i] = False
    return candies

print(kidsWithCandies([2,3,5,1,3], 3))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12,1,12], 10))