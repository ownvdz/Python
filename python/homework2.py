import os
path_name = "c:/본인학번"
full_filename = path_name + "/list.txt" # 읽을 파일의 전체경로
if os.path.isfile(full_filename):
    f = open(full_filename, "r")
    # 점수 정보를 저장할 리스트를 생성한다.
    scores = []
    while True:
        # 파일에서 한 줄을 읽어온다.
        line = f.readline()
        # 읽어온 내용이 없으면 반복문을 종료한다.
        if not line:
            break
        # 읽어온 내용을 ,(쉼표)로 분해한다. split()이용
        li = line.strip().split(",")
        # 분해한 데이터의 개수가 4 개인지 확인한다.
        if len(li) == 4:
        # 4 개인 경우에만
        # 딕셔너리를 생성하여
        # 이름(name), 국어점수(kor), 영어점수(eng), 수학점수(mat)를
        # 딕셔너리에 추가하고
            dict = {}
            dict[
        # 해당 딕셔너리를 점수 정보를 저장할 리스트에 추가한다.

    f.close()
 # 반복문을 통해 점수 정보를 저장할 리스트의 모든 내용을 실행화면 예제를 참고하여
 # 화면에 출력한다.