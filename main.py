import re
import sys
sys.path.append("ItChat-master")

import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response


@itchat.msg_register('Text')
def text_reply(msg):
    if u'作者' in msg['Text'] or u'主人' in msg['Text']:
        return u'我主人超级帅的！'
    elif u'源代码' in msg['Text'] or u'获取文件' in msg['Text']:
        itchat.send('@fil@main.py', msg['FromUserName'])
        itchat.send('Project: https://github.com/yhu20/WeChatBot/tree/master')
        return u'这就是现在机器人后台的代码，是不是很简单呢？'
    elif u'获取图片' in msg['Text'] or u'自拍' in msg['Text']:
        itchat.send('@img@irobot.jpg', msg['FromUserName']) # there should be a picture
    elif u'翻译' in msg['Text'] or u'translate' in msg['Text']:
        # print(msg['Text'])
        raw_text = re.split(':|：', msg['Text'], 1)
        # targetlan = raw_text[0]
        text = raw_text[-1]

        from api import ggtrans

        return ggtrans.translate2(text)
    else:
        return get_response(msg['Text']) or u'收到：' + msg['Text']


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': u'图片', 'Recording': u'录音',
        'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
        u'已下载到本地') # download function is: msg['Text'](msg['FileName'])


@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']


@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        text = msg['Text'].split(' ')[1].strip()
        if u'作者' in text or u'主人' in text:
            return u'我主人超级帅的！'
        elif u'源代码' in text or u'获取文件' in text:
            itchat.send('@fil@main.py', msg['FromUserName'])
            return u'这就是现在机器人后台的代码，是不是很简单呢？'
        elif u'获取图片' in text or u'自拍' in text:
            itchat.send('@img@irobot.jpg', msg['FromUserName'])  # there should be a picture
            return u'这就是帅气的我！'
        elif u'翻译' in msg['Text'] or u'translate' in msg['Text']:
            # print(msg['Text'])
            raw_text = re.split(':|：', msg['Text'], 1)
            targetl = raw_text[0]
            text = raw_text[-1]
            from api import ggtrans
            return ggtrans.translate2(text)
        else:
            return u'@%s\u2005%s' % (msg['ActualNickName'],
                get_response(text) or u'收到：' + msg['Text'])


@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('glad to be friend', msg['RecommendInfo']['UserName'])


if __name__ == '__main__':
    itchat.auto_login(True, enableCmdQR=True)
    itchat.run()
