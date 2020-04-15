# -*- coding: UTF-8 -*-
# 制造多错误程序

import FindErrors


# path:文件路径
def getLine(path):
    file = open(path, 'r')
    return file.readlines()


# target:生成.c文件目标及错误信息文本路径
# path1:正确程序，用于对比
# path2:错误程序1
# path2：错误程序2
def makeMultipleErrorsFile(target, path1, path2, path3):
    line1 = getLine(path1)
    line2 = getLine(path2)
    line3 = getLine(path3)
    dict1 = FindErrors.checkMain(line1, line2)
    dict2 = FindErrors.checkMain(line1, line3)
    targetLine = []
    for i in range(0, line1.__len__()):
        if i in dict1.keys():
            num = int(dict1.get(i))
            if num == 0:
                targetLine.append(line2[i])
            elif num > 0:
                i = i + num
        elif i in dict2.keys():
            num = int(dict2.get(i))
            if num == 0:
                targetLine.append(line3[i])
            elif num > 0:
                i = i + num
        else:
            targetLine.append(line1[i])
    dicts = {}
    keys = []
    dicts.update(dict1)
    dicts.update(dict2)
    for key in dicts.keys():
        keys.append(key)
    keys.sort()
    targetFile1 = open(target + "/target.c", "w")
    targetFile2 = open(target + "/errorList", "w")
    for item in targetLine:
        targetFile1.write(item)
    for key in keys:
        if dicts.get(key) == 0:
            targetFile2.write(str(key + 1) + ":单行错误\n")
        else:
            targetFile2.write(str(key + 1) + ":从该行开始缺失了" + str(dicts.get(key)) + "行\n")


if __name__ == '__main__':
    makeMultipleErrorsFile("/home/kalasu/PycharmProjects/MultipleErrors",
                           "tot_info/true/tot_info.c",
                           "tot_info/v1/tot_info.c",
                           "tot_info/v2/tot_info.c")
