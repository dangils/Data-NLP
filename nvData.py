'''
Naver Crawling Process

1.검색어 지정
- srcText=''
2.네이버 뉴스로 검색
- url 구성 : url = base + noew + srcText
- url 접속과 검색 교청 : urllib.request.urlopen()
- 데이터 json 반환 : json.load()
3.리스트 저장
- getPostData()
4.리스트 json파일로 저장
json.dumps()
'''
#===============================================#


import os
import sys
import urllib.request
import datetime
import time
import json

client_id = '발급 받은 Cleint ID' # 발급 받은 Cleint ID
client_secret = '발급 받은 Cleint PW'

#URL 접속을 요청하고 응답을 받아서 반환
def getRequestUrl(url):
    req = urllib.request.Request(url)
    # api 사용을 위한 ID,PW 요청 객체 헤더에 추가
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try : 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(),url))
        return None

# 네이버 뉴스검색 url 생성, 응답 데이터 json 반환
def getNaverSearch(node, srcText, start, display) :
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url) #[code1]

    if(responseDecode==None):
        return None
    else:
        return json.loads(responseDecode)


#검색 결과 항목 저장
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    #문자열 형태 날짜 객체로 변환, 표준시간과 맞추기 위해 9시간 +
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'org_link':org_link,'link':org_link,'pDate':pDate})

    return


    
def main():
    node = 'news' #크롤링 대상
    srcText = input('검색어를 입력하세요: ')
    cnt = 0 #검색 결과 카운트
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100) # [code2] start =1 , display=100
    total = jsonResponse['total']

    while ((jsonResponse != None) and (jsonResponse['display'])!=0):
        for post in jsonResponse['items']:
            cnt+=1
            getPostData(post, jsonResult, cnt) #[code3]
        
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100) #[code2]
    
    print('전체 검색 : %d 건' %total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding = 'utf8') as outfile:
            jsonFile = json.dumps(jsonResult, indent = 4 , sort_keys = True, ensure_ascii = False)

            outfile.write(jsonFile)
    
    print("가져온 데이터 : %d 건" %(cnt))
    print('%s_namer_%s.json SAVED' % (srcText, node))

#해당 파일이 임포트 되지 않고 독립적으로 실행할경우 main()이 호출되어 시작
if __name__=='__main__':
    main()

