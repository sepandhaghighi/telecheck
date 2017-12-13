# -*- coding: utf-8 -*-
'''
>>> from telecheck import *
>>> import coverage
>>> import random
>>> cov=coverage.Coverage()
>>> cov.start()
>>> line()
******************************
>>> random.seed(2)
>>> create_random_sleep()
2.879094247695436
>>> random.seed(3)
>>> create_random_sleep(index=0)
1
>>> TIR_help_func()
 _          _              _                  _
| |_   ___ | |  ___   ___ | |__    ___   ___ | | __
| __| / _ \| | / _ \ / __|| '_ \  / _ \ / __|| |/ /
| |_ |  __/| ||  __/| (__ | | | ||  __/| (__ |   <
 \__| \___||_| \___| \___||_| |_| \___| \___||_|\_\


         ___      _
__   __ / _ \    / |
\ \ / /| | | |   | |
 \ V / | |_| | _ | |
  \_/   \___/ (_)|_|


You can use a-z,0-9 and underscores:

Help :

     - all 'your_keywords' --> (All Users) Example : 'python -m telecheck all keyword1,keyword2,keyword3'

     - bot 'your_keywords' --> (Bot Users) Example : 'python -m telecheck bot keyword1,keyword2,keyword3'

>>> id_check("sepkjaer")
False
>>> id_check("sepkjaer2323123123123")
True
>>> filter_keyword(['sepand','2','233444$$$'])
>>> filter_id(['sepand','222'])
>>> filter_id(['sss'])
>>> id_list_gen(['key1','key2'])
>>> run('sepkjaer')
>>> save_id(['sepkjaer','ssss'],45)
>>> cov.stop()
>>> cov.save()

'''