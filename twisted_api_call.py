from twisted.internet import reactor, ssl, _sslverify
from twisted.web.client import Agent, readBody
from twisted.web.iweb import IPolicyForHTTPS
from zope.interface import implementer
from utility import URLS
from twisted.internet.defer import gatherResults
import json
import time

def onError(ignored):
    print(ignored)


def onResponse(response):
    deferred = readBody(response)
    deferred.addCallback(printBody)
    return deferred


def printBody(body):
    parsed_body = json.loads(body)
    for m in parsed_body:
        try:
            print(m['match_date'] + ': ' + m['match_hometeam_name'] + ':' + m['match_awayteam_name'] + ' ----> ' +  m['match_hometeam_score'] + ':' + m['match_awayteam_score'])
        except TypeError:
            pass


@implementer(IPolicyForHTTPS)
class IgnoreHTTPS:
    def creatorForNetloc(self, hostname, port):
        options = ssl.CertificateOptions(verify=False)
        return _sslverify.ClientTLSOptions(hostname.decode('ascii'), options.getContext())


agent = Agent(reactor, IgnoreHTTPS())
closed_deferreds = []
start_time = time.time()
for url in URLS:
    d = agent.request(
        b'GET',
        url.encode()
    )

    d.addCallback(onResponse)
    d.addErrback(onError)

    closed_deferreds.append(d)

gatherResults(closed_deferreds).addCallback(lambda ignored: reactor.stop())
reactor.run()
end_time = time.time()

print(end_time - start_time)