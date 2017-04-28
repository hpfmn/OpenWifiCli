import requests
import json


class openwifi:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        r = requests.get(self.baseUrl+'/nodes')
        self.nodes = json.loads(r.text)

    def getNodes(self):
        return self.nodes

    def getNodeURL(self):
        return self.baseUrl+'/nodes'

    def exec(self, UUIDs, command):
        if type(UUIDs) != list:
            UUIDs = [UUIDs]

        ret = []

        for UUID in UUIDs:
            r = requests.post(self.getNodeURL()+'/'+UUID+'/exec',
                              data=json.dumps(command))
            ret.append(r.text)

        return ret

    def commandFromString(self, cmd):
        cmdList = cmd.split(' ')
        return {'command' : cmdList[0],
                'params'  : cmdList[1:]}

