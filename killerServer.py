import Requests

target = 'http://github.com/WebDevChaos987/wine-9.2-custom/edit/main/server/signal.c'

while True:
    r = requests.get(target, timeout=5)
    print(r.status_code)
