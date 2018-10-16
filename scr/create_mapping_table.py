import pandas as pd

#设置姻缘关系表
def create_mapping_table(man,women):

    man_ismapping = pd.DataFrame({
            'man_id':man.index,
            'target':'n',
            'love_level':0,
            'range':0
            }).set_index('man_id')

    women_ismapping = pd.DataFrame({
            'women_id':women.index,
            'target':'n',
            'love_level':0,
            'range':0
            }).set_index('women_id')
    return (man_ismapping,women_ismapping)

if __name__ == '__main__':
    create_mapping_table(man,women)