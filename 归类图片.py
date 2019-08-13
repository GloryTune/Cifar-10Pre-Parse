#图片归类 姓名：杨天佑 学号：201820001085
import os
import shutil
l_name = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
path1 = 'd:\\cifar\\train\\'
path2 = 'd:\\cifar\\test\\'
for i in l_name:
    if not os.path.exists(path1+i):
        os.makedirs(path1+i)
for q in l_name:
    if not os.path.exists(path2 + q):
        os.makedirs(path2 + q)
ori_testpath = 'D:\\cifar10PRE\\test'
ori_trainpath= 'D:\\cifar10PRE\\train'
filelist = os.listdir(ori_testpath)
filelist1 = os.listdir(ori_trainpath)
o = 1
for item in filelist:
    for num in range(0,10):
        if item.startswith(str(num)+'.'):
            shutil.copyfile(os.path.join(ori_testpath, item), os.path.join(path2+l_name[num], l_name[num] + str(o) + '.jpeg'))
            print('正在归类中...')
            o+=10
print('test归类完毕！')
n = 1
for item1 in filelist1:
    for num1 in range(0, 10):
        if item1.startswith(str(num1)+ '.'):
            shutil.copyfile(os.path.join(ori_trainpath, item1),
                            os.path.join(path1 + l_name[num1], l_name[num1] + str(n) + '.jpeg'))
            print('正在归类中...')
            n += 1
print('train归类完毕！')





