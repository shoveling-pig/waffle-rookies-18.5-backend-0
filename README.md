# waffle-rookies-18.5-backend-0

18.5기 김민찬
=========
Backend Seminar - 0th assignment
---------------------------
> ## 어려웠던 점
> * MySQL 관련 : User를 생성하고 권한을 부여하는 부분
> * Django 관련 : DRF library 활용법
> ## 질문
> * 클라이언트로부터 존재하지 않는 데이터에 대한 요청이 들어왔을 때, 처음에는 try&except 구문에서 Http404 객체를 사용하여 처리하였습니다. 그러나 Postman에서는 Status Code로 500 Intenal Server Error가 떠서 결국 다른 방식으로 해결할 수 밖에 없었습니다. 404 코드가 제대로 전달되지 않은 이유가 궁금합니다.
    try:
        ~
    except:
        raise Http404
- - -