from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Discord 메시지 전송 함수
def send_discord_message(title, description):
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        print("환경 변수 'WEBHOOK_URL'이 설정되지 않았습니다.")
        return {"error": "환경 변수 'WEBHOOK_URL'이 설정되지 않았습니다."}, 500

    data = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": 0x00FF00  # 초록색
            }
        ]
    }

    response = requests.post(webhook_url, json=data, verify=False)
    if response.status_code == 204:
        print(f"메시지 전송 성공: {title}")
        return {"message": "메시지가 성공적으로 전송되었습니다!"}, 200
    else:
        print(f"메시지 전송 실패: {response.status_code}, {response.text}")
        return {"error": f"전송 실패: {response.status_code}, {response.text}"}, 400

# 즉시 테스트 API
@app.route("/api/test-push", methods=["GET"])
def test_push():
    result, status_code = send_discord_message(
        "🔔 테스트 알림",
        "이것은 테스트 메시지입니다! 설정이 제대로 되었는지 확인하세요. 😊"
    )
    return jsonify(result), status_code

# 기본 루트 경로
@app.route("/")
def home():
    return jsonify({"message": "TOSbot Webhook API가 실행 중입니다!"})