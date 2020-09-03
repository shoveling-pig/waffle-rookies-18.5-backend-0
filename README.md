# waffle-rookies-18.5-backend-0

18.5기 김민찬
=========
Backend 세미나 과제 1
---------------------------
> ## 어려웠던 점
> * MySQL에서 User를 생성하고 권한을 주는 파트
> * DRF의 개념
> ## 질문
> * 존재하지 않는 데이터에 대한 요청이 들어왔을 때, try except 구문에서 Http404 객체를 사용하여 처리하였는데 Postman에서는 500 Error가 떠서 다른 방식으로 처리했습니다. 404 코드가 전달되지 않은 이유가 궁금합니다.
	try:
	    ~
	except:
	    raise Http404
- - -