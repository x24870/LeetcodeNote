# use built-in function
class Solution:
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if matrix[i] and matrix[i][-1] > target:
                return target in matrix[i]
        return False

# first try, ugly
class Solution:
    def searchMatrix(self, matrix, target):
        row_l, row_r = 0, len(matrix)
        while row_l < row_r:
            row_mid = (row_r - row_l)//2 + row_l
            if matrix[row_mid] and matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
                # search if target in this row
                print(row_mid)
                l, r = 0, len(matrix[row_mid])
                while l < r:
                    mid = (r - l)//2 + l
                    if matrix[row_mid][mid] == target:
                        return True
                    elif matrix[row_mid][mid] < target:
                        l = mid + 1
                    else:
                        r = mid
                break
            elif matrix[row_mid] and target < matrix[row_mid][-1]:
                row_r = row_mid
            else:
                row_l = row_mid + 1
        return False

# Treat matrix as a array
class Solution:
    def searchMatrix(self, matrix, target):
        height = len(matrix)
        if not height: return False

        width = len(matrix[0])
        l, r = 0, height * width

        while l < r:
            mid = (r - l)//2 + l
            row, col = mid // width, mid % width
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid
            else:
                l = mid + 1
        return False

