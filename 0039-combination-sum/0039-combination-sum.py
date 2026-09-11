class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        candidates.sort()

        def backtrack(start, target, current):
            if target == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > target:
                    break

                current.append(num)

              
                backtrack(i, target - num, current)

                current.pop()

        backtrack(0, target, [])

        return result