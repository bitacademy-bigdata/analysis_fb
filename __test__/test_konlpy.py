from konlpy.tag import Kkma

kkma = Kkma()

sentences = kkma.sentences(u'네, 안녕하세요. 반갑습니다.')
print(sentences)

nouns = kkma.nouns(u'1990년대활약한스타조지웨아아프리카라')
print(nouns)

pos = kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^')
print(pos)
