#-*- coding:utf-8 -*-
import codecs
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import time


#正向最大匹配算法fmm算法
#获取最大词长
def fmm(words_in):
    # 将字典存储为列表words_Str
    dic = []
    with open('chineseDic.txt', 'r') as f:
        line = f.readline().decode('gbk')
        while line:
            dic.append(line.split(',')[0])
            line = f.readline().decode('gbk')
    f.close()
    max_Len = 0
    for each in dic:
        if len(each) > max_Len:
            max_Len = len(each)

    #words[]用来存储分词结果
    words = []
    n = 0
    while n < len(words_in):
        matched = 0
        for i in xrange(max_Len, 0, -1):
            s = words_in[n:n+i]
            for each in dic:
                if s == each:
                    words.append(s)
                    n = n + i
                    matched = 1
        if not matched:
            words.append(words_in[n])
            n = n + 1
    words_out = ''
    for each in words:
        words_out = words_out + each + ' '
    return words_out

#逆向最大匹配算法bmm
def bmm(words_in):
    # 将字典存储为列表words_Str
    dic = []
    with open('chineseDic.txt', 'r') as f:
        line = f.readline().decode('gbk')
        while line:
            dic.append(line.split(',')[0])
            line = f.readline().decode('gbk')
    f.close()
    max_Len = 0
    for each in dic:
        if len(each) > max_Len:
            max_Len = len(each)

    #words[]用来存储分词结果
    words = []
    n = len(words_in)
    while n > 0:
        matched = 0
        for i in range(6, 0, -1):
            s = words_in[n-i:n]
            for each in dic:
                if s == each:
                    words.append(s)
                    n = n - i
                    matched = 1
                    break
        if not matched:
            words.append(words_in[n])
            n = n - 1

    #words逆向输出
    words.reverse()
    words_out = ''
    for each in words:
        words_out = words_out + each + ' '
    return words_out

#双向最大匹配算法rmm
# 启发式规则：
#     1.如果正反向分词结果词数不同，则取分词数量较少的那个。
#     2.如果分词结果词数相同
#                  a.分词结果相同，就说明没有歧义，可返回任意一个。
#                  b.分词结果不同，返回其中单字较少的那个。
def rmm(words_in):
    len_fmm = len(fmm(words_in).split())
    len_bmm = len(bmm(words_in).split())
    words_fmm = fmm(words_in)
    words_bmm = bmm(words_in)

    if len_fmm < len_bmm:
        return words_fmm
    elif len_fmm > len_bmm:
        return words_bmm
    else:
        if words_fmm == words_bmm:
            return words_fmm
        else:
            single_fmm = 0
            for each in words_fmm.split():
                if len(each) == 1:
                    single_fmm = single_fmm + 1
            single_bmm = 0
            for each in words_bmm.split():
                if len(each) == 1:
                    single_bmm = single_bmm + 1
            if single_fmm <= single_bmm:
                return words_fmm
            else:
                return words_bmm


# words_in = u"我们即将以丰收的喜悦送走牛年,以昂扬的斗志迎来虎年。"
# print rmm(words_in)
#
# print fmm(words_in)
# print bmm(words_in)