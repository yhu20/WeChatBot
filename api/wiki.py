from wikiapi import WikiApi

client = WikiApi()

def wiki(msg):
    """
    Use wikipedia search engine to find information.
    :param msg: Text string
    :return:
    """
    results = client.find(msg)  # Returns all related key words in Wikipedia
    article = client.get_article(results[0])    # Returns the article of the user inputted key word
    return {'url': article.url,
            'summary': article.summary}


if __name__ == '__main__':
    result = wiki(u'毛泽东')
    import re
    s = re.split('.', result['summary'])
    print(result['summary'].split('.'))
    # for s_ in s:
        # print(s_)
    print(type(result['summary']))
    print(result['url'])
    print(type(result['url']))