from apscheduler.schedulers.background import BackgroundScheduler
import requests
import os

# Discord 메시지 전송 함수
def send_discord_message(title, description):
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        print("환경 변수 'WEBHOOK_URL'이 설정되지 않았습니다.")
        return

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
    else:
        print(f"메시지 전송 실패: {response.status_code}, {response.text}")

# 스케줄러 설정
scheduler = BackgroundScheduler()

# 알림 스케줄 추가
scheduler.add_job(
    lambda: send_discord_message(
        "🔔 5분 뒤 보라안개 침입 시작합니다!",
        "매일 11:55, 13:55, 18:55, 22:55, 00:55에 알림이 발송됩니다."
    ),
    'cron',
    hour=[11, 13, 18, 22, 0],
    minute=55
)
scheduler.add_job(
    lambda: send_discord_message(
        "🔔 5분 뒤 폭주 라쿤 시작합니다!",
        "*미리 접속하여 기사단 파티를 꾸려보세요.\n매일 11:10, 14:40, 16:40, 18:40, 20:40에 알림이 발송됩니다."
    ),
    'cron',
    hour=[11, 14, 16, 18, 20],
    minute=40
)
scheduler.add_job(
    lambda: send_discord_message(
        "♨️ 5분 뒤 왕실 온천 참여 시간입니다!",
        "*보스 라쿤 처치 후 온천으로 바로 이동하시면 좋습니다.\n온천이 끝나면 이어지는 기사단 컨텐츠도 다들 참여해주세요!\n매일 20:55에 알림이 발송됩니다."
    ),
    'cron',
    hour=20,
    minute=55
)
scheduler.add_job(
    lambda: send_discord_message(
        "😈 마신의 시련이 개방되었습니다!",
        "*모두 까먹지 마시고 마신의 시련 참여 부탁드립니다.\n화/목/토 11:00에 알림이 발송됩니다."
    ),
    'cron',
    day_of_week="tue,thu,sat",
    hour=11,
    minute=0
)
scheduler.add_job(
    lambda: send_discord_message(
        "⚔️ 심연 투기장이 개방되었습니다!",
        "*모두 까먹지 마시고 심연 투기장 참여 부탁드립니다.\n월/수/금 11:00에 알림이 발송됩니다."
    ),
    'cron',
    day_of_week="mon,wed,fri",
    hour=11,
    minute=0
)
scheduler.add_job(
    lambda: send_discord_message(
        "🗺️ 5분 뒤 선발 탐사 일정이 도래했습니다!",
        "*모두 까먹지 마시고 기사단 파티를 통해 선발 탐사 참여 부탁드립니다.\n일요일 11:00에 알림이 발송됩니다."
    ),
    'cron',
    day_of_week="sun",
    hour=11,
    minute=0
)

scheduler.start()

print("TOSbot 스케줄러가 실행 중입니다!")