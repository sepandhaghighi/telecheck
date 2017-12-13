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
<BLANKLINE>
<BLANKLINE>
         ___      _
__   __ / _ \    / |
\ \ / /| | | |   | |
 \ V / | |_| | _ | |
  \_/   \___/ (_)|_|
<BLANKLINE>
<BLANKLINE>
You can use a-z,0-9 and underscores:
<BLANKLINE>
Help :
<BLANKLINE>
     - all 'your_keywords' --> (All Users) Example : 'python -m telecheck all keyword1,keyword2,keyword3'
<BLANKLINE>
     - bot 'your_keywords' --> (Bot Users) Example : 'python -m telecheck bot keyword1,keyword2,keyword3'
<BLANKLINE>
>>> id_check("sepkjaer")
False
>>> id_check("sepkjaer2323123123123")
True
>>> filter_keyword(['sepand','2','233444$$$'])
['sepand', '2']
>>> filter_id(['sepand','222'])
'sepand222'
>>> filter_id(['sss'])
>>> id_list_gen(['key1','key2'])
['key1key1key11', 'key1key1key12', 'key1key1key13', 'key1key1key14', 'key1key1key15', 'key1key1key16', 'key1key1key17', 'key1key1key18', 'key1key1key19', 'key1key1key1', 'key1key1key21', 'key1key1key22', 'key1key1key23', 'key1key1key24', 'key1key1key25', 'key1key1key26', 'key1key1key27', 'key1key1key28', 'key1key1key29', 'key1key1key2', 'key1key1_key11', 'key1key1_key12', 'key1key1_key13', 'key1key1_key14', 'key1key1_key15', 'key1key1_key16', 'key1key1_key17', 'key1key1_key18', 'key1key1_key19', 'key1key1_key1', 'key1key1_key21', 'key1key1_key22', 'key1key1_key23', 'key1key1_key24', 'key1key1_key25', 'key1key1_key26', 'key1key1_key27', 'key1key1_key28', 'key1key1_key29', 'key1key1_key2', 'key1key2key11', 'key1key2key12', 'key1key2key13', 'key1key2key14', 'key1key2key15', 'key1key2key16', 'key1key2key17', 'key1key2key18', 'key1key2key19', 'key1key2key1', 'key1key2key21', 'key1key2key22', 'key1key2key23', 'key1key2key24', 'key1key2key25', 'key1key2key26', 'key1key2key27', 'key1key2key28', 'key1key2key29', 'key1key2key2', 'key1key2_key11', 'key1key2_key12', 'key1key2_key13', 'key1key2_key14', 'key1key2_key15', 'key1key2_key16', 'key1key2_key17', 'key1key2_key18', 'key1key2_key19', 'key1key2_key1', 'key1key2_key21', 'key1key2_key22', 'key1key2_key23', 'key1key2_key24', 'key1key2_key25', 'key1key2_key26', 'key1key2_key27', 'key1key2_key28', 'key1key2_key29', 'key1key2_key2', 'key1key11', 'key1key12', 'key1key13', 'key1key14', 'key1key15', 'key1key16', 'key1key17', 'key1key18', 'key1key19', 'key1key1', 'key1key21', 'key1key22', 'key1key23', 'key1key24', 'key1key25', 'key1key26', 'key1key27', 'key1key28', 'key1key29', 'key1key2', 'key1_key11', 'key1_key12', 'key1_key13', 'key1_key14', 'key1_key15', 'key1_key16', 'key1_key17', 'key1_key18', 'key1_key19', 'key1_key1', 'key1_key21', 'key1_key22', 'key1_key23', 'key1_key24', 'key1_key25', 'key1_key26', 'key1_key27', 'key1_key28', 'key1_key29', 'key1_key2', 'key1_key1key11', 'key1_key1key12', 'key1_key1key13', 'key1_key1key14', 'key1_key1key15', 'key1_key1key16', 'key1_key1key17', 'key1_key1key18', 'key1_key1key19', 'key1_key1key1', 'key1_key1key21', 'key1_key1key22', 'key1_key1key23', 'key1_key1key24', 'key1_key1key25', 'key1_key1key26', 'key1_key1key27', 'key1_key1key28', 'key1_key1key29', 'key1_key1key2', 'key1_key1_key11', 'key1_key1_key12', 'key1_key1_key13', 'key1_key1_key14', 'key1_key1_key15', 'key1_key1_key16', 'key1_key1_key17', 'key1_key1_key18', 'key1_key1_key19', 'key1_key1_key1', 'key1_key1_key21', 'key1_key1_key22', 'key1_key1_key23', 'key1_key1_key24', 'key1_key1_key25', 'key1_key1_key26', 'key1_key1_key27', 'key1_key1_key28', 'key1_key1_key29', 'key1_key1_key2', 'key1_key2key11', 'key1_key2key12', 'key1_key2key13', 'key1_key2key14', 'key1_key2key15', 'key1_key2key16', 'key1_key2key17', 'key1_key2key18', 'key1_key2key19', 'key1_key2key1', 'key1_key2key21', 'key1_key2key22', 'key1_key2key23', 'key1_key2key24', 'key1_key2key25', 'key1_key2key26', 'key1_key2key27', 'key1_key2key28', 'key1_key2key29', 'key1_key2key2', 'key1_key2_key11', 'key1_key2_key12', 'key1_key2_key13', 'key1_key2_key14', 'key1_key2_key15', 'key1_key2_key16', 'key1_key2_key17', 'key1_key2_key18', 'key1_key2_key19', 'key1_key2_key1', 'key1_key2_key21', 'key1_key2_key22', 'key1_key2_key23', 'key1_key2_key24', 'key1_key2_key25', 'key1_key2_key26', 'key1_key2_key27', 'key1_key2_key28', 'key1_key2_key29', 'key1_key2_key2', 'key1_key11', 'key1_key12', 'key1_key13', 'key1_key14', 'key1_key15', 'key1_key16', 'key1_key17', 'key1_key18', 'key1_key19', 'key1_key1', 'key1_key21', 'key1_key22', 'key1_key23', 'key1_key24', 'key1_key25', 'key1_key26', 'key1_key27', 'key1_key28', 'key1_key29', 'key1_key2', 'key2key1key11', 'key2key1key12', 'key2key1key13', 'key2key1key14', 'key2key1key15', 'key2key1key16', 'key2key1key17', 'key2key1key18', 'key2key1key19', 'key2key1key1', 'key2key1key21', 'key2key1key22', 'key2key1key23', 'key2key1key24', 'key2key1key25', 'key2key1key26', 'key2key1key27', 'key2key1key28', 'key2key1key29', 'key2key1key2', 'key2key1_key11', 'key2key1_key12', 'key2key1_key13', 'key2key1_key14', 'key2key1_key15', 'key2key1_key16', 'key2key1_key17', 'key2key1_key18', 'key2key1_key19', 'key2key1_key1', 'key2key1_key21', 'key2key1_key22', 'key2key1_key23', 'key2key1_key24', 'key2key1_key25', 'key2key1_key26', 'key2key1_key27', 'key2key1_key28', 'key2key1_key29', 'key2key1_key2', 'key2key2key11', 'key2key2key12', 'key2key2key13', 'key2key2key14', 'key2key2key15', 'key2key2key16', 'key2key2key17', 'key2key2key18', 'key2key2key19', 'key2key2key1', 'key2key2key21', 'key2key2key22', 'key2key2key23', 'key2key2key24', 'key2key2key25', 'key2key2key26', 'key2key2key27', 'key2key2key28', 'key2key2key29', 'key2key2key2', 'key2key2_key11', 'key2key2_key12', 'key2key2_key13', 'key2key2_key14', 'key2key2_key15', 'key2key2_key16', 'key2key2_key17', 'key2key2_key18', 'key2key2_key19', 'key2key2_key1', 'key2key2_key21', 'key2key2_key22', 'key2key2_key23', 'key2key2_key24', 'key2key2_key25', 'key2key2_key26', 'key2key2_key27', 'key2key2_key28', 'key2key2_key29', 'key2key2_key2', 'key2key11', 'key2key12', 'key2key13', 'key2key14', 'key2key15', 'key2key16', 'key2key17', 'key2key18', 'key2key19', 'key2key1', 'key2key21', 'key2key22', 'key2key23', 'key2key24', 'key2key25', 'key2key26', 'key2key27', 'key2key28', 'key2key29', 'key2key2', 'key2_key11', 'key2_key12', 'key2_key13', 'key2_key14', 'key2_key15', 'key2_key16', 'key2_key17', 'key2_key18', 'key2_key19', 'key2_key1', 'key2_key21', 'key2_key22', 'key2_key23', 'key2_key24', 'key2_key25', 'key2_key26', 'key2_key27', 'key2_key28', 'key2_key29', 'key2_key2', 'key2_key1key11', 'key2_key1key12', 'key2_key1key13', 'key2_key1key14', 'key2_key1key15', 'key2_key1key16', 'key2_key1key17', 'key2_key1key18', 'key2_key1key19', 'key2_key1key1', 'key2_key1key21', 'key2_key1key22', 'key2_key1key23', 'key2_key1key24', 'key2_key1key25', 'key2_key1key26', 'key2_key1key27', 'key2_key1key28', 'key2_key1key29', 'key2_key1key2', 'key2_key1_key11', 'key2_key1_key12', 'key2_key1_key13', 'key2_key1_key14', 'key2_key1_key15', 'key2_key1_key16', 'key2_key1_key17', 'key2_key1_key18', 'key2_key1_key19', 'key2_key1_key1', 'key2_key1_key21', 'key2_key1_key22', 'key2_key1_key23', 'key2_key1_key24', 'key2_key1_key25', 'key2_key1_key26', 'key2_key1_key27', 'key2_key1_key28', 'key2_key1_key29', 'key2_key1_key2', 'key2_key2key11', 'key2_key2key12', 'key2_key2key13', 'key2_key2key14', 'key2_key2key15', 'key2_key2key16', 'key2_key2key17', 'key2_key2key18', 'key2_key2key19', 'key2_key2key1', 'key2_key2key21', 'key2_key2key22', 'key2_key2key23', 'key2_key2key24', 'key2_key2key25', 'key2_key2key26', 'key2_key2key27', 'key2_key2key28', 'key2_key2key29', 'key2_key2key2', 'key2_key2_key11', 'key2_key2_key12', 'key2_key2_key13', 'key2_key2_key14', 'key2_key2_key15', 'key2_key2_key16', 'key2_key2_key17', 'key2_key2_key18', 'key2_key2_key19', 'key2_key2_key1', 'key2_key2_key21', 'key2_key2_key22', 'key2_key2_key23', 'key2_key2_key24', 'key2_key2_key25', 'key2_key2_key26', 'key2_key2_key27', 'key2_key2_key28', 'key2_key2_key29', 'key2_key2_key2', 'key2_key11', 'key2_key12', 'key2_key13', 'key2_key14', 'key2_key15', 'key2_key16', 'key2_key17', 'key2_key18', 'key2_key19', 'key2_key1', 'key2_key21', 'key2_key22', 'key2_key23', 'key2_key24', 'key2_key25', 'key2_key26', 'key2_key27', 'key2_key28', 'key2_key29', 'key2_key2']
>>> run('sepkjaer')
>>> save_id(['sepkjaer','ssss'],45)
******************************
Total Valid Usernames : 45
Available Usernames : 2
******************************
>>> cov.stop()
>>> cov.save()

'''