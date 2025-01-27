class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            temp = [1]*(i+1)
            result.append(temp)
            for j in range(1, i):
                result[i][j] = result[i-1][j] + result[i-1][j-1]
        return result


# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
