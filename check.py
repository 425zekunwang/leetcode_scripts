import time

import requests
from settings import *



url = "https://leetcode.cn/submissions/detail/542537161/check/"


def get_check_url(submission_id):
    return f"https://leetcode.cn/submissions/detail/{submission_id}/check/"

def check(submission_id):

    while True:
        url=get_check_url(submission_id)
        # url = "https://leetcode.cn/submissions/detail/542536333/check/"
        response = requests.get(url, headers=headers, cookies=cookies)

        if response.status_code==200:
            result=response.json()
            state=result.get("state",None)
            if  state in  ["PENDING","STARTED"]:
                time.sleep(3)
                print("等待结果。。。")
                continue
            return response.json()

        else:
            return None