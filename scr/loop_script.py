from configuration import  TEST_NUM
import os
from scr.create_sample import create_sample
from scr.create_mapping_table import create_mapping_table
import pandas as pd

def loop_script():
    test_num = TEST_NUM
    if not os.path.exists('./data'):
        os.makedirs('./data')

    for i in range(1,test_num+1):
        print('==============================开始创建测试文件夹{}=============================='.format(i))
        path = './data/test' + str(i)
        if not os.path.exists(path):
            os.makedirs(path)
        sample_data = create_sample()
        man = sample_data[0]
        women = sample_data[1]
        man.reset_index().to_csv(path+'/'+'man_sample.csv', index=0)
        women.reset_index().to_csv(path+'/'+'woman_sample.csv', index=0)
        print('==============================样本数据生成成功==============================')
        print('==============================创建婚姻关系表==============================')
        man = pd.read_csv(path+'/'+'man_sample.csv').set_index('index')
        women = pd.read_csv(path+'/'+'woman_sample.csv').set_index('index')
        mapping_data = create_mapping_table(man, women)
        man_ismapping = mapping_data[0]
        women_ismapping = mapping_data[1]
        man_ismapping.reset_index().to_csv(path+'/'+'man_ismapping.csv', index=0)
        women_ismapping.reset_index().to_csv(path+'/'+'women_ismapping.csv', index=0)
        print('==============================婚姻关系表创建完成==============================')




