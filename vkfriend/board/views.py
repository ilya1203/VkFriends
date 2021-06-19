from django.shortcuts import render
from time import sleep, gmtime
from .finder import VK

def index(request):
    args = []
    tm = gmtime()
    if request.GET:
        auth = [request.GET['login'], request.GET['paassword']]
        for l in request.GET.getlist('link'):
            args.append(l.split('/')[-1])
        else:
            vk = VK()
            finded = vk.find_by_more(args, auth)
            friend = []
            for f in finded:
                while 1:
                    try:
                        infos = vk.getInfo(f, auth)['response']
                        friend.append({'name': f'{infos[0]["first_name"]} {infos[0]["last_name"]}', 'id': f})
                        try:
                            friend[-1]['img'] = infos[0]['photo_50']
                        except:
                            pass
                        break
                    except:
                        sleep(1)

            tm_search = [f'{abs(gmtime().tm_hour-tm.tm_hour)}:{abs(gmtime().tm_min-tm.tm_min)}:{abs(gmtime().tm_sec-tm.tm_sec)}']
            return render(request, "index.html", {"fnd": friend, 'time':tm_search})


    return render(request, "index.html", {})