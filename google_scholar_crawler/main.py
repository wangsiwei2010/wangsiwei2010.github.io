from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

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

search_query1 = scholarly.search_pubs(paper1)
data1 = next(search_query1)
print(json.dumps(data1, indent=2))

with open(f'results/gs_data_paper1.json', 'w') as outfile:
    json.dump(data1, outfile, ensure_ascii=False)

shieldio_data_paper1 = {
  "schemaVersion": 1,
  "label": "num_citations",
  "message": f"{data1['num_citations']}",
}

with open(f'results/gs_data_shieldsio_paper1.json', 'w') as outfile:
    json.dump(shieldio_data_paper1, outfile, ensure_ascii=False)


search_query2 = scholarly.search_pubs(paper2)
data2 = next(search_query2)
print(json.dumps(data2, indent=2))

with open(f'results/gs_data_paper2.json', 'w') as outfile:
    json.dump(data2, outfile, ensure_ascii=False)

shieldio_data_paper2 = {
  "schemaVersion": 1,
  "label": "num_citations",
  "message": f"{data2['num_citations']}",
}

with open(f'results/gs_data_shieldsio_paper2.json', 'w') as outfile:
    json.dump(shieldio_data_paper2, outfile, ensure_ascii=False)

search_query3 = scholarly.search_pubs(paper3)
data3 = next(search_query3)
print(json.dumps(data3, indent=2))

with open(f'results/gs_data_paper3.json', 'w') as outfile:
    json.dump(data3, outfile, ensure_ascii=False)

shieldio_data_paper3 = {
  "schemaVersion": 1,
  "label": "num_citations",
  "message": f"{data3['num_citations']}",
}

with open(f'results/gs_data_shieldsio_paper3.json', 'w') as outfile:
    json.dump(shieldio_data_paper3, outfile, ensure_ascii=False)    

search_query4 = scholarly.search_pubs(paper4)
data4 = next(search_query4)
print(json.dumps(data4, indent=2))

with open(f'results/gs_data_paper4.json', 'w') as outfile:
    json.dump(data4, outfile, ensure_ascii=False)

shieldio_data_paper4 = {
  "schemaVersion": 1,
  "label": "num_citations",
  "message": f"{data4['num_citations']}",
}

with open(f'results/gs_data_shieldsio_paper4.json', 'w') as outfile:
    json.dump(shieldio_data_paper4, outfile, ensure_ascii=False)    
