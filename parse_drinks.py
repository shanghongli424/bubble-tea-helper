import zipfile, xml.etree.ElementTree as ET, json, io, re

xlsx_path = "/Users/aaa/.openclaw/workspace/drink_menu.xlsx"

CONTAINERS = ['冷饮杯','热饮杯','雪克杯','量杯','出品杯','出品冷杯','出品热杯','冰沙机','奶缸','冷杯','热杯','咖啡机']
ICON_MAP = {'椰青系列':'🥥','爱乐冰系列':'🧊','气泡水系列':'🫧','手打柠檬茶系列':'🍋','轻乳茶系列':'🍵','奶茶系列':'🧋','咖啡系列':'☕','无咖啡因拿铁系列':'🥛'}

def parse_steps_from_cell(text):
    """Parse all steps from a single cell that contains numbered steps."""
    if not text or not text.strip(): return []
    text = text.strip()

    # Extract container from 【...】 prefix
    container = None
    m = re.match(r'^【([^】]+)】', text)
    if m:
        raw = m.group(1).strip()
        if '：' in raw: raw = raw.split('：',1)[-1].strip()
        for c in CONTAINERS:
            if c in raw: container = c; break
        if not container and len(raw) <= 6: container = raw
        text = text[m.end():].strip()

    # Split by numbered steps: 1. 2. 3. ...
    parts = re.split(r'(?<=[。；])\s*(?=[1-9][\.、])', text)
    steps = []
    for p in parts:
        p = re.sub(r'^[1-9][\.、]\s*', '', p.strip()).strip()
        if not p: continue

        # Detect which container this step uses (first container in text)
        found = None
        for c in CONTAINERS:
            if c in p[:12]: found = c; break
        title = found if found else (container or '制作')
        desc = p
        for c in CONTAINERS:
            if desc.startswith(c):
                desc = desc[len(c):].strip()
                break
        if desc:
            steps.append({'title': title, 'desc': desc})
    return steps

# Open xlsx and read shared strings
z = zipfile.ZipFile(xlsx_path)
ss = {}
ss_root = ET.parse(io.BytesIO(z.read('xl/sharedStrings.xml'))).getroot()
ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
for i, si in enumerate(ss_root.findall('{%s}si' % ns)):
    t = si.find('{%s}t' % ns)
    ss[i] = t.text if t is not None else ''

data = z.read('xl/worksheets/sheet1.xml')
root = ET.parse(io.BytesIO(data)).getroot()
rows = root.findall('.//{%s}row' % ns)

drinks = []
for row in rows[1:]:
    cells = {}
    for c in row.findall('{%s}c' % ns):
        col = ''.join(filter(str.isalpha, c.get('r')))
        t = c.get('t','')
        v = c.find('{%s}v' % ns)
        if v is not None and v.text:
            cells[col] = ss.get(int(v.text), v.text) if t == 's' else v.text

    name = cells.get('B', '').strip()
    cat  = cells.get('A', '').strip()
    temp = cells.get('C', '').strip()
    if not name: continue

    step_text = cells.get('D', '').strip()
    steps = parse_steps_from_cell(step_text)

    if steps:
        key = 'cold' if '冷' in temp else ('hot' if '热' in temp else 'cold')
        drink_id = f"{name.lower().replace(' ','').replace('×','')}-{key}"
        drinks.append({
            'id': drink_id,
            'name': name,
            'category': cat,
            'intro': temp,
            'icon': ICON_MAP.get(cat, '🧋'),
            'steps': steps
        })
        print(f"\n=== {cat} | {name} | {temp} ===")
        for i, s in enumerate(steps):
            print(f"  {i+1}. [{s['title']}] {s['desc'][:60]}")

print(f"\n\nTotal: {len(drinks)} drinks")
with open('/Users/aaa/.openclaw/workspace/drinks_final.json', 'w', encoding='utf-8') as f:
    json.dump(drinks, f, ensure_ascii=False, indent=2)