import camelot
import tabula
import PyPDF2
import re
#using camelot
tables  = camelot.read_pdf('Appraisal Report -270 Industrial Boulevard Kearneysville WV.pdf', pages ='70',flavour = 'lattice')
camelot.plot(tables[0], kind='contour')
df1=tables[0].df
tables[0].to_csv('087-19 04 08 19(C).csv')

# =============================================================================
# #using tabula
# df = tabula.read_pdf("VA_Salem_1725 W Main Street.pdf", pages='66')
# df[0].to_csv('VA_Salem_1725 W Main Street(T).csv')
# # =============================================================================
# # tables[0].parsing_report
# # df1=tables[0].df
# # camelot.plot(tables[0], kind='contour')
# # 
# # =============================================================================
# 
# =============================================================================


# Open the pdf file
object = PyPDF2.PdfFileReader("087-19 04 08 19.pdf")

# Get number of pages
NumPages = object.getNumPages()

# Enter code here
String = "Sales Comparison"

# Extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    if re.search(String,Text):
         if(re.search(('Contents' or 'Index'),Text)):
             pass
         else:    
             print("Pattern Found on Page: " + str(i))