import traceback

import requests
import json
from settings import *

url = "https://leetcode.cn/graphql/"


def get_data(question_name):
    data = {
        "query": "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    categoryTitle\n  }\n}\n    ",
        "variables": {
            "titleSlug": question_name
        },
        "operationName": "questionTitle"
    }
    data = json.dumps(data, separators=(',', ':'))
    return data
#     data = {
#     "query": "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    categoryTitle\n  }\n}\n    ",
#     "variables": {
#         "titleSlug": "deep-dark-fraction"
#     },
#     "operationName": "questionTitle"
# }

def get_question_id_by_name(question_name):
    data=get_data(question_name)
    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        if response.status_code!=200:
            raise Exception(f"get_question_id_by_name >> 非法的响应码",response.status_code)
        return response.json()["data"]["question"]["questionId"]
    except:
        print(traceback.format_exc())
        return None