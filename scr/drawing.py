import pandas as pd
from configuration import  TEST_NUM
from pyecharts import Bar
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def drawing():
    test_num =  TEST_NUM
    l_table = []
    for i in range(1,test_num+1):
        path = './data/test' + str(i)
        man_match_table = pd.read_csv(path + '/' + 'man_match_table.csv').set_index('man_id')
        woman_match_table = pd.read_csv(path + '/' + 'woman_match_table.csv').set_index('women_id')

        man_match_table = man_match_table.groupby('love_level').count()['range'].sort_values(ascending=False)
        woman_match_table = woman_match_table.groupby('love_level').count()['range'].sort_values(ascending=False)

        man_attr = man_match_table.index.tolist()
        man_v = man_match_table.values.tolist()
        bar_man = Bar('男生匹配对象喜爱程度分布',width=900,height=500)
        bar_man.add('频数',man_attr,man_v,mark_line=["max"],label_color = ['#9932CC'])
        bar_man.render(path + '/' + '男生匹配对象喜爱程度分布.html')

        women_attr = woman_match_table.index.tolist()
        women_v = woman_match_table.values.tolist()
        bar_women = Bar('女生匹配对象喜爱程度分布',width=900,height=500)
        bar_women.add('频数',women_attr,women_v,mark_line=["max"],label_color = ['#FF3030'])
        bar_women.render(path + '/' + '女生匹配对象喜爱程度分布.html')

        detail = pd.read_csv(path + '/' + 'test_detail.csv')
        l_table.append(detail)
        detail_table = pd.concat(l_table)
        s_match_range = detail_table['match_range']
        s_man_love_level_mean = detail_table['man_love_level_mean']
        women_love_level_mean = detail_table['women_love_level_mean']
    fig = plt.figure(figsize=(10, 6), facecolor='gray')
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.hist(s_match_range,bins = 20,
                        histtype = 'bar',
                        align = 'mid',
                        orientation = 'vertical',
                        alpha=0.5,
                        normed =False
                        )
    plt.grid(True)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.hist(s_man_love_level_mean, bins=20,
                         histtype='bar',
                         align='mid',
                         orientation='vertical',
                         alpha=0.5,
                         normed=False
                         )
    plt.grid(True)
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.hist(women_love_level_mean, bins=20,
                         histtype='bar',
                         align='mid',
                         orientation='vertical',
                         alpha=0.5,
                         normed=False
                         )
    plt.grid(True)
    plt.savefig('./data/detail_graph.png',dpi=400)
    plt.show()
    print('==========================制图完成==========================')






