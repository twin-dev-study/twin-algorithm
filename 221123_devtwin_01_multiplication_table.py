# 작업일 : 2022.11.23.수 23:00~ 2022.11.24.목 03:40
# 수정일 : 2022.11.24.목 19:26 (1 print('방법n')을 추가해 출력값 구분 / 2 방법3에서 g[-1]+1이나 g[-1]이나 출력값이 같은 이슈 발생 / 3 방법4 해결못한부분 설명 어려웠던 거 이젠 설명 가능)
# 작성자 : 이보형(boleesystem@gmail.com), 우태현(wth2052@gmail.com)
# 알고리즘 문제 : 구구단 2~9단 만들기


### 방법1. 이중 for문 : 1번째 for문 2~9단 / 2번째 for문 곱하는 숫자 1~9
print('방법1')
def multiple1():
     for a in range(2, 10):          # 1번째 for문 2~9단
         for b in range(1, 10):     # 2번째 for문 곱하는 숫자 1~9

             result = f'{a} * {b} = {a*b}'
             print(result)

multiple1()

    ## 인사이트1
     # range(start, stop) : start 시작할 시작위치, stop 끝낼 위치로 포함 안 함
     # range(1, 10)은 1부터 9까지 / 슬라이싱 f[0:10] 0부터 9까지
      # 참고. 슬라이싱 a[start : end : step]
      # - 각각 start, end, step 모두 양수와 음수를 가질 수 있음
      # - start: 슬라이싱을 시작할 시작 위치임
      # - end: 슬라이싱을 끝낼 위치로 end는 포함하지 않음
      # - step: stride(보폭)라고도 하며 몇개씩 끊어서 가져올지와 방향을 정함

    ## 인사이트2
     # 함수 적어야 함 def multiple1(): => 함수를 적었으면 호출해야 함. 안하면 오류가 남 multiple1()

    ## 인사이트3
     # f-string 사용 시 {함수+함수}의 형태로도 결과값 출력 가능
     # print(f'{x}*{y} = {x*y}')와 같은 형태로 변수의 결과값을 출력할 때 사용 가능



### 방법2. 2개의 배열 정해 놓고 꺼내기
print('방법2')
def multiple2():

    c = [2,3,4,5,6,7,8,9]
    d = [1,2,3,4,5,6,7,8,9]

    for e in c:
         for f in d:
             result = f'{e} * {f} = {e * f}'
             print(result)

multiple2()


    ## 인사이트1
     # 들여쓰기 : 함수선언 다음 배열=[]은 들여쓰기 / for문은 배열=[]에 맞춰쓰기 (배열=[]보다 들여쓰면 오류남)

    ## 인사이트2
     # 잘못된 코드(우태현) : range로 코드 낭비 (for x in range(a[0],a[-1]):)
	 # * 어차피 첫 번째부터 마지막 요소 값을 불러 오는 건데 굳이 range 함수를 사용

    ## 참고. 잘못된 코드(우태현)
     # a = [2,3,4,5,6,7,8,9]
     # b = [1,2,3,4,5,6,7,8,9,10]
     #
     # for x in range(a[0],a[-1]):  # 현재 몇단인지를 세는 for문 2단부터 출력한다 -1 마지막 요소를 가리킴. -2 뒤에서 두번째
     #     print(f'{x}단입니다~')
     #     for y in range(b[0],b[-1]):  # 뒤에 곱하기 값을 결정하는 for문 1~10 니까 9까지 돈다, 몇까지 곱할래?
     #         print(f'{x}*{y} = {x * y}')  # 구구단 출력하기



### 방법3. 1개의 배열 정해 놓고 꺼내기 (방법2 우태현 코드에서 응용 문제를 만듦)
print('방법3')
def multiple3():
    g = [1,2,3,4,5,6,7,8,9]

    for h in range(g[1],g[-1]+1):
         for i in g:
             result = f'{h} * {i} = {h * i}'
             print(result)

multiple3()


    ## 인사이트
     # range(start, stop)이니까 o[-1]+1로 마지막 요소 값을 불러 와야 함
     # (문제발생 - 2022.11.24. pm 7:10 추가) 다고 생각했는데 g[-1]+1이나 g[-1]이나 출력값이 같음?!



### 방법4. 중첩 while문 : 1번째 for문 2~9단 / 2번째 for문 곱하는 숫자 1~9
print('방법4')
def multiple4():

    j=2
    k=0
    while j < 10:       # 1번째 while문 2~9단
        while k < 9:    # 2번째 while문 곱하는 숫자 1~9
            k += 1
            print(f'{j} * {k} = {j * k}')
        k = 0
        j += 1

multiple4()


    ## 인사이트
     # 첫 번째 while문 다음에 j+=1를 적어서 초기값 j=2에서 1을 더한 값인 3부터 출력함
     # * j+=1을 삭제해 해결

    ## (해결완료) 해결 못한 부분
     # 설명가능 : k=0은 2단을 마치고 두 개의 while문을 마친 후에는 k=9이고 돌아가는 위치는 j=2가 아니라 첫 번째 while문임.
     # 그렇기 때문에 k는 0으로 대입해서 곱하는 수가 1부터 나오도록 해야 함

     # (해결 못한 부분이었던 이유) k += 1 설명 방법을 모르겠음
     # * j=2로 초기화해놨는데 k는 1이 아니라 0으로 초기화하고 +1하는 이유에 대해 설명할 워딩을 찾기 어려움
     # * 두번째 while문에서 곱해주는 숫자인 1~9까지를 만들어야 하기 때문에 k를 0으로 초기화한 것임

    ## 문제 있는 코드
     # j=1
     # k=0
     # while j < 9:
     #     j += 1
     #     while k <= 8: #1 2 3 4 5 6 7 8
     #         k += 1
     #         print(f'{j}*{k} = {j * k}')
     #     k = 1
     #     j += 1



### 방법5. input 방식
print('방법5')
def multiple5(number1, number2, number3):
    for x in range(number1, number2 + 1):
        print(f'---여기서부터는 {x}단입니다---')
        for y in range(1, number3 + 1):
            print(f'{x}*{y} = {x * y}')


num1 = int(input('몇 단부터 출력하시겠습니까?'))
num2 = int(input('몇 단까지 출력하시겠습니까?'))
num3 = int(input('1부터 몇까지 곱하시겠습니까?'))
print(f'{num1}단부터 {num2}단까지 {num3}까지 곱하겠습니다.')
multiple5(num1, num2, num3)


    ## 인사이트
     # num1 = int(input('몇 단부터 출력하시겠습니까?'))
     # 상단 부분에서 int를 작성하지 않아 입력창에 숫자를 입력한 경우 string으로 인식해 숫자 계산이 작동하지 않았음
     # * int(정수), string(문자열)