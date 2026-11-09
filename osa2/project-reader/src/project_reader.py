from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content = tomllib.loads(content)
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content['project']['name'], content['project']['description'], 
                       content['project']['license'], content['project']['authors'], 
                       content['project']['dependencies'],content['dependency-groups']['dev'])