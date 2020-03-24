from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
import os
from viber_bot import viber_bot

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='XON',
    avatar='https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/f09b'
           '/fc477e80d5306023ccf92a07170886fee98bba96aca04959700207a62cc6f09b.jpg',
    auth_token='4b231b604267d24e-d830fc6e7126277a-a1720ec63a7aa5bc'
))



@app.route('/', methods=['POST'])
def incoming():
    viber_request = viber.parse_request(request.get_data())

    bot = viber_bot()
    bot.set_request(viber_request)
    messages = bot.get_response()
    if messages is not None:
        viber.send_messages(bot.current_user.viber_id, messages)
    return Response(status=200)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
