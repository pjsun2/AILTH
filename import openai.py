import openai

# OpenAI API 키 설정
openai.api_key_path = r"D:\NAI\api_key.txt"

def extract_ingredients(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "사용자의 입력에서 식재료와 양을 파악 후 성분표를 분석하고 탄수화물, 단백질, 지방 총합과 칼로리 총합 값을 간단한 JSON 구조로 반환하세요 이때 한국어로 반환해야합니다. 그리고 식단에 대한 간단한 피드백을 넣어주세요"},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

print("식단 성분 분석기를 시작합니다. '종료'라고 입력하면 프로그램이 종료됩니다.")

while True:
    user_input = input("식단을 입력하세요: ")
    
    if user_input.lower() in ["종료", "quit", "exit"]:
        print("프로그램을 종료합니다.")
        break
    
    if not user_input.strip():
        print("유효한 식단을 입력하세요.")
        continue

    try:
        ingredients = extract_ingredients(user_input)
        print("추출된 식재료 및 성분표:", ingredients)
    except openai.error.OpenAIError as e:
        print("OpenAI API 오류가 발생했습니다:", str(e))
    except Exception as e:
        print("일반 오류가 발생했습니다:", str(e))
