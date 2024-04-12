from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

paper1 = 'Fast Parameter-Free Multi-View Subspace Clustering With Consensus Anchor Guidance'

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))

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

with open(f'results/gs_data_paper1.json', 'w') as outfile:
    json.dump(data1, outfile, ensure_ascii=False)

shieldio_data_paper1 = {
  "schemaVersion": 1,
  "label": "num_citations",
  "message": f"{data1['num_citations']}",
}

with open(f'results/gs_data_shieldsio_paper1.json', 'w') as outfile:
    json.dump(shieldio_data_paper1, outfile, ensure_ascii=False)

