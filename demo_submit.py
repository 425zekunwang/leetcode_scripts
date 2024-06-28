# https://leetcode.cn/contest/weekly-contest-403/
from check import check
from submit import submit,get_submit_data
from get_quesstion_id import get_question_id_by_name
java_code='''class Solution {
    public int minimumArea(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int startRow = Integer.MAX_VALUE, endRow = Integer.MIN_VALUE, startCol = Integer.MAX_VALUE, endCol = Integer.MIN_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    startRow = Math.min(startRow, i);
                    endRow = Math.max(endRow, i);
                    startCol = Math.min(startCol, j);
                    endCol = Math.max(endCol, j);
                }
            }
        }
        return (endRow - startRow + 1) * (endCol - startCol + 1);
    }
}'''
# https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i/
question_id=get_question_id_by_name("find-the-minimum-area-to-cover-all-ones-i")
submit_data=get_submit_data(
    lang="java",
    question_id=question_id,
    typed_code=java_code
)

submit_result=submit(submit_data)
submit_id=submit_result["submission_id"]

check_result=check(submit_id)
print(check_result)