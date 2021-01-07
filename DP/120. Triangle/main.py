# Button up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row_len = len(triangle)
        path_sum = [] # store path sum of each row
        
        # calculate  path sum from buttom row
        for row_idx in range(row_len-1, -1, -1):
            path_sum_row = triangle[row_idx][:]
            if path_sum:
                for i in range(len(path_sum_row)):
                    path_sum_row[i] += min(
                        path_sum[-1][i],
                        path_sum[-1][i+1]
                    )
                    
            path_sum.append(path_sum_row)
        
        return path_sum[-1][0]