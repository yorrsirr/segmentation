# -*- coding:utf-8 -*-
from Tkinter import *
import time
import MM

root = Tk()
root.title('快想个组名')
root.geometry('480x420')

Label(root, text='中文分词实验').pack()

insert_text = Text(root, height=10)
insert_text.pack()


button_fram = Frame(root, height=5)

##MM_button
seg_text = ''
on_hit = False  # 默认初始状态为 False


def FMM_hit_me():
    row_text = insert_text.get("0.0", "end")
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        start_time = time.clock()
        output_text.insert('insert', '(FMM)' + MM.fmm(row_text))
        end_time = time.clock()
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        output_text.insert('end','') # 设置 文字为空
    seg_time = end_time - start_time
    Label(root, text='FMM分词所用时间为' + str(seg_time) + 's').pack()

def BMM_hit_me():
    row_text = insert_text.get("0.0", "end")
    row_text = row_text.replace('\n', '')
    # text1 = MM.bmm(u"判断当前字符串是否在词典中并不存在，若该字符串从头切割到尾都没有词典中的词则认为无法切割并且")
    # print text1
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        start_time1 = time.clock()
        output_text.insert('insert', '(BMM)' + MM.bmm(row_text) + '\n')
        end_time1 = time.clock()
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        output_text.insert('end', '') # 设置 文字为空
    seg_time = end_time1 - start_time1
    Label(root, text='BMM分词所用时间为' + str(seg_time) + 's').pack()

def RMM_hit_me():
    row_text = insert_text.get("0.0", "end")
    row_text = row_text.replace('\n', '')
    # text1 = MM.bmm(u"判断当前字符串是否在词典中并不存在，若该字符串从头切割到尾都没有词典中的词则认为无法切割并且")
    # print text1
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        start_time1 = time.clock()
        output_text.insert('insert', '(RMM)' + MM.rmm(row_text) + '\n')
        end_time1 = time.clock()
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        output_text.insert('end', '') # 设置 文字为空
    seg_time = end_time1 - start_time1
    Label(root, text='RMM分词所用时间为' + str(seg_time) + 's').pack()


##FMM_button
Button(button_fram, text='FMM分词', command=FMM_hit_me).pack(side=LEFT)
##RMM_button
Button(button_fram, text='RMM分词', command=RMM_hit_me).pack(side=RIGHT)
##BMM_button
Button(button_fram, text='BMM分词', command=BMM_hit_me).pack(side=RIGHT)

button_fram.pack()


output_text = Text(root, height=10)
output_text.pack()

root.mainloop()
