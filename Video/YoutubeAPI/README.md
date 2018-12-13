YouTube Data API v3 사용

준비
(참고:https://github.com/youtube/api-samples/blob/master/python/README.md)

1. pip install --upgrade google-api-python-client

2. pip install --upgrade google-api-python-client

3. 승인된 자바스크립트 원본
"http://localhost:8080"
"http://127.0.0.1:8080"

4. 승인된 리디렉션 URL
"http://localhost:8080/"
"http://127.0.0.1/oauth2callback"

5. Test : python sample.py --arg1=value1 --arg2=value2 ...

사용 예시

```
 Video ID : 6Uk5CIm4IPI
 Caption ID : SO_yf9MW10MySZwVMmzvA6uYGT0t6ccgXPhralxBKVw=
 python captions.py --videoid=6Uk5CIm4IPI --action=list
 python captions.py --videoid=6Uk5CIm4IPI --captionid=SO_yf9MW10MySZwVMmzvA6uYGT0t6ccgXPhralxBKVw= --action=download
```

6. url과 view에 youtube로 주석 처리한 부분 -> youtube api web으로 구현
   하지만 oauth2callback 함수에서 오류 발생
