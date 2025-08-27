import json
from datetime import date, datetime

def main():
    """
    사용자로부터 개인 정보와 프로젝트 이력을 입력받아
    JSON 형태의 자기소개서를 생성하고 출력하는 메인 함수
    """
    person = {}

    # --- 1. 기본 정보 입력 ---
    print("--- 기본 정보를 입력해주세요 ---")
    person['name'] = input("이름이 무엇인가요? ")
    person['sex'] = input("성별이 무엇인가요? (예: 남성/여성) ")
    person['email'] = input("이메일 주소가 무엇인가요? ")
    person['phone'] = input("연락처가 무엇인가요? ")
    person['address'] = input("거주지가 어디인가요? ")
    person['major'] = input("전공이 무엇인가요? ")

    # --- 2. 생년월일 입력 및 나이/D-Day 계산 ---
    while True:
        birth_date_str = input("생년월일을 입력하세요 (YYYY-MM-DD): ")
        try:
            # 문자열을 날짜 객체로 변환 (시간 정보 제외)
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            break  # 올바른 형식이면 반복문 탈출
        except ValueError:
            print("❌ 잘못된 형식입니다. YYYY-MM-DD 형식으로 다시 입력해주세요.")

    today = date.today()

    # 만 나이 계산
    # (오늘 연도 - 태어난 연도) 에서 생일이 지났는지 여부를 빼서 계산
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    person['age'] = age

    # 다음 생일까지 남은 날짜(D-Day) 계산
    try:
        this_year_birthday = birth_date.replace(year=today.year)
    except ValueError:  # 2월 29일생이 윤년이 아닌 해를 만났을 때
        this_year_birthday = birth_date.replace(year=today.year, day=28)

    if this_year_birthday < today:
        # 올해 생일이 지났으면, 다음 생일은 내년
        next_birthday = this_year_birthday.replace(year=today.year + 1)
    else:
        # 올해 생일이 아직 안 지났거나 오늘이라면
        next_birthday = this_year_birthday

    d_day = (next_birthday - today).days
    person['d_day_to_birthday'] = d_day

    # --- 3. 기술 및 관심 분야 정보 입력 ---
    print("--- 기술 및 관심 분야 정보를 입력해주세요 ---")
    skills = input("보유 기술을 쉼표(,)로 구분하여 입력하세요 (예: Python, Java, SQL): ")
    interests = input("관심 분야를 쉼표(,)로 구분하여 입력하세요 (예: AI, Web Development): ")
    person['skills'] = [skill.strip() for skill in skills.split(',') if skill.strip()]
    person['interests'] = [interest.strip() for interest in interests.split(',') if interest.strip()]

    # --- 4. 프로젝트 이력 입력 ---
    print("--- 프로젝트 이력을 입력해주세요 ---")
    projects = []
    while True:
        project_name = input("프로젝트명을 입력하세요 (종료하려면 '끝' 입력): ")
        if project_name.lower() == '끝':
            break
        
        project_topic = input("프로젝트 주제를 입력하세요: ")
        project_tech = input("사용 기술을 입력하세요: ")
        project_duration = input("프로젝트 기간을 입력하세요 (예: 2024.01 ~ 2024.03): ")
        
        projects.append({
            "name": project_name,
            "topic": project_topic,
            "tech": project_tech,
            "duration": project_duration
        })
        print("프로젝트가 추가되었습니다.\n")

    person['projects'] = projects


    # --- 4. 최종 자기소개서 출력 ---
    print("\n\n--- 최종 자기소개서 (JSON) ---")
    # json.dumps를 사용하여 딕셔너리를 보기 좋은 JSON 문자열로 변환
    # indent: 들여쓰기, ensure_ascii=False: 한글이 깨지지 않도록 설정
    print(json.dumps(person, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()