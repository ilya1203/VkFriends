from django.shortcuts import render
from time import sleep
from .finder import VK

def index(request):
    args = []
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
            return render(request, "index.html", {"fnd": friend})


    return render(request, "index.html", {})