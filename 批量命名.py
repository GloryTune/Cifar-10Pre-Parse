#批量重命名文件夹内图片文件
import os
class BatchRename():

    def __init__(self):
        self.path = 'C:\\Users\\杨天佑\\Desktop\\test\\9'  #表示需要命名处理的文件夹
        self.paath = 'C:\\Users\\杨天佑\\Desktop\\train\\0'
    def rename(self):
        filelist = os.listdir(self.path) #获取文件路径下的文件名
        total_num = len(filelist) #获取文件长度（个数）
        i = 1  #表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.jpg'):  #初始的图片的格式为jpg格式的，可以根据情况设置
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath((self.path)), 'truck'+'.'+str(i) + '.jpeg')#处理后的格式也为jpg格式，可以改成png格式
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))
    def renamee(self):
        filelist = os.listdir(self.paath) #获取文件路径下的文件名
        total_num = len(filelist) #获取文件长度（个数）
        i = 1  #表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.jpg'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.paath), item)
                dst = os.path.join(os.path.abspath(self.paath), 'airplane'+'.'+str(i) + '.jpeg')#处理后的格式也为jpg格式的，当然这里可以改成png格式
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    #demo.rename()
    demo.renamee()