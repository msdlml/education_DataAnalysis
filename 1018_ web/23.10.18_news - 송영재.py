import urllib.request
import time
import bs4


# 기사 제목 / 뉴스 링크 / 언론사 / 출간 일시 1분간격 반복출력

def get_news_info(news):
    news_title = news.find("h2", {"class":"tit"}).text
    news_link = news.find("a")["href"]
    news_mt = news.find("span", {"class":"medium"}).text
    news_mt_list = news_mt.split()
    news_media = news_mt_list[0]
    news_time = f"{news_mt_list[1]}  {news_mt_list[2]}"
    return [news_title, news_link, news_media, news_time]


url = "https://news.nate.com/recent?mid=n0100"


while True:
    html_object = urllib.request.urlopen(url)
    web_page = html_object.read()
    bs_object = bs4.BeautifulSoup(web_page, "html.parser")

    news_all = bs_object.find("div", {"class":"postSubjectContent"})
    news_list = news_all.findAll("div", {"class":"mduSubjectList"})
    
    header = ["기사 제목", "뉴스 링크", "언론사", "출간 일시"]
    print(header)
    for news in news_list:
        info = get_news_info(news)
        print(info)

    print()
    print()
    time.sleep(60)