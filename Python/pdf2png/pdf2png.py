import fitz,os
#1、安装库  pip install pymupdf
#  打开PDF文件，生成一个对象

def pdf2png(doc_path,mkd):
    doc = fitz.open(doc_path)
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        #pm.writePNG('%s.png' % pg)
        if mkd==0:
            pm.writePNG('%s-%s.png' % (os.path.splitext(doc_path)[0],pg))
        elif mkd==2:
            p=os.path.join(os.getcwd(),'ok')
            if not os.path.exists(p):
                os.mkdir(p)
            p=os.path.join(p,os.path.splitext(doc_path)[0])
            pm.writePNG('%s-%s.png' % (p,pg))
        else :
            p=os.path.join(os.getcwd(),os.path.splitext(doc_path)[0])
            if not os.path.exists(p):
                os.mkdir(p)
            p=os.path.join(p,os.path.splitext(doc_path)[0])
            pm.writePNG('%s-%s.png' % (p,pg))    

print('是否要分别建立文件夹，1=是，0=否')
mk=int(input())
if mk==0:
    print('是否要合并在一个文件夹内，1=是，0=否')
    mk2=int(input())
else :
    mk2=0
file_path=os.getcwd()
file_list=os.listdir(file_path)
for pdf_path in file_list:
    if pdf_path.endswith('.pdf'):
        pdf2png(pdf_path,mk+mk2*2)
