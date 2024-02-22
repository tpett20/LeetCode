# 997. Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
    # The town judge trusts nobody.
    # Everybody (except for the town judge) trusts the town judge.
    # There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        possible_judges = set(range(1, n + 1))
        for pair in trust:
            possible_judges.discard(pair[0])
        if len(possible_judges) != 1:
            return -1
        judge = list(possible_judges)[0]
        judge_trusters = set()
        for pair in trust:
            if pair[1] == judge:
                judge_trusters.add(pair[0])
        if len(judge_trusters) != (n - 1):
            return -1
        return judge

s = Solution()
print(s.findJudge(2, [[1,2]]))
print(s.findJudge(3, [[1,3], [2,3]]))
print(s.findJudge(3, [[1,3], [2,3], [3,1]]))