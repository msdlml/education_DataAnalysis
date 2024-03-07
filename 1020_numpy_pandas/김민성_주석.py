import os, re, codecs
#자신의 저장경로를 입력해야 합니다. 
os.chdir(r'c:\temp')
f = open('friends101.txt', 'r', encoding = 'utf-8') #텍스트 파일을 읽기모드로 출력 
script101 = f.read() #읽어온 텍스트파일을 문자열 타입으로 변수에 저장

# 문자열 객체 슬라이싱
print(script101[:100]) #100자까지 출력   

Line = re.findall(r'Monica:.+', script101) #스크립트 안에서 Monica: 뒤에 아무 문자나 1개 이상있는 문자열을 찾음
#Line = re.findall('Monica:.+', script101)
#리스트 요소 중 앞에서 3개까지만 출력
print(Line[:3])
# 모니카의 대사만 모으기 
Line = re.findall(r'Monica:.+', script101)

# monica.txt 파일 만들기
f = open('monica.txt', 'w', encoding = 'utf-8') #텍스트를 쓰기모드로 염
monica = '' # monica라는 문자열 변수 생성
for i in Line:
	monica += i +'\n' # 모니카의 대사를 모은 리스트에서 하나씩 문자열 변수에 추가, 줄바꿈
f.write(monica) #문자열 변수를 텍스트파일에 작성
# 파일 닫기 
f.close()	

# 모니카의 대사만 출력해보기
for item in Line[:3]:
    print(item)

# 등장인물 이름 모으기 
print(re.findall(r'[A-Z][a-z]+: ', script101) ) #대본에서 대문자로 시작하고 소문자가 1개이상오고 마지막이 : 인 것을 찾음

# 중복 지우기
print(set(re.findall(r'[A-Z][a-z]+: ', script101))) #집합으로 변환해서 중복 제거

# 캐릭터 이름 한 줄로 출력하기
character = [x[:-2] for x in list(set(re.findall(r'[A-Z][a-z]+: ',script101)))] #집합을 리스트화하고 콜론제거 후 리스트에 저장

# 캐릭터 이름 각각 출력하기 
for i in character: 
    print(i)            

# 지문만 출력하기
re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101, re.VERBOSE) [:6]  
#(로 시작하고 ( 다음 알파벳 대소문자로 시작 후 아무문자나 1개이상 오고 알파벳소문자 혹은 . 으로 끝남 그리고 ) 로 끝나는 것 찾기

f = open('friends101.txt','r') #텍스트를 읽기모드로 염
sentences = f.readlines()   #읽어온 텍스트를 리스트로 저장
# 20개만 출력해보기
for i in sentences[:20]:			## 먼저 문장 20개만 가져와 실험해 보겠습니다
    if re.match(r'[A-Z][a-z]+:', i): 	## match 문으로 문장 맨 앞에서 패턴을 찾습니다 
        print(i)

# would가 나오는 문장만 추출하기 
would = [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
# take가 들어간 문장만 추출하기 
take = [ i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search(' take',i)]
# take가 들어간 문장 출력하기
for i in take:
	print(i)
 
# would가 들어간 문장 파일로 만들기 
newf = open('would.txt','w')	
newf.writelines(would)		
