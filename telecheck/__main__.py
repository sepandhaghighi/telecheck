# -*- coding: utf-8 -*-
from .telecheck import *
import sys
import multiprocessing as mu
ValidIDList=[]
if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if len(args)>2:
            keywords = filter_keyword(args[2].split(","))
            p=mu.Pool(mu.cpu_count())
            if args[1].upper()=="ALL":
                print("Generating ...")
                gen_list = id_list_gen(keywords)
                gen_list.sort(key=lambda s: len(s))
                ValidIDList=p.map(run,gen_list)
                save_id(ValidIDList,len(gen_list))
            elif args[1].upper()=="BOT":
                print("Generating ...")
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






