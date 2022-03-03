from Models import *
from Dao import *
from novovarejo import *
from github import Github
from flask import jsonify, Flask, render_template, send_file, make_response, url_for, Response, redirect, request
from datetime import datetime
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html', PageTitle='Landing Page')


access_token = "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"
g = Github(access_token)

def filtroData( dataInicio1, dataTermino1):     #criação do repo
    access_token = "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"
    g = Github(access_token)

    dataInicio1 = datetime.strptime(dataInicio1, '%d/%m/%Y').date()
    dataTermino1 = datetime.strptime(dataTermino1, '%d/%m/%Y').date()
    repos = [_ for _ in g.get_user().get_repos()]
    for repo in repos:
        x = repo.created_at
        y = datetime.date(x)
        if dataInicio1 < y and dataTermino1 > y:
            print(str(repo))
            return str(repo)
        elif dataInicio1 > y and dataTermino1 < y:
            print('Não há repositórios publicados neste período' )
            return 'Não há repositórios publicados neste período'

@app.route('/handle_data', methods=['POST'])
def handle_data():

    projectpath = request.form['date']
    data1 = projectpath[1:11]
    data2 = projectpath[15:25]
    return str(filtroData(data1, data2))


def filtroConteudoRepo(nomeRepo):       #arquivos do repo
    repo = g.get_user().get_repos()
    repos = g.get_repo('viniyan/'+nomeRepo)
    for i in repo:
        x = str(i)
        if nomeRepo in x:
            content = repos.get_contents('')
            for i in content:
                print(str(i))


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
        nome1 = repo1['name']
        nome2 = repo2['name']
        nome3 = repo3['name']
        nome4 = repo4['name']
        nome5 = repo5['name']
        nomes = [nome1, nome2, nome3, nome4, nome5]
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
    def filtroNome(self, nome):    #nome do repo
        repos = [_ for _ in g.get_user().get_repos(nome)]
        for repo in repos:
            x = str(repo)
            if nome in x:
                print(x.replace('Repository(full_name=', ''))
            else:
                print('Não há repositórios com esse nome')

@app.route('/handle_name', methods=['POST'])
def handle_name():
    projectpath = request.form['name']
    x = ControllerFiltro
    return str(x.filtroNome(x, projectpath))








if __name__ == '__main__':
    app.run(debug=True)
