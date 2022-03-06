
from github import Github
from flask import jsonify, Flask, render_template, send_file, make_response, url_for, Response, redirect, request
from datetime import datetime
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html', PageTitle='Landing Page')




#filtro 1:

access_token = "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"
g = Github(access_token)



class Data:
       def filtroData(self, DATA):
        api_base_url = 'https://api.github.com'
        date = DATA
        endpoint_path = f'https://api.github.com/search/repositories?q=user:viniyan+created:>{date}'
        endpoint = f'{endpoint_path}'
        r = requests.get(endpoint)
        x = json.loads(r.text)
        a = []

        y = x['items']
        for i in y:
            for z in i:
                k = i['full_name']
                a.append(k)

        print(a)
        return a

#x = Data
#x.filtroData(x, '2022-02-01')
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#filtro 2:

class Conteudo:
    def filtroConteudoRepo(self, nomeArquivo):
        api_base_url = 'https://api.github.com'
        nome = nomeArquivo
        endpoint_path = f'https://api.github.com/search/code?q=user:viniyan+language:python+{nome}%20in:file'
        endpoint = f'{endpoint_path}'
        r = requests.get(endpoint)
        x = json.loads(r.text)
        a = []


        y = x['items']
        for i in y:

           for z in i:
               k = i['name']
               a.append(k)

        print(a)
        return a
    
#x = Conteudo
#x.filtroConteudoRepo(x, 'app')
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#filtro 3:

class FiltroLinguagem:
    def filtroLinguagem(self):
        base_url = ('https://api.github.com/{}')
        path = 'users/viniyan'
        token = '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'
        headers = {'authorization': 'Bearer {}'.format(token)}
        response = requests.get(base_url.format(path), headers=headers)  # autenticar o github

        api_base_url = 'https://api.github.com'
        owner = 'viniyan'
        repo = 'YEarn'
        endpoint_path = f'/repos/{owner}/{repo}/languages'
        endpoint = f'{api_base_url}{endpoint_path}'
        r = requests.get(endpoint)
        print(r.text)

x = FiltroLinguagem
x.filtroLinguagem(x)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ordenação alfabética:

class OrdenarAlfabeticamente:
    def ordenaAlfa(self):
        base_url = ('https://api.github.com/{}')
        path = 'users/viniyan'
        token = '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'
        headers = {'authorization': 'Bearer {}'.format(token)}
        response = requests.get(base_url.format(path), headers=headers)  # autenticar o github



        api_base_url = 'https://api.github.com/users/viniyan'
        endpoint_path = '/repos'
        endpoint = f'{api_base_url}{endpoint_path}'
        r = requests.get(endpoint, data={'sort': 'full_name', 'per_page': 100})

        x = r.text
        json_completo = json.loads(x)
        #pprint.pprint(json_completo)
        repo1 = json_completo[0]
        repo2 = json_completo[1]
        repo3 = json_completo[2]
        repo4 = json_completo[3]
        repo5 = json_completo[4]
        nome1 = repo1['name']
        nome2 = repo2['name']
        nome3 = repo3['name']
        nome4 = repo4['name']
        nome5 = repo5['name']
        nomes = [nome1, nome2, nome3, nome4, nome5]
        ordenado = sorted(nomes, key= str.casefold)
        print(ordenado)

#x = OrdenarAlfabeticamente
#x.ordenaAlfa(x)
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Data do último commit:

class UltimoCommit:
    def achaData(self):
        base_url = ('https://api.github.com/{}')
        path = 'users/viniyan'
        token = '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'
        headers = {'authorization': 'Bearer {}'.format(token)}
        response = requests.get(base_url.format(path), headers=headers)  # autenticar o github

        api_base_url = 'https://api.github.com'
        owner = 'viniyan'
        repo = input('Digite o nome do repositório que deseja consultar:')

        endpoint_path = f'/repos/{owner}/{repo}/commits'
        endpoint = f'{api_base_url}{endpoint_path}'

        r = requests.get(endpoint)
        print(r.status_code)
        x = r.text
        json_completo = json.loads(x)
        json_dicts = json_completo[0]
        dict_values = json_dicts.values()
        for i in dict_values:
            if type(i) == dict:
                x = i.values()
                for k in x:
                    if type(k) == dict:
                        y = list(k.values())
                        data = y[2]
                        print(data)
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Pesquisa simples:

class ControllerFiltro:
    def filtroNome(self, NOME):    #nome do repo
        api_base_url = 'https://api.github.com'
        nome = NOME
        endpoint_path = f'https://api.github.com/search/repositories?q=user:viniyan+{nome}%20in:name'
        endpoint = f'{endpoint_path}'
        r = requests.get(endpoint)
        x = json.loads(r.text)
        a = []

        y = x['items']
        for i in y:
            for z in i:
                k = i['full_name']
                a.append(k)

        print(a)
        return a

x = ControllerFiltro
x.filtroNome(x, 'De')





@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['date']

    def filtroData(DATA):
        api_base_url = 'https://api.github.com'
        date = DATA
        endpoint_path = f'https://api.github.com/search/repositories?q=user:viniyan+created:>{date}'
        endpoint = f'{endpoint_path}'
        r = requests.get(endpoint)
        x = json.loads(r.text)
        a = []

        y = x['items']
        for i in y:
            for z in i:
                k = i['full_name']
                a.append(k)

        print(a)
        return a

    projectpath = request.form['date']
    
    return str(filtroData(projectpath))
    
#x = Data
#x.filtroData(x, '2022-02-01')

def filtroConteudoRepo(nomeArquivo):
    api_base_url = 'https://api.github.com'
    nome = nomeArquivo
    endpoint_path = f'https://api.github.com/search/code?q=user:viniyan+language:python+{nome}%20in:file'
    endpoint = f'{endpoint_path}'
    r = requests.get(endpoint)
    x = json.loads(r.text)
    a = []


    y = x['items']
    for i in y:

       for z in i:
           k = i['name']
           a.append(k)

    print(a)
    return a


@app.route('/handle_content', methods=['POST'])
def handle_content():

    projectpath = request.form['content']
    print(filtroConteudoRepo(projectpath))
    print(type(str(filtroConteudoRepo(projectpath))))
    return str(filtroConteudoRepo(projectpath))


class FiltroLinguagem:
    def filtroLinguagem(self):
        base_url = ('https://api.github.com/{}')
        path = 'users/viniyan'
        token = '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'
        headers = {'authorization': 'Bearer {}'.format(token)}
        response = requests.get(base_url.format(path), headers=headers)  # autenticar o github

        api_base_url = 'https://api.github.com'
        owner = 'viniyan'
        repo = 'YEarn'
        endpoint_path = f'/repos/{owner}/{repo}/languages'
        endpoint = f'{api_base_url}{endpoint_path}'
        r = requests.get(endpoint)
        print(r.text)
        return r.text

@app.route('/handle_language', methods=['POST'])
def handle_language():
    projectpath = request.form['language']
    x = FiltroLinguagem
    print(x.filtroLinguagem(x))
    return str(x.filtroLinguagem(projectpath))

class OrdenarAlfabeticamente:
    def ordenaAlfa(self):
        base_url = ('https://api.github.com/{}')
        path = 'users/viniyan'
        token = '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'
        headers = {'authorization': 'Bearer {}'.format(token)}
        response = requests.get(base_url.format(path), headers=headers)  # autenticar o github



        api_base_url = 'https://api.github.com/users/viniyan'
        endpoint_path = '/repos'
        endpoint = f'{api_base_url}{endpoint_path}'
        r = requests.get(endpoint, data={'sort': 'full_name', 'per_page': 100})

        x = r.text
        json_completo = json.loads(x)
        #pprint.pprint(json_completo)
        repo1 = json_completo[0]
        repo2 = json_completo[1]
        repo3 = json_completo[2]
        repo4 = json_completo[3]
        repo5 = json_completo[4]
        repo6 = json_completo[5]
        nome1 = repo1['name']
        nome2 = repo2['name']
        nome3 = repo3['name']
        nome4 = repo4['name']
        nome5 = repo5['name']
        nome6 = repo6['name']
        nomes = [nome1, nome2, nome3, nome4, nome5, nome6]
        ordenado = sorted(nomes, key= str.casefold)
        print(ordenado)
        return ordenado

@app.route('/handle_alfa', methods=['POST'])
def handle_alfa():
    projectpath = request.form['alfa']
    x = OrdenarAlfabeticamente
    return str(x.ordenaAlfa(projectpath))

class UltimoCommit:
    def achaData(self, repo):
        base_url = ('https://api.github.com/{}')
        path = 'users/viniyan'
        token = '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'
        headers = {'authorization': 'Bearer {}'.format(token)}
        response = requests.get(base_url.format(path), headers=headers)  # autenticar o github

        api_base_url = 'https://api.github.com'
        owner = 'viniyan'
        repo = repo

        endpoint_path = f'/repos/{owner}/{repo}/commits'
        endpoint = f'{api_base_url}{endpoint_path}'

        r = requests.get(endpoint)
        print(r.status_code)
        x = r.text
        json_completo = json.loads(x)
        json_dicts = json_completo[0]
        dict_values = json_dicts.values()
        for i in dict_values:
            if type(i) == dict:
                x = i.values()
                for k in x:
                    if type(k) == dict:
                        y = list(k.values())
                        data = y[2]
                        print(data)
                        return data

@app.route('/handle_last', methods=['POST'])
def handle_last():
    projectpath = request.form['last']
    x = UltimoCommit
    return str(x.achaData(x, projectpath))


class ControllerFiltro:
    def filtroNome(self, NOME):  # nome do repo
        api_base_url = 'https://api.github.com'
        nome = NOME
        endpoint_path = f'https://api.github.com/search/repositories?q=user:viniyan+{nome}%20in:name'
        endpoint = f'{endpoint_path}'
        r = requests.get(endpoint)
        x = json.loads(r.text)
        a = []

        y = x['items']
        for i in y:
            for z in i:
                k = i['full_name']
                a.append(k)

        return a

#x = ControllerFiltro
#x.filtroNome(x, 'De')

@app.route('/handle_name', methods=['POST'])
def handle_name():
    projectpath = request.form['name']
    x = ControllerFiltro
    return str(x.filtroNome(x, projectpath))








if __name__ == '__main__':
    app.run(debug=True)
