import pandas as pd
import random

from configuration import MAN_NUM,WOMAN_NUM


def create_sample():
    man_num = MAN_NUM
    women_num = WOMAN_NUM

    #设置男女生喜好样本
    print('==============================生成样本数据==============================')
    man = pd.DataFrame( [['w'+str(i) for i in random.sample(range(1,women_num+1),women_num)] \
                          for i in range(man_num)],
                        index = ['m'+str(i) for i in range(1,man_num+1)],
                        columns = ['level'+str(i) for i in range(1,women_num+1)]
                        )

    women = pd.DataFrame( [['m'+str(i) for i in random.sample(range(1,man_num+1),man_num)] \
                          for i in range(women_num)],
                        index = ['w'+str(i) for i in range(1,women_num+1)],
                        columns = ['level'+str(i) for i in range(1,man_num+1)]
                        )
    return (man,women)

if __name__ == '__main__':
    create_sample(man,women)





