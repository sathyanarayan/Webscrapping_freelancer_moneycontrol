import requests
import lxml.html as lh
import pandas as pd
import csv

"""
    This Program is to download the Splits data  - View Company Splits during
    the year, from https://www.moneycontrol.com/stocks/marketinfo/splits/index.php
    As part of Freelancing project request raised:
    https://www.freelancer.com/projects/web-scraping/Need-someone-download-Bhav-Copy/details
    @author:S.SATHYANARAYAN
"""

"""
@params:Starting year from which data is required and till which year:
@arguments str_year:2019 total_year:20
@Result: CSV file containing data : see splitdata.csv file
"""
urls = []
result = open("splitdata.csv", "w")
csvwriter = csv.writer(result)
url1 = "https://www.moneycontrol.com/stocks/marketinfo/splits/index.php?sel_year="
str_year = int(input("Enter the year from which data need to be fetched"))
total_year = int(input("Enter the number of year till which data is required"))
for i  in range(0,total_year):
    tmp_year = str_year - i
    temp_url = url1 + str(tmp_year)
    urls.append(temp_url)
for url in urls:
    try:
        page = requests.get(url)
        doc = lh.fromstring(page.content)
        tr_elements = doc.xpath('//tr')
        col=[]
        for i in range(0,len(tr_elements)):
            row = []
            k=0
            if (len(tr_elements[i]) == 4):
                for t in tr_elements[i]:
                    k+=1
                    name=t.text_content().split('\n')[0]
                    row.append(name)
                csvwriter.writerow(row)
                print(row)
    except Exception as E:
        print("Exception raise while running the script" + str(E))
result.close()
