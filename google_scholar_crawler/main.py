from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time

# Setup proxy
pg = ProxyGenerator()
pg.FreeProxies()  # Use free rotating proxies
scholarly.use_proxy(pg)

paper1 = 'Fast Parameter-Free Multi-View Subspace Clustering With Consensus Anchor Guidance'
paper2 = 'Align then Fusion: Generalized Large-scale Multi-view Clustering with Anchor Matching Correspondences'
paper3 = 'Highly-efficient Incomplete Large-scale Multi-view Clustering with Consensus Bipartite Graph'
paper4 = 'Multi-view Clustering via Late Fusion Alignment Maximization'

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
##print(json.dumps(author, indent=2))

os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}

with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print(json.dumps(author['citedby'], indent=2))
