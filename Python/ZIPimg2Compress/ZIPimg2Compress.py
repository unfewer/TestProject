import glob
#import fitz  #包 pymupdf
import os,zipfile ,re
from tempfile import TemporaryDirectory
from PIL import Image
from io import BytesIO
from multiprocessing import Pool
import time 

ComPressrate = 70
resize = 0.7

def zip2pdf(now_path):
    mtmp = os.path.join(now_path,"*.zip")
    mtmp = sorted(glob.glob(mtmp))
    for zipfi in mtmp:
        #doc = fitz.open()
        exampleZip = zipfile.ZipFile(zipfi,'r')
        
        with TemporaryDirectory() as tmpdirname:    #创建临时目录
            print('created temporary directory', tmpdirname)
            exampleZip.extractall(tmpdirname)
            print(zipfi)
            Cleansorted  = []  #清理完的文件列表
            AllRight = []
            cleanfilename = -7   
            for foldername, subfolders, filenames in os.walk(tmpdirname):
                for file in filenames:  #除去杂项文件
                    if file.endswith('.png') or file.endswith('.jpg'):
                        AllRight.append(file)
                        if len(file) <= 7:
                            cleanfilename = 0
                filenames = AllRight
                if len(filenames) != 0:
                    filenames.sort(key = lambda x:  int(re.search( r'(\d)+', x[cleanfilename:]).group())\
                        if re.search( r'(\d)+', x[cleanfilename:])!= None else int(9999)) #排序
                    for filename in filenames:
                        if len(subfolders) != 0:
                            tempath = os.path.join(foldername,subfolders,filename)
                        else :
                            tempath = os.path.join(foldername,filename)
                        Cleansorted.append(tempath)
                        print(tempath)
                        (filepath,tempfilename) = os.path.split(foldername)

                    tempfilename = tempfilename.replace(' ','')
                    filefull =  tempfilename + '.zip'

                    #os.path.splitext(filepath)[0] #提取文件名
                    if not os.path.exists(os.path.join(now_path,'transed')):
                        os.mkdir(os.path.join(now_path,'transed'))
                        now_path2 = os.path.join(now_path,'transed')
                    else:
                        now_path2 = os.path.join(now_path,'transed')
                    filefull = os.path.join(now_path2,filefull)
                    try:
                        filefull = filefull.encode('cp437').decode('GBK') 
                        #编码转换防止乱码
                    except Exception as e:
                        print(e)

                    res = multiproIni(Cleansorted)
                    unity(res,filefull)

            print("finshed")
            exampleZip.close()


def multiproIni(Cleansorted):
    prolist = []
    datalist = []
    p = Pool(4)
    for i in range(4):
        res = p.apply_async(multipro0,args=(i,Cleansorted,))
        prolist.append(res)
    p.close()
    p.join()
    for i in prolist:
        datalist.append(i.get())
    return datalist


def unity(data,zfile):
    Totolcount = len(data[0]) + len(data[1])+\
         len(data[2]) + len(data[3])
    _ , filename  = os.path.split(zfile)

    filename = filename.replace('.zip','')
    with zipfile.ZipFile(zfile,'w',zipfile.ZIP_STORED ) as zipf:
        for i in range(Totolcount):
            if i%4 ==0:
                a = Image.open(data[0][int(i/4)])
                if a.format == 'JPEG':
                    d= data[0][int(i/4)].read()
                    zipf.writestr(filename+'/'+str(i)+'.jpg',data[0][int(i/4)].getvalue())
                else :
                    zipf.writestr(filename+'/'+str(i)+'.png',data[0][int(i/4)].getvalue())
            elif i % 4 ==1:
                a = Image.open(data[1][int(i/4)])
                if a.format == 'JPEG':
                    zipf.writestr(filename+'/'+str(i)+'.jpg',data[1][int(i/4)].getvalue())
                else :
                    zipf.writestr(filename+'/'+str(i)+'.png',data[1][int(i/4)].getvalue())
            elif i%4 ==2:
                a = Image.open(data[2][int(i/4)])
                if a.format == 'JPEG':
                    zipf.writestr(filename+'/'+str(i)+'.jpg',data[2][int(i/4)].getvalue())
                else :
                    zipf.writestr(filename+'/'+str(i)+'.png',data[2][int(i/4)].getvalue())
            elif i%4 ==3:
                a = Image.open(data[3][int(i/4)])
                if a.format == 'JPEG':
                    zipf.writestr(filename+'/'+str(i)+'.jpg',data[3][int(i/4)].getvalue())
                else :
                    zipf.writestr(filename+'/'+str(i)+'.png',data[3][int(i/4)].getvalue())


def multipro0(j,Cleansorted):
    doc = []
    i = int(0)
    for  tempath in Cleansorted:
        (filepath,tempfilename) = os.path.split(tempath)
        #  tempfilename ：临时暂存文件名
        #内存临时存储
        bf = BytesIO() 
        if i % 4 == j:
            try:
                img = Image.open(tempath)  # PIL库加载图片
                x,y = img.size
                if x < 3000 and y < 3000: 
                    try:
                        img.save(bf,format='Jpeg',quality=ComPressrate, subsampling=0) #压缩文件
                    except Exception as e:
                        img.save(bf,format='PNG',quality=ComPressrate, subsampling=0) #压缩文件
                        print(e)
                else:
                    x = int(x*resize)
                    y = int(y*resize)
                    img = img.resize((x, y),Image.ANTIALIAS)
                    try:
                        img.save(bf,format='Jpeg',quality=ComPressrate, subsampling=0) #压缩文件
                    except Exception as e:
                        img.save(bf,format='PNG',quality=ComPressrate, subsampling=0) #压缩文件
                        print(e)
                #删除文件   
                os.unlink(tempath)     
                doc.append(bf)
                
            except Exception as e:
                print(e)
        i = i + 1
    return doc      #处理完成返回doc文档


if __name__ == '__main__':

    now_path=os.getcwd()
    zip2pdf(now_path)

            
