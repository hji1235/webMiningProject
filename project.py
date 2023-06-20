import requests
from bs4 import BeautifulSoup
import pandas as pd

test = []
jobSectorList = []

comNameList = []
jobTitleList = []
careerList = []
eduList = []
linkList = []

for page_num in  range(1, 300) : 
    res = requests.get('https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={}&cat_mcls=2&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1#searchTitle'.format(page_num), headers ={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, "lxml")
    listItem = soup.select('.list_item')
    for item in listItem : 
        jobSectorList = []
        comName = item.select_one('div.company_nm > .str_tit').attrs['title']
        comNameList.append(comName)
        jobTitle = item.select_one('div.notification_info > .job_tit > .str_tit').attrs['title']
        jobTitleList.append(jobTitle)
        jobMeta = item.select_one('div.notification_info > .job_meta > .job_sector > span').text
        career = item.select_one('div.recruit_condition > .career').text
        careerList.append(career)
        edu =  item.select_one('div.recruit_condition > .education').text
        eduList.append(edu)
        link = item.select_one('div.notification_info > .job_tit > .str_tit').attrs['href']
        linkList.append('https://www.saramin.co.kr' + link)
        test.append(jobMeta)
        

df = pd.DataFrame(
    {
        "comName" : comNameList,
        "jobTitle" : jobTitleList,
        "jobMeta" : test,
        "career" : careerList,
        "edu" : eduList,
        "link" : linkList
    }
)

df.to_csv('project.csv', index=False, encoding='utf-8')
    
    




