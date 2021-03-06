import os
import time
import json
import subprocess
import meilisearch
import xxhash
from pathlib import Path
from datetime import datetime

DELAY = int(os.getenv('DELAY'))
input_path = Path('/inputs')
client = meilisearch.Client('http://search:7700')
index = client.get_or_create_index('screenshots')

while True:
    print(f'\n\n****** Checking for changes: {datetime.now()} ******')
    inputs = set(i.name for i in input_path.iterdir() if not i.is_dir())
    n_docs = index.get_stats()['numberOfDocuments']
    outputs = set(x['name'] for x in index.get_documents({'limit': n_docs, 'attributesToRetrieve': 'name'}))

    deleted_files = outputs - inputs
    print(f'No of docs to be deleted from db = {len(deleted_files)}'.upper())
    index.delete_documents([xxhash.xxh3_64_hexdigest(x) for x in deleted_files])

    added_files = inputs - outputs
    print(f'No of docs to be added to db = {len(added_files)}'.upper())
    docs = []
    for idx, file in enumerate(added_files, start=1):
        loc = str(input_path / file)
        result = subprocess.run([
            'tesseract', loc, 'stdout', 'quiet',
            '-l', 'eng', '--psm', '1', '--oem', '3', 'txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        doc = {
            'id': xxhash.xxh3_64_hexdigest(file),
            'name': file,
            'ocr': result.stdout.decode('utf-8')
        }
        docs.append(doc)
        if idx % 50 == 0:
            index.add_documents(docs)
            print(f'New documents added : {docs[0]["id"]} ... {docs[-1]["id"]}')
            docs = []

    if len(added_files) > 0:
        index.add_documents(docs)
        print(r'Finished adding final set of documents to search database \m/(>.<)\m/')
    time.sleep(DELAY * 60)
