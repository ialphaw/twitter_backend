import re

def get_hashtag(body):
    m = re.findall(r'[#]\w+', body)
    return m
