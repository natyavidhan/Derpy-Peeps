from flask import Flask, send_file, request, render_template
from io import StringIO, BytesIO
import random
import json

def serve_content(content):
    svg_io = StringIO()
    svg_io.write(content)
    svg_io.seek(0)
    mem = BytesIO()
    mem.write(svg_io.getvalue().encode('utf-8'))
    mem.seek(0)
    return send_file(mem, mimetype='image/svg+xml')

app = Flask(__name__)

svgs = json.load(open('assets.json'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image')
def image():
    seed = "derp" if 'seed' not in request.args else request.args.get('seed')
    random.seed(seed)
    hair = random.choice(svgs['hairs'])
    mouth = random.choice(svgs['mouths'])
    skin = random.choice(svgs['skins'])
    spec = random.choice(svgs['specs'])
    color = random.choice(svgs['colors'])
    svg = f"""<svg width="256" height="256" viewBox="0 0 256 256" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="256" height="256" fill="{color}"/>
{skin}
{hair}
{mouth}
{spec}
</svg>"""
    return serve_content(svg)

if __name__ == "__main__":
    app.run(debug=True)