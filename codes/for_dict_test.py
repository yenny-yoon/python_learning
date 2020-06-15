dict_tohoku={'amori':5349.0, 'akita':4644.0, 'sendai':5344.0,\
             'yamagata':4968.0, 'fukushima':6259.0, 'morioka':5478.0}

avg_tohoku=0.0
for att in dict_tohoku:
    avg_tohoku+=dict_tohoku[att]

avg_tohoku/=len(dict_tohoku)
print(avg_tohoku)

