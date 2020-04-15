# -*- coding: UTF-8 -*-
# 文件多行不同判断


def clean(line, num):
    while num < line.__len__() and line[num].strip() == '':
        num = num + 1
    return num


def logic(c):
    # 最后一行
    if c.trueNum + 1 == c.trueLine.__len__() or c.falseNum + 1 == c.falseLine.__len__():
        return False
    # 中间行
    else:
        temp1 = c.trueNum
        temp2 = c.falseNum
        clean(c.trueLine, temp1)
        clean(c.falseLine, temp2)
    if c.trueLine[temp1 + 1].replace(' ', '') == c.falseLine[temp2 + 1].replace(' ', ''):
        return True
    else:
        return False


# 少了一些行
def lessTrue(c):
    temp1 = c.falseNum + 1
    temp1 = clean(c.falseLine, temp1)
    temp2 = c.trueNum + 1
    temp2 = clean(c.trueLine, temp2)
    temp3 = temp2 + 1
    temp3 = clean(c.trueLine, temp3)
    while temp3 != c.trueLine:
        if c.trueLine[temp2].replace(' ', '') == c.falseLine[c.falseNum].replace(' ', '') and \
                c.trueLine[temp3].replace(' ', '') == c.falseLine[temp1].replace(' ', ''):
            return temp2
        else:
            temp2 = temp2 + 1
            temp2 = clean(c.trueLine, temp2)
            temp3 = temp2 + 1
            temp3 = clean(c.trueLine, temp3)
    return -3


def check(c):
    # 去空行
    answerDict = {}
    clean(c.trueLine, c.trueNum)
    clean(c.falseLine, c.falseNum)
    while c.trueNum < c.trueLine.__len__() and c.falseNum < c.falseLine.__len__():
        # 相同行继续
        if c.trueLine[c.trueNum].replace(' ', '') == c.falseLine[c.falseNum].replace(' ', ''):
            c.trueNum = c.trueNum + 1
            c.falseNum = c.falseNum + 1
        # 不同行
        else:
            # 判断是否为逻辑错误
            if logic(c):
                answerDict[c.falseNum] = 0
                c.trueNum = c.trueNum + 1
                c.falseNum = c.falseNum + 1
            else:
                lessReturn = lessTrue(c)
                if lessReturn != 0:
                    answerDict[c.falseNum] = lessReturn - c.trueNum
                    c.trueNum = lessReturn + 1
                    c.falseNum = c.falseNum + 1
        c.trueNum = clean(c.trueLine, c.trueNum)
        c.falseNum = clean(c.falseLine, c.falseNum)
    # 运行到最后有剩余行
    # 正确程序还有剩余行
    if c.trueNum == c.trueLine.__len__() and c.falseNum != c.falseLine.__len__():
        answerDict[c.falseNum] = -1
    # 错误程序还有剩余行
    elif c.falseNum == c.falseLine.__len__() and c.trueNum != c.trueLine.__len__():
        answerDict[c.falseNum] = -2
    return answerDict


class CheckCode:
    def __init__(self):
        pass

    trueLine = []
    falseLine = []
    trueNum = 0
    falseNum = 0


# path1:正确程序列
# path2:错误程序列
# checkDir:错误行数字典
#       key:    错误行数
#       value:  0       //单行逻辑错误
#               -1      //正确程序有剩余行
#               -2      //错误程序有剩余行
#               -3      //多行缺失，可能存在问题
#               其他正数 //相较于正确程序的缺失行数
def checkMain(line1, line2):
    ck = CheckCode()
    ck.trueLine = line1
    ck.falseLine = line2
    checkDict = check(ck)
    return checkDict
