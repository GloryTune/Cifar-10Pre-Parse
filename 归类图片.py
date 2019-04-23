#图片归类 姓名：杨天佑 学号：201820001085
import os
import shutil
class GuiLei():
    def __init__(self):
        self.path = 'd:\\pachong\\train'#原始文件夹 包含以0-9为类标的所有图片 0代表airplane， 1代表automobile...
        self.new_path = 'c:\\Users\\杨天佑\\Desktop\\automobile'#要归类到的目标路径
    def gui(self):
        filelist = os.listdir(self.path)#将原始路径的文件夹下的所有文件名存储到一个列表中
        i=1
        for item in filelist:
            if item.startswith('1.'):#判断：将0开头的图片归类这里0代表airplane
                shutil.copyfile(os.path.join(self.path, item),os.path.join(self.new_path, 'automobile.' + str(i) + '.jpeg'))#这里用到shutil库的copy函数，前面的参数是原始路径，后面是目标路径，并且完成重命名
                i+=1
                print('正在归类中...')
        print('归类完毕！')

if __name__ == '__main__':
    demo = GuiLei()
    demo.gui()




