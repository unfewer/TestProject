#import sys
			#python -m pip install pypiwin32  包要求
import os,time
from win32com import client as wc 

def doc2pdf(word,input_file,Out_file): 	 
	doc = word.Documents.Open(input_file) 
	doc.SaveAs(Out_file, 17) 
	doc.Close() 
	

file_path=os.getcwd() #工作目录 当前目录
p=os.path.join(file_path,'PdfGenerate')
if not os.path.exists(p):
		os.mkdir(p) 
file_list=os.listdir(file_path)
for word_path in file_list:
	if(word_path.endswith('.docx') or word_path.endswith('.doc') and word_path[0]!='~'):
		doc_name=os.path.join(file_path,word_path)
		pdf_name=os.path.join(p,word_path.split(".")[0]+".pdf")
		word = wc.Dispatch('Word.Application')  #启动word
		doc2pdf(word,doc_name,pdf_name)
		print(doc_name)
		print(pdf_name)
word.Quit()	   #关闭word
time.sleep(2)
	

