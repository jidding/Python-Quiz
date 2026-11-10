import json
import os


class Quiz:
       def __init__(self, question, choices, answer):
            self.question = question  # 문제 내용
            self.choices = choices    # 선택지 4개 (리스트 형태)
            self.answer = answer      # 정답 번호

class QuizGame:
    def __init__(self, quizzes):
        self.filename = "state.json"
        self.default_quizzes = quizzes 
        
        # 게임 시작 시 파일에서 데이터 불러오기
        self.quizzes, self.best_score = self.load_data()

    # ---  파일 불러오기 (Load) ---
    def load_data(self):
        # state.json 파일이 아예 없는 경우 (첫 실행)
        if not os.path.exists(self.filename):
            print("📂 저장된 데이터 파일이 없어 기본 퀴즈를 로드합니다.")
            return self.default_quizzes, 0

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # 저장된 퀴즈 딕셔너리 형태를 Quiz 객체로 다시 변환
                loaded_quizzes = []
                for q in data.get("quizzes", []):
                    loaded_quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))
                
                best_score = data.get("best_score", 0)
                
                print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(loaded_quizzes)}개, 최고점수 {best_score}점)")
                return loaded_quizzes, best_score
                
        except (json.JSONDecodeError, Exception) as e:
            # 파일이 손상되었거나 읽기 오류가 난 경우 예외 처리
            print("⚠️ 데이터 파일이 손상되었거나 읽을 수 없습니다. 기본 데이터로 복구합니다.")
            return self.default_quizzes, 0

    # --- 🌟 파일 저장하기 (Save) ---
    def save_data(self):
        try:
            # Quiz 객체 리스트를 JSON이 이해할 수 있는 딕셔너리 형태로 변환
            quizzes_data = []
            for q in self.quizzes:
                quizzes_data.append({
                    "question": q.question,
                    "choices": q.choices,
                    "answer": q.answer
                })
                
            data = {
                "quizzes": quizzes_data,
                "best_score": self.best_score
            }
            
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("💾 데이터가 state.json에 안전하게 저장되었습니다.")
        except Exception as e:
            print(f"⚠️ 파일 저장 중 오류가 발생했습니다: {e}")

    def display_menu(self):
        print("\n" + "="*40)
        print("         퀴즈 게임 ")
        print("="*40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("="*40)

    #퀴즈 목록 보기 기능 ---
    def display_quiz_list(self):
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        # 퀴즈가 하나도 없을 때의 방어 코드
        if not self.quizzes:
            print("현재 등록된 퀴즈가 없습니다.")
        else:
            # enumerate를 사용해서 1번부터 번호 매겨서 출력
            for i, quiz in enumerate(self.quizzes, start=1):
                print(f"[{i}] {quiz.question}")
        print("-" * 40)

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        
        # 1. 문제 입력 (빈칸 방어)
        while True:
            question = input("문제를 입력하세요: ").strip()
            if not question:
                print("⚠️ 문제가 비어있습니다. 다시 입력해 주세요.")
            else:
                break
                
        # 2. 선택지 4개 입력 
        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()
                if not choice:
                    print("⚠️ 선택지 내용은 비워둘 수 없습니다. 다시 입력해 주세요.")
                else:
                    choices.append(choice)
                    break
                    
        # 3. 정답 번호 입력 (숫자 및 1~4 범위)
        while True:
            answer_input = input("정답 번호 (1-4): ").strip()
            try:
                answer = int(answer_input)
                if 1 <= answer <= 4:
                    break
                else:
                    print("⚠️ 1에서 4 사이의 숫자를 입력해 주세요.")
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 숫자로 입력해 주세요.")
                
        # 4. 새로운 Quiz 객체를 만들고 목록(quizzes)에 추가
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        self.save_data()
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")

    def play_quiz(self):
        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        print("-" * 40)
        
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요!")
            return

        score = 0
        total = len(self.quizzes)

        # 등록된 퀴즈를 하나씩 출제
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {i}]")
            print(quiz.question)
            for j, choice in enumerate(quiz.choices, start=1):
                print(f"{j}. {choice}")
            
            # 사용자 정답 입력 받기 (예외 처리 포함)
            while True:
                answer_input = input("\n정답 입력 (1-4): ").strip()
                if not answer_input:
                    print("⚠️ 값을 입력해 주세요.")
                    continue
                try:
                    user_answer = int(answer_input)
                    if 1 <= user_answer <= 4:
                        break
                    else:
                        print("⚠️ 1에서 4 사이의 숫자를 입력해 주세요.")
                except ValueError:
                    print("⚠️ 잘못된 입력입니다. 숫자로 입력해 주세요.")

            # 정답 확인
            if user_answer == quiz.answer:
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")
                
        # 결과 출력 및 최고 점수 갱신
        print("\n" + "="*40)
        print(f"🏆 결과: {total}문제 중 {score}문제 정답!")
        
        # 기존 최고 점수보다 높으면 갱신
        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("="*40)

    # 최고 점수 확인 기능
    def show_best_score(self):
        print("\n" + "="*40)
        print(f"🏆 현재 최고 점수: {self.best_score}점")
        print("="*40)

    def run(self):
        while True:
            self.display_menu()
            choice_input = input("선택: ").strip() 

            if not choice_input:
                print("⚠️ 값을 입력해 주세요.")
                continue
            
            try:
                choice = int(choice_input)
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.display_quiz_list()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                print("게임을 종료합니다. 플레이해주셔서 감사합니다! 👋")
                break 
            else:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")

#  게임 실행을 위한 기본 세팅
if __name__ == "__main__":
    print("🎯 나만의 퀴즈 게임 데이터를 준비합니다...")
    
    
    quiz_list = [
        Quiz("2026 KBO 한국 시리즈 우승팀은?", ["한화 이글스", "기아 타이거즈", "삼성 라이온즈", "KT 위즈"], 3),
        Quiz("포켓몬스터의 대표 캐릭터인 전기쥐포켓몬의 이름은?.", ["이상해씨", "파이리", "꼬부기", "피카츄"], 4),
        Quiz("북한산이 존재하는 나라는?.", ["일본", "대한민국", "북한", "중국"], 2),
        Quiz("다음 중 대한민국의 광역시가 아닌 곳은?.", ["대전", "부산", "수원", "인천"], 3),
        Quiz("영화 '기생충'의 감독 이름은?.3", ["봉준호", "이창동", "박찬욱", "김기영"], 1) 
        ]
    
    
    game = QuizGame(quiz_list)
    game.run()