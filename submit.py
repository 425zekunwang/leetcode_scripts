import traceback

import requests
import json
from settings import  *
url = "https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements/submit/"




def get_submit_data(lang,question_id,typed_code):
    data = {
        "lang": lang,
        "question_id": question_id,
        "typed_code": typed_code
    }
#     data={
#     "lang": "cpp",
#     "question_id": "3471",
#     "typed_code": "class Solution {\npublic:\n    double minimumAverage(vector<int>& nums) {\n        vector<char> c(51,0);\n        for(const auto i:nums){\n            ++c[i];\n        }\n        char low = 1;\n        char high = 50;\n        double rt = 100;\n        while(1){\n            while(low<=high&&c[low]==0){\n                ++low;\n            }\n            if(low>high){break;}\n            while(low<=high&&c[high]==0){\n                --high;\n            }\n            if(low==high){\n                rt = min(rt,(double)low);\n                break;\n            }\n            rt = min(rt,(low+high)/2.0);\n            char d = min(c[low],c[high]);\n            c[low]-=d;\n            c[high]-=d;\n        }\n        return rt+1.0;\n    }\n};"
# }
    data = json.dumps(data, separators=(',', ':'))
    return  data

def submit(data):
    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        result=response.json()

        return result
    except:
        print(traceback.format_exc())
        return None