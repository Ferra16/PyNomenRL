__author__ = 'Twelve'

import re


def ad(text):
    x = 0
    if len(list) is not 0:
        lastitem = list[-1]
        if (re.search('\(\d+\)', list[-1])) is not None:
            xx = re.search('\(\d+\)', list[-1]).group()
            x = int(xx[1:-2])
            #x = int(re.search(r'\d+', xx).group())
            lastitem1 = re.split(r'\:', lastitem)

            if text == lastitem1[0]:
                x += 1
                text = text + " :(%d)" % x

    list.append(text)