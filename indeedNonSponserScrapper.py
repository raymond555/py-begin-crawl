#! python 3
#indeedNonSponserScrapper - web crawls indeed website for job postings that aren't sponsored

#Scrapper will grab information that from indeed
#copy that information and paste into an xls sheet
#sheet will include in order link, title, company, job description?


#TODO: Set up web scrapper

import requests, bs4, openpyxl, os

url = "https://www.indeed.com/q-supply-chain-l-San-Francisco,-CA-jobs.html"
res = requests.get(url)
res.raise_for_status()

htmlPage = bs4.BeautifulSoup(res.text,features="lxml")

toExcelFile = []
titleList = []
refList = []
toExcelFile.append(refList)
toExcelFile.append(titleList)


linkEle = htmlPage.findAll(name = 'div', attrs={'class':'row'})
#TODO: Scrape for specific data set

for rows in linkEle:
    jobTitle = rows.find(name='a',attrs={'data-tn-element':'jobTitle'}).get('title')
    refLink = rows.find(name='a',attrs={'data-tn-element':'jobTitle'}).get('href')
    fullLink = 'https://www.indeed.com' + refLink
    companyName = rows.find(name = 'a', attrs={'data-tn-element':'companyName'})
    titleList.append(jobTitle)
    refList.append(fullLink)
    
#TODO: Set up Excel file

os.chdir('C:\\Users\\Ray\\Desktop\\Python')

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'List of Jobs'
sheet = wb['List of Jobs']
#TODO: Write columns
for col in range(0,len(toExcelFile)):
    for row in range(0,len(toExcelFile[col])):
        sheet.cell(row + 1,col + 1).value = (toExcelFile[col][row])
        
wb.save('jobHunting.xlsx')
print('Done')
#TODO: paste information into excel
#TODO: save and close. 
#'data-tn-element[jobTitle]'
