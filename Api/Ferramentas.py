import requests
import json as js

'''Destinada a leitura das labels do Trello'''
class Trello():
    import requests
    import json as js
    def __init__(self):
        # __init__ é o nosso contrutor em Python, obrigatórimante precisa poassar valores de instância

        '''Para obter as informações de como começar a utilizar a API do Trello, você pode acessar esse
        link https://developers.trello.com/docs/api-introduction !
        Acessando esse link já logado na conta do Trello é possível obter a Chave de acesso,
         ela será necessária para obter os dados.'''
        self.key = ''
        self.token = ''
        self.board = ''
        '''Aqui nesta classe definiremos quais parametros serão definidos'''

    def getBoard(self):
        '''Todas as tarefas do quadro'''

        url = "https://api.trello.com/1/boards/" + self.board

        querystring = {"actions": "all", "boardStars": "none", "cards": "none", "card_pluginData": "false",
                       "checklists": "none", "customFields": "false",
                       "fields": "name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames",
                       "lists": "open", "members": "none", "memberships": "none", "membersInvited": "none",
                       "membersInvited_fields": "all", "pluginData": "false", "organization": "false",
                       "organization_pluginData": "false", "myPrefs": "false", "tags": "false", "key": self.key,
                       "token": self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    def getCards(self):

        '''Pegar informações do card'''
        self.limit = '30'
        url = 'https://api.trello.com/1/boards/' + \
              self.board + '/cards/?limit=' + \
              self.limit + '&fields=name&members=true&member_fields=fullName&key=' + \
              self.key + '&token=' + \
              self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url, headers=headers)
        dic = js.loads(call.text)

        print(dic)

    def getCardID(self):


        self.idCard = '5825f7408fc73004763693d7'

        url = 'https://trello.com/1/boards/' + self.board + '/cards/' + self.idCard + '?key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url, headers=headers)
        dic = js.loads(call.text)

        print(dic)

    def getMember(self):
        '''Este método pega o que cada membro obtém por tarefa, '''

        self.member = '550a1457c58a3212b6851477'

        url = "https://api.trello.com/1/members/" + self.member

        querystring = {"boardBackgrounds": "none", "boardsInvited_fields": "name,closed,idOrganization,pinned",
                       "boardStars": "false", "cards": "none", "customBoardBackgrounds": "none", "customEmoji": "none",
                       "customStickers": "none", "fields": "all", "organizations": "none", "organization_fields": "all",
                       "organization_paid_account": "false", "organizationsInvited": "none",
                       "organizationsInvited_fields": "all", "paid_account": "false", "savedSearches": "false",
                       "tokens": "none", "key": self.key, "token": self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

'''Deixar em branco para definir outras ferramentas a ser ultilizadas'''


class ferramente2():
    pass

class ferramente3():
    pass
