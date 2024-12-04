from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/api/webhook", methods=["POST"])
def send_webhook():
    # 환경 변수에서 Webhook URL 가져오기
    webhook_url = os.getenv("WEBHOOK_URL")

    # 메시지 데이터
    data = {
        "embeds": [
            {
                "title": "🔔 TOSbot 테스트 메시지입니다!",
                "description": "이 메시지는 Vercel에서 실행된 함수로 전송되었습니다. 🎉",
                "color": 0x00FF00  # 초록색
            }
        ]
    }

    # 디스코드 Webhook 요청
    response = requests.post(webhook_url, json=data, verify=False)

    if response.status_code == 204:
        return jsonify({"message": "메시지가 성공적으로 전송됐습니다!"}), 200
    else:
        return jsonify({"error": f"전송 실패: {response.status_code}, {response.text}"}), 400

if __name__ == "__main__":
    app.run()
