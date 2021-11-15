from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        palautus = toml.loads(content)

        dependencies = palautus["tool"]["poetry"]["dependencies"].keys()
        devDependencies = palautus["tool"]["poetry"]["dev-dependencies"].keys()

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(palautus["tool"]["poetry"]["name"], palautus["tool"]["poetry"]["description"],
         dependencies, devDependencies)
