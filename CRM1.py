import random
import warnings
import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

cards =  [
'小骷髅','冰精灵','矿工','骑士',
'滚木','三枪','大苍蝇','采集器',
'光头强','小电','蝙蝠','小火人',
'投矛手','弓箭手','箭雨','小苍蝇',
'土炮','炸弹兵','团伙','电塔',
'迫击炮', '黄毛', '铁毛', '黄家驹',
'冰人','治疗','墓碑','吹箭',
'铁苍蝇','火球','野猪','熔炉',
'女武神','女枪','小皮卡','攻城锤',
'火法','胖子','哥布林房子','炸弹塔',
'地狱塔','火箭','黄毛房子','镜像',
'狂暴','复制','飓风','骷髅海',
'飞桶','盾牌兵','飞龙','毒药',
'黑骑','冰冻','女巫','炮车',
'气球','王子','投石','飞斧',
'弩车','大骷髅','大电','大皮卡',
'石头','冰法','刺客','公主',
'电法','地狱龙','樵夫','电车',
'熔岩','暗夜女巫','蹦迪'
]
warnings.filterwarnings("ignore")
#print(cards.__len__())
#Image.open('resource/石头'+'.jpg').show()
out = random.sample(cards,8)
for index in range(len(out)):
    print('===' + out[index] + '===')
    #fp = open('resource/'+ out[index] + '.jpg','r')
    im = mpimg.imread('resource/'+ out[index] + '.jpg')
    #plt.ion()
    #im = Image.open('resource/'+ out[index] + '.jpg')
    plt.imshow(im)  # 显示图片
    plt.axis('off')  # 不显示坐标轴
    #plt.show()
    #time.sleep(random.randint(0,3))
    plt.pause(3)
    plt.close()


