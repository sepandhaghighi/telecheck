# -*- coding: utf-8 -*-
import re
import itertools
from functools import partial
import multiprocessing as mu
from art import tprint
import random
import time
import requests
import string

ValidLetters=string.ascii_letters+string.digits+"_"
version="0.1"
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
    tprint("TIR")
    tprint("v"+version)
    print("You can use a-z,0-9 and underscores: \n")
    print("Help : \n")
    print("     - all 'your_keywords' --> (All Users) Example : 'python -m TIR all keyword1,keyword2,keyword3'\n")
    print("     - bot 'your_keywords' --> (Bot Users) Example : 'python -m TIR bot keyword1,keyword2,keyword3'\n")

def id_check(input_id):
    try:
        response = requests.get("https://t.me/" + input_id)
        html = response.text
        if "tgme_page_extra" in html:
            return False
        else:
            return True
    except Exception as e:
        print("[Error] Getting " + input_id + " Information")
def filter_keyword(keywords):
    filtered_keywords=[]
    try:
        for item in keywords:
            for i in item:
                if i not in ValidLetters:
                    break
            filtered_keywords.append(item)
        return filtered_keywords
    except Exception :
        return keywords

def filter_id(tuple_id):
    id="".join(list(tuple_id))
    if len(id)>5:
        return id

def id_list_gen(keywords):
    search_list = list(keywords)
    search_list.append("")
    generated_tuple = list(itertools.product(search_list, ["", "_"], search_list, ["", "_"], keywords,["", "_"]))
    result = list(map(filter_id, generated_tuple))
    result=list(filter(None, result))
    return result

def run(id):
    time.sleep(create_random_sleep())
    if id_check(id)==True:
        print(id)
