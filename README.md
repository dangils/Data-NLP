# Data-NLP

## Neuro-Linguistic Programming(자연어 처리)
1) 데이터에서 분석할 특징(feature)을 선정
2) 데이터를 벡터 형태로 변환
3) 분석 기법을 적용하여 필요한 정보를 추출
4) 키워드 시각화

## 텍스트 분석 종류  
>text classification(텍스트 분류)  
test clustering(텍스트 군집화)  
sentiment analysis(감성 분석)  

## 자연어 처리시 필요한 패키지
- glob : 경로와 이름을 지정하여 파일을 처리하는 모듈( 데이터 병합 )
- re : 메타 문자를 지정하여 특정 규칙 작성(정규식 사용)
- reduce : 2차원 리스트를 1차원으로 줄이기 위한 모듈
- word_tokenize : 자연어 처리 패키지중 토큰화 작업을 위한 모듈
- stopwords : 자연어 처리 패키지중 불용어 정보를 제공
- WordNetLemmatizer : 단어 형태의 일반화를 위해 표제어 추출을 제공
- Counter : 데이터 집합에서 갯수 자동으로 계산
- stopwords, wordcloud : 워드클라우드를 그리기 위해 사용할 워드클라우드용 불용어 모듈과 워드클라우드 모듈
'
## 수행 과정
1) 데이터 수집
2) 데이터 선정, 데이터 전처리 [ 단어분석시 : 데이터 정규화, 단어 토큰화 ]
3) 구성 탐색 및 시각화


<hr>  

## Text Mining

1) 텍스트 전처리  
2) 특성 벡터화  
3) 머신러닝 모델 구축 및 학습/평가 프로세스 수행  
</br>     
특성 벡터화  
BoW(Bag of Words) :
문서가 가진 모든 단어에 대해 순서는 무시한 채 빈도만 고려하여 특성 벡터를 만드는법 (카운트 기반 벡터화, TF-IDF 기반 벡터화가 있음)      

  </br>   
     
- 카운트 기반 벡터화 : 단어 빈도를 부여하는 벡터화 방식으로 문서별 단어 빈도를 정리하여 문서 단어 행렬(DTM. Document Term Matrix)을 구성한다. 문서 d에 등장한 단어 t의 횟수는 tf(t,d)로 표현
[카운트 기반 벡터화는 사이킷런의 CountVectorizer 모듈에서 제공]      
     
   
   
- TF-IDF(Term Frequency-Inverse Document Frequency) 기반 벡터화 : 카운트 기반 벡터화에서 높은 빈도의 단어가 문장 구성상 많이 사용하는 단어일 수도 있다는 점을 보완한 벡터화, 특정 문서에 많이 나타나는 단어는 해당 문서의 단어 벡터에 가중치를 높임, 모든 문서에 많이 나타나는 단어는 가중치를 낮춤     
[TF-IDF 기반 벡터화는 사이킷런의 TfidfVectorizer 모듈에서 제공]



