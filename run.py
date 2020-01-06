# -*- encoding=utf8 -*-
__author__ = "song"

import sys
from airtest.core.api import *





#获取py文件
def get_file_path(root_dir='./case', suffix='.py', condition=None, exclude=None)->list:
    """Return dir path of specify file.
        :param str root_dir: search path.
        :param str suffix: file extension.
        :param str or list condition: Keyword of condition.
        :param str or list  exclude: filter of exclude
        :return:
        """
    res = list()
    cond = None
    excl = None

    def is_condition(cond, file):
        for c in cond:
            if c.lower() in file:
                continue
            else:
                return False
        return True

    def is_exclude(exc, file):
        for e in exc:
            if e.lower() in file:
                return False
        return True
    #获取文件
    def get_file(root_dir=None, suffix=None, condition=None, exclude=None):
        if not isinstance(exclude, str) and not isinstance(exclude, list):
            print('Invalid exp format.')
            sys.exit(1)
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                tmpfile = os.path.join(root, file).lower()
                if os.path.splitext(file)[1] == suffix:
                    if is_condition(condition, tmpfile) and is_exclude(exclude, tmpfile):
                        res.append(os.path.join(root, file))

    if not condition:
        condition = suffix
    if not exclude:
        exclude = ' '
    if root_dir != './' and root_dir != '.':
        root_dir = root_dir.strip('./').lower()
        for root, dirs, files in os.walk('.'):
            if root.strip('./').lower() == root_dir:
                root_dir = root
                break
    if isinstance(condition, str):
        cond = [condition]
    elif isinstance(condition, list):
        cond = condition
    if isinstance(exclude, str):
        excl = [exclude]
    elif isinstance(exclude, list):
        excl = exclude
    if not isinstance(cond, list) or not isinstance(excl, list):
        print("Invalid condition format.")
        sys.exit(1)
    get_file(root_dir=root_dir, suffix=suffix, condition=cond, exclude=excl)

    return list(set(res))


#执行py文件
def exec_py() -> bool():
    try:
        file = []     #过滤执行文件
        for i in get_file_path():
            if 'base.py' not in i and 'run.py' not in i:
                file.append(i)
            else:
                continue
        for file in file:
            os.system("python {0}".format(file))
            print(file)
    except Exception as e:
        print(e)
        return False
    return True


if __name__=="__main__":
    #执行全部用例
    exec_result = exec_py()
    if exec_result:
        print("-----------------全部流程测试结束,测试结果请看测试报告-----------------")



