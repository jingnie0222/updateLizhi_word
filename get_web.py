import datetime
import pymysql
from urllib.parse import quote


def get_web_word(vrid, web_query_file):
    """
    :param vrid: str
    :param web_query_file: str
    :return: NONE
    """

    print("GETTING Web Word")
    web_db = pymysql.connect(host="hosttip", user="openread", passwd="openread", db="pcvrquery", charset="utf8")
    web_corsur = web_db.cursor()
    now_time = datetime.datetime.now()
    word_count = 50


    delta1 = datetime.timedelta(days=2)
    delta2 = datetime.timedelta(days=3)
    time_str1 = now_time - delta1
    time_str2 = now_time - delta2
    table_name1 = "pcvrquery_" + time_str1.strftime('%Y%m%d')
    table_name2 = "pcvrquery_" + time_str2.strftime('%Y%m%d')
    sql_str = "(select query from " + table_name1 \
              + " where vrid=\"" + vrid \
              + "\" order by pv desc limit " + str(word_count) \
              + ") union " \
              + "(select query from " + table_name2 \
              + " where vrid=\"" + vrid \
              + "\" order by pv desc limit " + str(word_count) \
              + ") limit " + str(word_count) + ";"

    web_corsur.execute(sql_str)
    result = web_corsur.fetchall()

    if len(result) > 20:
        with open(web_query_file, 'w+', encoding='gbk', errors='ignore') as f:
            f.write("QUERY\n")
            for element in result:
                write_str = quote(element[0]) + "\n"
                f.write(write_str)


if __name__ == '__main__':

    vrid_lst = "50024801"
    get_web_word(vrid_lst, './yyy.csv')