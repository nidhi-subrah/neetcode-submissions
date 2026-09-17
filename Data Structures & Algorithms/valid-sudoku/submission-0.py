class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen=set()

        for r in range(9):
            for c in range(9):
                num=board[r][c]
        
                if num==".":
                    continue

                row_val=("row", r, num)
                col_val=("col", c, num)
                box_val=("box", r//3, c//3, num)

                if row_val in seen or col_val in seen or box_val in seen:
                    return False
        
                seen.add(row_val)
                seen.add(col_val)
                seen.add(box_val)

        return True






                

                
        