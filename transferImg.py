"""
读取CSV，把binary转为图片，保存到本地

"""
import csv
import numpy as np
from PIL import Image
import os
import time
start_time = time.time()
image_number = [0, 0, 0, 0, 0, 0, 0]  # 每种表情统计
couter_num = 1
total = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
}
with open('C:/Users/pc/Desktop/fer2013.csv', 'r') as csvfile:
    file_reader = csv.DictReader(csvfile)
    for reader in file_reader:
        x = reader["pixels"]
        x = x.split()

        arry = [int(i) for i in x]

        result = np.array(arry)
        result = result.reshape([48, 48])

        image = Image.fromarray(result)  # 从数据，生成image对象
        image = image.resize([384, 384], Image.ANTIALIAS)

        number = reader["emotion"]  # 读出这张图片对应的表情标签
        total[number] += 1
        # name = "/image"+str(image_number[int(number)])+".png"
        name = str(image_number[int(number)])+".png"
        path = os.path.join(
            "E:/Python Code/Pytorch/ExpressionClassification/expr_data/expr_photo/", number+'/')  # 生成这个表情图片对应的路径

        print("正在保存%s类型表情%s" % (number, name))
        image_save = image.convert("L")  # 转化为灰度图片
        image_save.save(path+name)
        print("第%d保存成功！" % (couter_num))  # 显示已经保存了第几张
        image_number[int(number)] = image_number[int(number)]+1
        couter_num += 1
end_time = time.time()
print(total, end_time-end_time)
