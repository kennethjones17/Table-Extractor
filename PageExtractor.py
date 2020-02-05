import fitz
import re

ifile = "A022819 Atlee Comm. Blvd.  Ashland  CBC (Revised).pdf"
doc = fitz.open(ifile)
page_count = doc.pageCount
String = "Sales Comparison"
text = ''
l = []
for i in range(0,page_count):
    p = doc.loadPage(i)
    text = p.getText()
    if re.search(String,text):
        if(re.search(('Table' or 'Contents' or 'Index'),text,re.IGNORECASE) and i<20):
            pass
        else:
        #print("Pattern Found on Page: " + str(i))
            l.append(i)

# =============================================================================
# k = sum(l)/len(l)
# for i in l:
#   if(k-i>20):
#          l.remove(i)
#  print(l)
#  print("The range of elemnts for Sales is " + str(min(l)) + "to" + str(max(l)))
# 
# 
# =============================================================================
