import os
import json
from datetime import datetime, timedelta
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_post(post):
    # 공유수
    if 'shares' not in post:
        post['count_shares'] = 0
    else:
        post['count_shares'] = post['shares']['count']

    #전체 리액션 수
    if 'reactions' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']

    #전체 코멘트 수
    if 'commetns' not in post:
        post['count_comments'] = 0
    else:
        post['count_commects'] = post['comments']['summary']['total_count']

    # KST = UTC + 9
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')


def crawling(pagename, since, until, fetch=True):
    results = []
    filename = '%s/%s_%s_%s.json' % (
        RESULT_DIRECTORY,
        pagename,
        since,
        until)

    if fetch:
        for posts in api.fb_fetch_posts(pagename, since, until):
            for post in posts:
                preprocess_post(post)

            results += posts

        # save results to file(저장/적재)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(
                results,
                indent=4,
                sort_keys=True,
                ensure_ascii=False)
            outfile.write(json_string)

    return filename


if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)
