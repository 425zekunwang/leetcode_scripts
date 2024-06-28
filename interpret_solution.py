import traceback

import requests
import json
from settings import *


url = "https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i/interpret_solution/"


def get_interpret_solution_data(lang,question_id,typed_code,data_input):
    data = {
        "lang": lang,
        "question_id": question_id,
        "typed_code": typed_code,
        "data_input": data_input
    }
    # data = {
    #     "lang": "csharp",
    #     "question_id": "3461",
    #     "typed_code": "class Solution {\n    public int minimumArea(int[][] grid) {\n        int m = grid.length, n = grid[0].length;\n        int startRow = Integer.MAX_VALUE, endRow = Integer.MIN_VALUE, startCol = Integer.MAX_VALUE, endCol = Integer.MIN_VALUE;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (grid[i][j] == 1) {\n                    startRow = Math.min(startRow, i);\n                    endRow = Math.max(endRow, i);\n                    startCol = Math.min(startCol, j);\n                    endCol = Math.max(endCol, j);\n                }\n            }\n        }\n        return (endRow - startRow + 1) * (endCol - startCol + 1);\n    }\n}",
    #     "data_input": "[[0,1,0],[1,0,1]]\n[[1,0],[0,0]]"
    # }

    return json.dumps(data, separators=(',', ':'))

def interpret_solution(data):
    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        if response.status_code==200:
            return response.json()
        elif response.status_code == 409:
            raise Exception("提交动作频繁")
        else:
            raise Exception("interpret_solution >>异常的响应码:",response.status_code)
    except:
        print(traceback.format_exc())
        return None

    # {
    #     "interpret_id": "runcode_1719543932.228726_3EYv42qb0k",
    #     "test_case": "[[0,1,0],[1,0,1]]\n[[1,0],[0,0]]",
    #     "interpret_expected_id": "runcode_expected_1719543932.228726_3EYv42qb0k"
    # }