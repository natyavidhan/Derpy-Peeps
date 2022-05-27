import os, json

hairs = []
mouth = []
skins = []
specs = []

for file in os.listdir('assets'):
    content = open(os.path.join('assets', file)).readlines()
    content.pop(0)
    content.pop(-1)
    content.pop(-1)
    content = "\n".join(x for x in content)
    if file.startswith('Hair'):
        hairs.append(content)
    elif file.startswith('Mouth'):
        mouth.append(content)
    elif file.startswith('Skin'):
        skins.append(content)
    elif file.startswith('Specs'):
        specs.append(content)

with open('assets.json', 'w') as f:
    json.dump({
        'hairs': hairs,
        'mouths': mouth,
        'skins': skins,
        'specs': specs
    }, f)