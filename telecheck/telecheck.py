# -*- coding: utf-8 -*-
import itertools
from art import tprint
import random
import time
import requests
import string
import os
import datetime

ValidLetters=string.ascii_letters+string.digits+"_"
DigitList=[str(i+1) for i in range(9)]
DigitList.append("")
version="0.1"
def line(char="*",number=30):
    print(char*number)
def create_random_sleep(index=1,min_time=0.25,max_time=3):
    '''
    This function generate sleep time with random processes
    :param index: index to determine first page  and messages(index = 0 is for first page)
    :param min_time: minimum time of sleep
    :param max_time: maximum time of sleep
    :type index:int
    :type min_time:int
    :type max_time:int
    :return: time of sleep as integer (a number between max and min)
    '''
    if index==0:
        time_sleep = 1
    else:
        time_sleep = random.uniform(min_time, max_time)
    return time_sleep

def TIR_help_func():
    '''
    Print Help Page
    :return: None
    '''
    tprint("telecheck")
    tprint("v"+version)
    print("You can use a-z,0-9 and underscores: \n")
    print("Help : \n")
    print("     - all 'your_keywords' --> (All Users) Example : 'python -m telecheck all keyword1,keyword2,keyword3'\n")
    print("     - bot 'your_keywords' --> (Bot Users) Example : 'python -m telecheck bot keyword1,keyword2,keyword3'\n")

def id_check(input_id):
    try:
        response = requests.get("https://t.me/" + input_id)
        html = response.text
        if "tgme_page_extra" in html:
            return False
        else:
            return True
    except Exception:
        print("[Error] Getting " + input_id + " Information")
def filter_keyword(keywords):
    filtered_keywords=list(keywords)
    try:
        for item in keywords:
            for i in item:
                if i not in ValidLetters:
                    filtered_keywords.remove(item)
                    break
        return filtered_keywords
    except Exception :
        return keywords

def filter_id(tuple_id):
    test_id="".join(list(tuple_id))
    if (len(test_id)>5) and ("__" not in test_id):
        return test_id

def id_list_gen(keywords,mode="all"):
    search_list = list(keywords)
    search_list.append("")
    first_list=list(filter(lambda x: not x.isdigit(), keywords))
    if mode=="all":
        generated_tuple = list(itertools.product(first_list, ["", "_"], search_list, ["", "_"], keywords,DigitList))
    else:
        generated_tuple = list(itertools.product(first_list, ["", "_"], search_list, ["", "_"], search_list, ["", "_"],DigitList,["bot"]))
    result = list(map(filter_id, generated_tuple))
    result=list(filter(None, result))
    return result

def run(input_id):
    time.sleep(create_random_sleep())
    if id_check(input_id)==True:
        print(input_id)
        return input_id

def save_id(data,list_len):
    filtered_data=list(filter(None, data))
    ValidLength=str(len(filtered_data))
    if list_len==0:
        print("No Valid Username!!(Choose Better Keywords)")
    elif ValidLength=="0":
        print("No Available Username!!!")
    line()
    print("Total Valid Usernames : " + str(list_len))
    print("Available Usernames : " + ValidLength)
    line()
    file=open("TIR_ID.log","w")
    file.write(str(datetime.datetime.now())+"\n")
    file.write("Total : "+str(list_len)+"\n")
    file.write("Valid Usernames : "+ValidLength+"\n")
    file.write("\n".join(filtered_data))
    file.close()
    print("Log File --> "+os.getcwd())

