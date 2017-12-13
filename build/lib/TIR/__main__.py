# -*- coding: utf-8 -*-
from .TIR import *
import sys
import doctest
import multiprocessing as mu
ValidIDList=[]
if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py",optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
        if len(args)>2:
            keywords = filter_keyword(args[2].split(","))
            p=mu.Pool(4)
            if args[1].upper()=="ALL":
                gen_list = id_list_gen(keywords)
                gen_list.sort(key=lambda s: len(s))
                ValidIDList=p.map(run,gen_list)
                save_id(ValidIDList,len(gen_list))
            elif args[1].upper()=="BOT":
                gen_list = id_list_gen(keywords,"bot")
                gen_list.sort(key=lambda s: len(s))
                ValidIDList=p.map(run, gen_list)
                save_id(ValidIDList,len(gen_list))
            else:
                TIR_help_func()
        else:
            TIR_help_func()
    else:
        TIR_help_func()






