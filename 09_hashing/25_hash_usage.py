names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}
for name in names:
    # If countMap does not contain name
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1

'''
SUGGESTED PROBLEMS

https://leetcode.com/problems/contains-duplicate/

https://leetcode.com/problems/two-sum/

https://leetcode.com/problems/lru-cache/
'''