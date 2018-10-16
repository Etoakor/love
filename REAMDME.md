#稳定匹配模拟

程序会用到pyecharts,请安装：
管理员身份运行CMD
pip install pyecharts

操作步骤：
1.把解压缩的好的代码包放在某一个文件夹下。
2.打开configuration文件进行参数设置。

MAN_NUM:男生样本数量
WOMAN_NUM：女生样本数量
TEST_NUM：测试次数

男女样本数量也可以填写不同数字，但结果无法达到稳定匹配。

测试次数，因为样本是随机的，所以可以进行多轮测试，看平均分布。

3.运行main.py文件。

4.运行完毕在目录下会有一个data文件，文件下有数个test文件夹（数量与测试次数相同）
每个test文件夹下有以下几个excel：
man_sample：男生样本
woman_sample：女生样本
man_ismapping：男生配对表（空表，可无视）
women_ismapping：女生配对表（空表，可无视）
man_match_table：男生匹配结果表
woman_match_table：女生匹配结果表
test_detail：此轮结果概述
男生匹配对象喜爱程度分布、女生匹配对象喜爱程度分布：证明这个过程中, 男性能够获得尽可能好的伴侣
和女人总是在可能的情况下被最不喜欢的人追上
data目录下：
detail_graph：模拟结果总体分布（轮次，man_love_level平均，women_love_level平均）

