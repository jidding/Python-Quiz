class Quiz:
       def __init__(self, question, choices, answer):
            self.question = question  # 문제 내용
            self.choices = choices    # 선택지 4개 (리스트 형태)
            self.answer = answer      # 정답 번호

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes  # main에서 넘겨받은 퀴즈 5개를 저장
        self.best_score = 0     # 최고 점수 저장용 (나중에 사용)

    def display_menu(self):
        print("\n" + "="*40)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("="*40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("="*40)

    def run(self):
        # 무한 반복 루프: 사용자가 5번(종료)을 누를 때까지 메뉴를 계속 띄웁니다.
        while True:
            self.display_menu()
            
            # input()으로 입력을 받고, .strip()으로 양옆 공백(스페이스바)을 제거합니다.
            choice_input = input("선택: ").strip() 

            # 1. 빈 입력(엔터만 친 경우) 방어
            if not choice_input:
                print("⚠️ 값을 입력해 주세요.")
                continue
            
            # 2. 숫자 변환 실패(abc 등 문자 입력) 방어
            try:
                choice = int(choice_input)
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            
            # 3. 메뉴 선택에 따른 동작 분기
            if choice == 1:
                print("🛠️ '퀴즈 풀기' 기능은 아직 개발 중입니다!")
            elif choice == 2:
                print("🛠️ '퀴즈 추가' 기능은 아직 개발 중입니다!")
            elif choice == 3:
                print("🛠️ '퀴즈 목록' 기능은 아직 개발 중입니다!")
            elif choice == 4:
                print("🛠️ '점수 확인' 기능은 아직 개발 중입니다!")
            elif choice == 5:
                print("게임을 종료합니다. 플레이해주셔서 감사합니다! 👋")
                break # 여기서 무한 루프를 탈출하여 프로그램 종료
            else:
                # 1~5 범위를 벗어난 숫자 방어
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")

#  게임 실행을 위한 기본 세팅
if __name__ == "__main__":
    print("🎯 나만의 퀴즈 게임 데이터를 준비합니다...")
    
    
    quiz_list = [
        Quiz("2026 KBO 한국 시리즈 우승팀은?", ["한화 이글스", "기아 타이거즈", "삼성 라이온즈", "KT 위즈"], 3),
        Quiz("포켓몬스터의 대표 캐릭터인 전기쥐포켓몬의 이름은?.", ["이상해씨", "파이리", "꼬부기", "피카츄"], 4),
        Quiz("북한산이 존재하는 나라는?.", ["일본", "대한민국", "북한", "중국"], 2),
        Quiz("다음 중 대한민국의 광역시가 아닌 곳은?.", ["대전", "부산", "수원", "인천"], 3),
        Quiz("영화 '기생충'의 감독 이름은?.", ["봉준호", "이창동", "박찬욱", "김기영"], 1) 
        ]
    
    
    game = QuizGame(quiz_list)
    game.run()