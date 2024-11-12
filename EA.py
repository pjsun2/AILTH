import openai

# OpenAI API 키 설정
openai.api_key_path = r"D:\Code\api_key.txt"

def extract_ingredients(prompt, goal):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"사용자의 목표는 '{goal}'입니다. 입력된 식재료와 양을 분석하여 성분표를 제공하고 탄수화물, 단백질, 지방 총합과 칼로리 총합 값을 JSON 구조로 반환하세요. 또한, 목표에 맞는 식단 피드백을 한국어로 제공하세요."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

print("식단 성분 분석기를 시작합니다. '종료'라고 입력하면 프로그램이 종료됩니다.")

# 사용자 목표 입력
goal = ""
while goal not in ["체지방 감량", "근육량 증대"]:
    goal = input("당신의 목표를 입력하세요 ('체지방 감량' 또는 '근육량 증대'): ").strip()
    if goal not in ["체지방 감량", "근육량 증대"]:
        print("유효한 목표를 입력하세요 ('체지방 감량' 또는 '근육량 증대').")

while True:
    user_input = input("\n식단을 입력하세요: ")
    
    if user_input.lower() in ["종료", "quit", "exit"]:
        print("프로그램을 종료합니다.")
        break
    
    if not user_input.strip():
        print("유효한 식단을 입력하세요.")
        continue

    try:
        ingredients = extract_ingredients(user_input, goal)
        print("추출된 식재료 및 성분표:", ingredients)
    except openai.error.OpenAIError as e:
        print("OpenAI API 오류가 발생했습니다:", str(e))
    except Exception as e:
        print("일반 오류가 발생했습니다:", str(e))
