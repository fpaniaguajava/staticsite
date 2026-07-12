from pathlib import Path
import re

root = Path(__file__).resolve().parent
pattern = re.compile(r'https://upload\.wikimedia\.org/wikipedia/commons/thumb/([^/]+)/([^/]+)/([^/]+)/[^"\'\s<>]+')

files = [root / 'index.html', *sorted((root / 'pages').glob('*.html'))]
changed = []
for path in files:
    text = path.read_text(encoding='utf-8')
    new_text = pattern.sub(r'https://upload.wikimedia.org/wikipedia/commons/\1/\2/\3', text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        changed.append(path.relative_to(root).as_posix())

print('Updated files:')
for item in changed:
    print(item)
