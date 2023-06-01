import requests, PyPDF2
from PyPDF2 import PdfFileReader
import sys
from ast import literal_eval
import codecs



def searchans(id,ques):
    
    esc = [r'\n',r'\r']
    link='https://drive.google.com/uc?export=download&id='+id
    response = requests.get(link)
    with open('metadata.pdf', 'wb') as f:
        f.write(response.content)
    open("fin.pdf", "wb").write(response.content)
    pdf=open(r"fin.pdf",'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    page = pdf_reader.getPage(0)

    #t=pdf.readlines()
    q=ques
    l=[]
    qs=q.split(" ")
    stop_words=['THE','ARE','OR','A','ABOUT','ACTUALLY','ALMOST','ALSO','ALTHOUGH','ALWAYS','AM','AN','AND','ANY','AS','AT','BE','BECAME','BECOME','BUT','BY','CAN','COULD','DID','DO','DOES','EACH','EITHER','ELSE','FOR','FROM','HAD','HAS','HAVE','HENCE','HOW','I','IF','IN','IS','IT','ITS','JUST','MAY','MAYBE','ME','MIGHT','MINE','MUST','MY','NEITHER','NOR','NOT','OF','OH','OK','WHAT','WHEN','WHERE','WHEREAS','WHERE','WHENEVER','WHETHER','WHICH','WHILE','WHO','WHOM','WHOEVER','WHOSE','WHY','WILL','WITH','WITHIN','WITHOUT','WOULD','YES','YET','YOU','YOUR']
    for i in qs:
        if i.upper() not in stop_words:
            l.append(i)
    # print(l)
    s=''
    c=0
    for i in range(pdf_reader.getNumPages()):
        page=pdf_reader.getPage(i)
        page_content=page.extractText()
        page_content=page_content.encode('utf-8')
        page_content=page_content.decode('utf-8')
        t=page_content.splitlines()
        for i in t:
            
            j=i.strip()
            s+=' '+j
            copy=s.upper()
            if(j[len(j)-1]=='.'):
                for k in l:
                    if k.upper() in copy:
                        c=c+1
                if c>=len(l):
                    for x in s:
                        if x in esc:
                            s=s.replace(x,'')

                    print(literal_eval("'%s'" % s))
                    s=''
                    c=0
                    break
                s=''
                c=0
'''print('workbook:\n')
searchans('1FEP6AHMvb2YsScx6GfOSn-aSxgH1ocZy','renewable resources')  '''      

# print('\ntextbook:\n')
searchans('1sdugBdH_eakEvVtnkUcGxOrw1dlFtaZX',str(sys.argv[1]))
