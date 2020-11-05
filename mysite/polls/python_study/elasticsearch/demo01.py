from datetime import datetime
from elasticsearch import Elasticsearch

'''
使用elasticsearch检索自定义的dict

'''

es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="polls_test-index", id=1, body=doc)
print(res['result'])

res = es.get(index="polls_test-index", id=1)
print(res['_source'])

es.indices.refresh(index="polls_test-index")

res = es.search(index="polls_test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

res = es.search(index="polls_test-index", body={"query": {"match_all": {}}},
                filter_path=['hits.hits._source'])

'''
res的结构如下:通过filter_path过滤到了hits下所有的_source。
{'hits': {'hits': [{'_source': {'author': 'kimchy', 'text': 'Elasticsearch: cool. bonsai cool.', 'timestamp': '2020-10-09T11:44:47.622542'}}]}}
'''

for hit in res['hits']['hits']:
    print("(author)%s" % hit["_source"]["author"])
