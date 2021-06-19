import requests
import vk_api

class VK:



    def getInfo(self, id, auth):
        vk_session = vk_api.VkApi(auth[0], auth[1])
        vk_session.auth()
        token = vk_session.token['access_token']
        version =  vk_session.api_version
        url_to_find = f'https://api.vk.com/method/users.get?&fields=photo_50&user_ids={id}&access_token={token}&v=5.131'
        resp = requests.get(url_to_find)
        return resp.json()

    def find(self, link, token, version):
        url_to_find = f'https://api.vk.com/method/users.get?user_ids={link}&access_token={token}&v={version}'
        resp = requests.get(url_to_find)

        return resp.json()

    def find_friend(self, link, auth):
        vk_session = vk_api.VkApi(auth[0], auth[1])
        # vk_session = vk_api.VkApi('+79120848001', 'csxvmn28')
        vk_session.auth()
        token = vk_session.token['access_token']
        version =  vk_session.api_version
        # print(token)
        # print(version)


        ids = self.find(link=link, token=token, version=version)['response'][0]['id']
        # print(ids)

        session = requests.session()
        to_return = []
        try:
            response = session.get(f'https://api.vk.com/method/friends.get?user_id={ids}&access_token={token}&v={version}').json()
            for element in response['response']['items']:
                to_return.append(element)
        except Exception as ex:
            # print(ex)
            pass
        return to_return

    def find_by_more(self, args, auth):
        vk = VK()
        to_return = []
        for arg in range(len(args)):
            if arg == 0:
                first = vk.find_friend(args[arg], auth)
            else:
                second = vk.find_friend(args[arg], auth)
                for f in first:
                    for s in second:
                        if f == s:
                            to_return.append(f)
                else:
                    f = to_return
        else:
            return to_return



# vk = VK()
# links = ['ad_mini_str_a_tor', 'nastejnka']
# print(vk.find_by_more(args=links))

