import yaml
from jinja2 import Template
from markdown import markdown

# Načti data z YAML
with open("content.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Markdown → HTML pro každou sekci
position = 'right'
for section in data["sections"]:
    section["content_html"] = markdown(section["content"])
    section["image_position"] = position
    position = 'right' if position == 'left' else 'left'

# Načti šablonu
with open("template.html", encoding="utf-8") as f:
    template = Template(f.read())

# Vygeneruj výstup
html = template.render(**data)

# Ulož výsledek
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Soubor index.html byl úspěšně vygenerován.")
