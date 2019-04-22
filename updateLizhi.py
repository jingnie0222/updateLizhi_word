#!/usr/bin/python3
# -*-codig=utf8-*-

"""
__author__ = 'yinjingjing'
__mtime__ = '2019/2/18'
"""

import os
import requests
from get_web import get_web_word

lizhi_vrid = ['50022101', '50022201', '50023601', '50024701', '50024801']

for file in os.listdir():
    if ".csv" == os.path.splitext(file)[-1]:
        os.remove(file)

for vrid in lizhi_vrid:
    file_name = "./" + vrid + ".csv"
    get_web_word(vrid, file_name)


try:
    os.rename("50022101.csv", "[140385][1]50022101.csv")
    os.rename("50022201.csv", "[136762][1]50022201.csv")
    os.rename("50023601.csv", "[140387][1]50023601.csv")
    os.rename("50024701.csv", "[125146][1]50024701.csv")
    os.rename("50024801.csv", "[140386][1]50024801.csv")

    in_file1 = {"file": open('[140385][1]50022101.csv', 'rb')}
    ret = requests.post('http://pagetest.sogou-inc.com/update_file.php', files=in_file1)
    print("15_300_1: %s" % ret.text)

    in_file2 = {"file": open('[136762][1]50022201.csv', 'rb')}
    ret = requests.post('http://pagetest.sogou-inc.com/update_file.php', files=in_file2)
    print("15_300_2: %s" % ret.text)

    in_file7 = {"file": open('[140387][1]50023601.csv', 'rb')}
    ret = requests.post('http://pagetest.sogou-inc.com/update_file.php', files=in_file7)
    print("15_300_7: %s" % ret.text)

    in_file13 = {"file": open('[125146][1]50024701.csv', 'rb')}
    ret = requests.post('http://pagetest.sogou-inc.com/update_file.php', files=in_file13)
    print("15_300_13: %s" % ret.text)

    in_file14 = {"file": open('[140386][1]50024801.csv', 'rb')}
    ret = requests.post('http://pagetest.sogou-inc.com/update_file.php', files=in_file14)
    print("15_300_14: %s" % ret.text)

except Exception as err:
    print(err)
