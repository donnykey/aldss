
from flask import Flask, render_template, request
from utils.baidu_map import search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_view():
    city = request.args.get('city')
    region = request.args.get('region')
    keyword = request.args.get('keyword')
    results = search(city, region, keyword)
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

app.debug = True
