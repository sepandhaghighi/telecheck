# -*- coding: utf-8 -*-
from .TIR import *
import sys
import doctest
import multiprocessing as mu
if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py",optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
        if len(args)>2:
            keywords = filter_keyword(args[2].split(","))
            gen_list = id_list_gen(keywords)
            p=mu.Pool(4)
            if args[1].upper()=="ALL":
                p.map(run,gen_list)
            elif args[1].upper()=="BOT":
                gen_list=list(map(lambda x:x+"bot",gen_list))
                p.map(run, gen_list)
            else:
                TIR_help_func()
        else:
            TIR_help_func()
    else:
        TIR_help_func()






