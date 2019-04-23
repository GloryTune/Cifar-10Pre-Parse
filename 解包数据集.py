#学号：201820001085 姓名：杨天佑
import imageio
import numpy as np
import pickle
# 解压缩，返回解压后的字典
def unpickle(file):
    fo = open(file, 'rb')
    dict = pickle.load(fo,encoding='bytes')
    fo.close()
    return dict

# 生成训练集图片
for j in range(1, 6):
    dataName = "data_batch_" + str(j)  # 读取当前目录下的data_batch12345文件
    Xtr = unpickle(dataName)
    print (dataName + " is loading...")
    #meta=unpickle('batches.meta')
    for i in range(0, 10000):

        img = np.reshape(Xtr[b'data'][i], (3, 32, 32))  # Xtr['data']为图片二进制数据
        img = img.transpose((1, 2, 0))  # 读取image
        picName = 'train\\' + str(Xtr[b'labels'][i]) + '.' + str(i + (j - 1) * 10000) + '.jpg'
        imageio.imwrite(picName, img)
    print (dataName + " loaded.")

print ("test_batch is loading...")

# 生成测试集图片
testXtr = unpickle("test_batch")
for i in range(0, 10000):
    img = np.reshape(testXtr[b'data'][i], (3, 32, 32))
    img = img.transpose((1,2,0))
    picName = 'test\\' + str(testXtr[b'labels'][i]) + '_' + str(i) + '.jpg'
    imageio.imwrite(picName, img)
print ("test_batch loaded.")
