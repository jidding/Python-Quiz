class Quiz:
       def __init__(self, question, choices, answer):
            self.question = question  # 문제 내용
            self.choices = choices    # 선택지 4개 (리스트 형태)
            self.answer = answer      # 정답 번호

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
    
    
    print(f"총 {len(quiz_list)}개의 퀴즈가 준비되었습니다!")