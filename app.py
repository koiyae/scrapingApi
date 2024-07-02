from flask import Flask, jsonify
import csv

app = Flask(__name__)

def read_csv():
    with open('scraping.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

@app.route('/<author_slug>', methods=['GET'])
def get_author_passages(author_slug):
    passages = read_csv()
    passages_filtered = [passage['passage'] for passage in passages if passage['author'] == author_slug]

    if not passages_filtered:
        return jsonify({'message':'Autor não encontrado'}), 404

    response = {
        'author': author_slug,
        'passages': []
    }

    for passage_text in passages_filtered:
        response['passages'].append({'passage': passage_text})

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=False)