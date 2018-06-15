# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBAA0Jg0TC8TnaIoZAZCjDCLmHN4XZCWtgD4ZBRZBSGsuKJrLoavTYQqnMxzgOliMAqV9DZCLoLbPKRcbxw17tXj5aWa60TPl6ypZB22A4ZAeWReyAz4P7TIIKzblsrHCdfI7GNRnKZB9f2L2EN6ytdCM1tGWR3aZCwozFkxTMWQriw4jGVTznxLRysZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"


def fb_gen_url(
        base=BASE_URL_FB_API,
        node='',
        **params):
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url


def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename)+"/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN)

    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get("next")
        isnext = url is not None

        yield posts


