'''
两个大数相加
'''
'''
两个大数相加
'''


def func():
    while 1:
        try:
            caseNumber = int(input("请输入测试用例个数:"))
            if caseNumber <= 0:
                print('输入错误，请重试！')
                return
            # 初始化列表
            tmpList = [['0'] * 2 for _ in range(caseNumber)]
            for i in range(caseNumber):
                tmpArray = input("请输入两个加数，加数与加数之间用空格分隔:").strip().split()
                if len(tmpArray) != 2:
                    continue
                tmpList[i][0] = tmpArray[0]
                tmpList[i][1] = tmpArray[1]

            # 循环遍历求和
            if len(tmpList) > 0:
                for i, item in enumerate(tmpList):
                    a = item[0]
                    b = item[1]
                    c = add(a, b)
                    print("Case %s:" % (i + 1))
                    print("%s+%s=%s" % (a, b, c))

        except EOFError:
            break


def add(a, b):
    a_resever_temp = a[::-1]
    b_resever_temp = b[::-1]
    min_len = min(len(a_resever_temp), len(b_resever_temp))
    # 定义一个变量用于存储每次相加的进位
    step_number = 0
    # 定义一个字符串变量用于拼接相加的字符串
    result = ''
    # 求最小位数字相加之和
    for i in range(0, min_len):
        current_number = (ord(a_resever_temp[i]) - ord('0')) + (ord(b_resever_temp[i]) - ord('0')) + step_number
        step_number = current_number // 10  # 相加得到的进位数字
        current_number = current_number % 10
        result += str(current_number)
    if len(a_resever_temp) < len(b_resever_temp):
        a_resever_temp = b_resever_temp
    for j in range(min_len, len(a_resever_temp)):
        current_number = ord(a_resever_temp[j]) - ord('0') + step_number
        step_number = current_number // 10  # 相加得到的进位数字
        current_number = current_number % 10  #
        result += str(current_number)
    # 处理最后一个进位
    if step_number > 0:
        result += str(step_number)
    # 对处理之后的数字进行反转返回
    return result[::-1]


if __name__ == '__main__':
    func()
