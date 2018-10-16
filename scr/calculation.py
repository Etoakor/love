import pandas as pd
from configuration import  TEST_NUM

def calculation():
    test_num =  TEST_NUM
    for i in range(1,test_num+1):
        path = './data/test' + str(i)
        man = pd.read_csv(path + '/' + 'man_sample.csv').set_index('index')
        women = pd.read_csv(path + '/' + 'woman_sample.csv').set_index('index')
        man_ismapping = pd.read_csv(path + '/' + 'man_ismapping.csv').set_index('man_id')
        women_ismapping = pd.read_csv(path + '/' + 'women_ismapping.csv').set_index('women_id')
        print('==============================测试集{}模拟开始=============================='.format(i))
        print('==============================开始模拟求婚过程==============================')
        level_num = 0
        while man_ismapping['love_level'].min() == 0:
            level_num += 1
            print('==============================开始第{}天婚姻配对=============================='.format(level_num))
            u_mapping_man = man_ismapping[man_ismapping.target == 'n'].index.tolist()

            if level_num < 2:
                level_col = 'level' + str(level_num)
                man_choose = man[man.index.isin(u_mapping_man)][level_col].to_frame().reset_index()
                man_choose.columns = ['man_id', 'women_id']
                man_choose['range'] = 1
            else:
                m_id = u_mapping_man
                l = []
                for man_id in m_id:
                    col_n = int(man_ismapping[man_ismapping.index == man_id].range[0])
                    level_col = 'level' + str(col_n + 1)
                    women_id = man[man.index == man_id][level_col][0]
                    rg = col_n + 1
                    l.append([man_id, women_id, rg])
                man_choose = pd.DataFrame(l, columns=['man_id', 'women_id', 'range'])

            for r in range(0, len(man_choose)):
                relationship = man_choose[man_choose.index == r]
                m = [i for i in relationship['man_id']][0]
                w = [i for i in relationship['women_id']][0]
                find = women[women.index == w].unstack().reset_index()
                find.columns = ['level', 'women_id', 'man_id']
                find = int([i for i in find[find['man_id'] == m]['level']][0].split('level')[1])
                o_love_level = [i for i in women_ismapping[women_ismapping.index == w]['love_level']][0]
                rg = [i for i in relationship['range']][0]
                if o_love_level == 0:
                    women_ismapping.loc[w, 'love_level'] = find
                    women_ismapping.loc[w, 'target'] = m
                    women_ismapping.loc[w, 'range'] = level_num
                    man_ismapping.loc[m, 'love_level'] = rg
                    man_ismapping.loc[m, 'target'] = w
                    man_ismapping.loc[m, 'range'] = rg
                elif o_love_level > find:
                    m_o = women_ismapping.loc[w, 'target']
                    man_ismapping.loc[m_o, 'love_level'] = 0
                    man_ismapping.loc[m_o, 'target'] = 'n'
                    man_ismapping.loc[m, 'love_level'] = rg
                    man_ismapping.loc[m, 'target'] = w
                    man_ismapping.loc[m, 'range'] = rg
                    women_ismapping.loc[w, 'love_level'] = find
                    women_ismapping.loc[w, 'target'] = m
                    women_ismapping.loc[w, 'range'] = level_num
                else:
                    man_ismapping.loc[m, 'range'] = rg
                    pass

        print('==============================婚姻配对完成==============================')
        print('共进行了{}次牵线搭桥，在第{}天举办集体婚礼。'.format(level_num, level_num + 1))

        print('==============================导出配对明细表==============================')
        man_love_level_mean = man_ismapping.love_level.mean()
        women_love_level_mean = women_ismapping.love_level.mean()
        detail = [[level_num,level_num,man_love_level_mean,women_love_level_mean]]
        pd.DataFrame(detail,columns=['match_range','party_time','man_love_level_mean','women_love_level_mean'])\
                .to_csv(path+'/'+'test_detail.csv', index=0)
        man_ismapping.reset_index().to_csv(path+'/'+'man_match_table.csv', index=0)
        women_ismapping.reset_index().to_csv(path+'/'+'woman_match_table.csv', index=0)
        print('==============================导出完毕==============================')

if __name__ == '__main__':
    calculation()