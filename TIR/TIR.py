# -*- coding: utf-8 -*-
import re
import itertools
from functools import partial
import multiprocessing as mu
from art import tprint
import random
import time
import requests


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

def filter_id(tuple_id):
    id="".join(list(tuple_id))
    if len(id)>5:
        return id

def id_list_gen(keywords):
    search_list = list(keywords)
    search_list.append("")
    generated_tuple = list(itertools.product(search_list, ["", "_"], search_list, ["", "_"], keywords))
    result = list(map(filter_id, generated_tuple))
    result=list(filter(None, result))
    return result
