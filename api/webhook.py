from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/api/webhook", methods=["POST"])
def send_webhook():
    # 환경 변수에서 Webhook URL 가져오기
    webhook_url = os.getenv("https://discord.com/api/webhooks/1313338442155032627/Trmc3fYWf1gei4pdUuJPxb25am2UVXGe0lTX7SEuoHtr7dtMn3EankeCjKbA9KK6CKg9")

    # 요청 데이터 처리 (옵션)
    data_from_request = request.json

    # Discord로 보낼 메시지 데이터
    data = {
        "embeds": [
            {
                "title": "🔔 TOSbot 알림",
                "description": data_from_request.get("message", "테스트 메시지입니다! 🎉"),
                "color": 0x00FF00  # 초록색
            }
        ]
    }

    # Discord Webhook 요청
    response = requests.post(webhook_url, json=data, verify=False)

    if response.status_code == 204:
        return jsonify({"message": "메시지가 성공적으로 전송되었습니다!"}), 200
    else:
        return jsonify({"error": f"전송 실패: {response.status_code}, {response.text}"}), 400
