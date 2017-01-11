from langdetect import detect
from translate import Translator


ch_language_code = {u'繁体中文': 'zh-TW',
                    u'中文': 'zh',
                    u'简体中文': 'zh',
                    u'英语': 'en',
                    u'日语': 'ja',
                    u'法语': 'fr'}


def translate2(msg, targetl='zh'):
    """
    Translate from one language to another language. If sourcel is the same as targetl, then tranlate it to ch-TW.
    :param targetl: language abbreviation.
    :param msg: message.
    :return: message in another language.
    """
    sourcel = detect(msg)
    # print(sourcel)
    if detect(targetl) in ('zh', 'zh-TW', 'zh-cn') or targetl in ('zh', 'zh-TW', 'zh-cn'):
        try:
            targetl_ = ch_language_code[targetl] if targetl in ch_language_code.keys() else targetl
            # print(targetl)
        except:
            return 'No this language available!'
    else:
        print(detect(targetl))  #DEBUG
        targetl_ = targetl if targetl != sourcel else 'zh-TW'

    translator = Translator(to_lang=targetl_, from_lang=sourcel)
    translation = translator.translate(msg)
    return translation




if __name__ == '__main__':

    print(translate2(u'翻译 what is this? Can you understand me?', u'中文'))
