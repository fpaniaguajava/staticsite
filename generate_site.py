from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"
ASSETS_DIR = ROOT / "assets"
IMAGES_DIR = ASSETS_DIR / "images"

IMAGE_URLS = {
    "sega-master-system": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Sega_Master_System_II.jpg",
    "sega-genesis": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Sega_Genesis_Console.jpg",
    "sega-cd": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Sega-CD-Model1-Set.jpg",
    "sega-saturn": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Sega-Saturn-Console-Set-Mk1.jpg",
    "sega-dreamcast": "https://upload.wikimedia.org/wikipedia/commons/7/78/Sega_Dreamcast_Console.jpg",
    "nes": "https://upload.wikimedia.org/wikipedia/commons/0/0d/NES-Console-Set.jpg",
    "snes": "https://upload.wikimedia.org/wikipedia/commons/3/3e/SNES-Console-Set.jpg",
    "nintendo-64": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Nintendo_64_Console.jpg",
    "gamecube": "https://upload.wikimedia.org/wikipedia/commons/8/81/GameCube-Set.jpg",
    "wii": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Wii-console.jpg",
    "wii-u": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Wii_U_Console_and_GamePad.jpg",
    "switch": "https://upload.wikimedia.org/wikipedia/commons/8/88/Nintendo-Switch-Console-Docked-wJoyConRB.jpg",
    "xbox": "https://upload.wikimedia.org/wikipedia/commons/2/20/Original_Xbox_console.jpg",
    "xbox-360": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Xbox_360.jpg",
    "xbox-one": "https://upload.wikimedia.org/wikipedia/commons/8/81/Xbox_One_Console_Set.jpg",
    "xbox-series": "https://upload.wikimedia.org/wikipedia/commons/8/85/Xbox_Series_X_and_S.jpg",
    "playstation": "https://upload.wikimedia.org/wikipedia/commons/4/4e/PSX-Console-wController.jpg",
    "playstation-2": "https://upload.wikimedia.org/wikipedia/commons/5/5d/PlayStation_2.png",
    "playstation-3": "https://upload.wikimedia.org/wikipedia/commons/8/8d/PlayStation_3.png",
    "playstation-4": "https://upload.wikimedia.org/wikipedia/commons/4/4b/PS4-Console-wDS4.jpg",
    "playstation-5": "https://upload.wikimedia.org/wikipedia/commons/7/76/PlayStation_5_and_DualSense.jpg",
}

CONSOLES = [
    {
        "name": "Sega Master System",
        "slug": "sega-master-system",
        "brand": "Sega",
        "year": "1985",
        "summary": "La primera consola doméstica de Sega que llevó el sistema de 8 bits a un público masivo en Europa y América.",
        "highlights": ["Procesador 8 bits", "Gran catálogo de juegos arcade", "Iconos como Alex Kidd y Sonic"],
        "games": ["Alex Kidd in Miracle World", "Phantasy Star", "Castle of Illusion"],
        "accent": "#ff5f7d",
        "secondary": "#6a3eea"
    },
    {
        "name": "Sega Genesis",
        "slug": "sega-genesis",
        "brand": "Sega",
        "year": "1989",
        "summary": "La consola de 16 bits que consolidó a Sega como rival de Nintendo con un catálogo de acción y arcade inolvidable.",
        "highlights": ["16 bits", "Sonic the Hedgehog", "Consola de culto"],
        "games": ["Sonic the Hedgehog", "Streets of Rage", "Mortal Kombat"],
        "accent": "#ff8b3d",
        "secondary": "#4f4da3"
    },
    {
        "name": "Sega CD",
        "slug": "sega-cd",
        "brand": "Sega",
        "year": "1992",
        "summary": "Una unidad de expansión que añadió sonido CD y secuencias cinematográficas a los juegos de Genesis.",
        "highlights": ["CD-ROM", "FMV", "Experiencia más cinematográfica"],
        "games": ["Sonic CD", "Lunar: Silver Star Story", "Snatcher"],
        "accent": "#24c4ff",
        "secondary": "#ce3dff"
    },
    {
        "name": "Sega Saturn",
        "slug": "sega-saturn",
        "brand": "Sega",
        "year": "1995",
        "summary": "La consola de 32 bits que brilló con títulos innovadores, aunque llegó en un momento complejo para Sega.",
        "highlights": ["32 bits", "Controladores duales", "Gran catálogo japonés"],
        "games": ["Nights into Dreams", "Panzer Dragoon Saga", "Virtua Fighter"],
        "accent": "#ff4d6d",
        "secondary": "#1c7fb6"
    },
    {
        "name": "Sega Dreamcast",
        "slug": "sega-dreamcast",
        "brand": "Sega",
        "year": "1998",
        "summary": "La última gran consola de Sega y una máquina adelantada a su tiempo con red online y gráficos de vanguardia.",
        "highlights": ["Internet en consola", "Gráficos 3D punteros", "Biblioteca muy querida"],
        "games": ["Crazy Taxi", "Soulcalibur", "Jet Set Radio"],
        "accent": "#ff6b6b",
        "secondary": "#2dd4bf"
    },
    {
        "name": "Nintendo Entertainment System",
        "slug": "nes",
        "brand": "Nintendo",
        "year": "1983",
        "summary": "La consola que popularizó el videojuego en casa y definió el modelo de éxito de Nintendo en los años 80.",
        "highlights": ["8 bits", "Cartuchos icónicos", "Super Mario Bros."],
        "games": ["Super Mario Bros.", "The Legend of Zelda", "Metroid"],
        "accent": "#ef4444",
        "secondary": "#fbbf24"
    },
    {
        "name": "Super Nintendo Entertainment System",
        "slug": "snes",
        "brand": "Nintendo",
        "year": "1990",
        "summary": "La gran consola de 16 bits de Nintendo, con un catálogo de juegos que sigue siendo referencia absoluta.",
        "highlights": ["16 bits", "Mode 7", "Mario Kart"],
        "games": ["Super Mario World", "Donkey Kong Country", "Super Metroid"],
        "accent": "#f97316",
        "secondary": "#3b82f6"
    },
    {
        "name": "Nintendo 64",
        "slug": "nintendo-64",
        "brand": "Nintendo",
        "year": "1996",
        "summary": "La consola de 64 bits que trajo el salto a 3D y redefinió la experiencia de los juegos de acción.",
        "highlights": ["64 bits", "Control analógico", "Mario 64"],
        "games": ["Super Mario 64", "The Legend of Zelda: Ocarina of Time", "GoldenEye 007"],
        "accent": "#8b5cf6",
        "secondary": "#22c55e"
    },
    {
        "name": "Nintendo GameCube",
        "slug": "gamecube",
        "brand": "Nintendo",
        "year": "2001",
        "summary": "Una consola compacta y poderosa con un catálogo creativo y muy querido por la comunidad.",
        "highlights": ["Discos miniDVD", "Diseño compacto", "Mario Sunshine"],
        "games": ["Luigi's Mansion", "Super Smash Bros. Melee", "Mario Kart: Double Dash!!"],
        "accent": "#22c55e",
        "secondary": "#ef4444"
    },
    {
        "name": "Nintendo Wii",
        "slug": "wii",
        "brand": "Nintendo",
        "year": "2006",
        "summary": "La consola que hizo que los videojuegos fueran accesibles para todos gracias a su mando de movimiento.",
        "highlights": ["Wiimote", "Accesibilidad", "Wii Sports"],
        "games": ["Wii Sports", "Mario Kart Wii", "The Legend of Zelda: Twilight Princess"],
        "accent": "#38bdf8",
        "secondary": "#facc15"
    },
    {
        "name": "Nintendo Wii U",
        "slug": "wii-u",
        "brand": "Nintendo",
        "year": "2012",
        "summary": "Una propuesta innovadora con pantalla táctil en el mando, aunque con una vida comercial corta.",
        "highlights": ["GamePad", "Multiplataforma", "Nintendo Land"],
        "games": ["Mario Kart 8", "Super Mario 3D World", "Nintendo Land"],
        "accent": "#fb923c",
        "secondary": "#6366f1"
    },
    {
        "name": "Nintendo Switch",
        "slug": "switch",
        "brand": "Nintendo",
        "year": "2017",
        "summary": "La consola híbrida que fusiona sobremesa y portátil con una de las bibliotecas más fuertes de la historia.",
        "highlights": ["Modo portátil", "Nintendo Switch Online", "Mario, Zelda y Pokémon"],
        "games": ["The Legend of Zelda: Breath of the Wild", "Mario Kart 8 Deluxe", "Animal Crossing: New Horizons"],
        "accent": "#f43f5e",
        "secondary": "#1d4ed8"
    },
    {
        "name": "Xbox",
        "slug": "xbox",
        "brand": "Xbox",
        "year": "2001",
        "summary": "La primera consola de Microsoft, diseñada para competir con PlayStation y Nintendo con un enfoque centrado en el online.",
        "highlights": ["Xbox Live", "Hardware potente", "Halo"],
        "games": ["Halo: Combat Evolved", "Project Gotham Racing", "Fable"],
        "accent": "#22c55e",
        "secondary": "#0f172a"
    },
    {
        "name": "Xbox 360",
        "slug": "xbox-360",
        "brand": "Xbox",
        "year": "2005",
        "summary": "Una máquina de gran éxito que consolidó el servicio online de Microsoft y el catálogo de exclusivas.",
        "highlights": ["Xbox Live Arcade", "Gears of War", "Gran biblioteca de juegos"],
        "games": ["Halo 3", "Gears of War", "Forza Horizon"],
        "accent": "#14b8a6",
        "secondary": "#2563eb"
    },
    {
        "name": "Xbox One",
        "slug": "xbox-one",
        "brand": "Xbox",
        "year": "2013",
        "summary": "La consola de la generación siguiente, impulsada por el servicio de suscripción y las experiencias multimedia.",
        "highlights": ["Multimedia", "Xbox One X", "Game Pass"],
        "games": ["Halo 5", "Forza Horizon 2", "Sunset Overdrive"],
        "accent": "#3b82f6",
        "secondary": "#1e293b"
    },
    {
        "name": "Xbox Series X|S",
        "slug": "xbox-series",
        "brand": "Xbox",
        "year": "2020",
        "summary": "La familia de consolas actuales de Microsoft, orientada a rendimiento, velocidad y acceso inmediato.",
        "highlights": ["SSD veloz", "Ray tracing", "Game Pass"],
        "games": ["Halo Infinite", "Forza Horizon 5", "Starfield"],
        "accent": "#0ea5e9",
        "secondary": "#0f172a"
    },
    {
        "name": "PlayStation",
        "slug": "playstation",
        "brand": "PlayStation",
        "year": "1994",
        "summary": "La consola original de Sony que cambió para siempre el panorama del videojuego con un catálogo memorable.",
        "highlights": ["CD-ROM", "Final Fantasy VII", "Gran catálogo 3D"],
        "games": ["Final Fantasy VII", "Metal Gear Solid", "Gran Turismo"],
        "accent": "#2563eb",
        "secondary": "#f59e0b"
    },
    {
        "name": "PlayStation 2",
        "slug": "playstation-2",
        "brand": "PlayStation",
        "year": "2000",
        "summary": "La consola más vendida de la historia, con una biblioteca gigantesca y un impacto cultural enorme.",
        "highlights": ["Consola más vendida", "DVD", "Grandes exclusivas"],
        "games": ["Shadow of the Colossus", "God of War", "Gran Turismo 3"],
        "accent": "#6366f1",
        "secondary": "#f43f5e"
    },
    {
        "name": "PlayStation 3",
        "slug": "playstation-3",
        "brand": "PlayStation",
        "year": "2006",
        "summary": "La consola de Sony con Blu-ray, online y un salto en potencia que dio lugar a grandes experiencias.",
        "highlights": ["Blu-ray", "PSN", "The Last of Us"],
        "games": ["Uncharted 2", "The Last of Us", "Metal Gear Solid 4"],
        "accent": "#0f766e",
        "secondary": "#f59e0b"
    },
    {
        "name": "PlayStation 4",
        "slug": "playstation-4",
        "brand": "PlayStation",
        "year": "2013",
        "summary": "La generación que consolidó el ecosistema de PlayStation con títulos de alta calidad y gran alcance.",
        "highlights": ["Juegos AAA", "Realismo", "PS Plus"],
        "games": ["God of War", "Horizon Zero Dawn", "The Last of Us Part II"],
        "accent": "#1d4ed8",
        "secondary": "#a855f7"
    },
    {
        "name": "PlayStation 5",
        "slug": "playstation-5",
        "brand": "PlayStation",
        "year": "2020",
        "summary": "La consola actual de Sony, enfocada en el rendimiento, tiempos de carga mínimos y experiencias inmersivas.",
        "highlights": ["SSD ultrarrápido", "DualSense", "Ray tracing"],
        "games": ["Marvel's Spider-Man 2", "Ratchet & Clank: Rift Apart", "Astro's Playroom"],
        "accent": "#3b82f6",
        "secondary": "#22c55e"
    }
]


def build_svg(console):
    accent = console["accent"]
    secondary = console["secondary"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360">
  <rect width="640" height="360" rx="32" fill="#0f172a"/>
  <rect x="30" y="30" width="580" height="300" rx="24" fill="#111827" stroke="#fef3c7" stroke-width="6"/>
  <rect x="90" y="90" width="460" height="180" rx="24" fill="{accent}"/>
  <rect x="120" y="120" width="400" height="120" rx="18" fill="{secondary}"/>
  <rect x="150" y="150" width="340" height="50" rx="10" fill="#ffffff" opacity="0.95"/>
  <text x="320" y="182" text-anchor="middle" font-family="Arial, sans-serif" font-size="26" font-weight="700" fill="#0f172a">{escape(console['name'])}</text>
  <circle cx="520" cy="90" r="22" fill="#fef3c7"/>
  <text x="520" y="98" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="700" fill="#0f172a">{escape(console['brand'][0])}</text>
  <text x="320" y="315" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#fef3c7">Retro Console Vault</text>
</svg>'''


for console in CONSOLES:
    console["image_url"] = IMAGE_URLS.get(console["slug"], "")


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_index():
    cards = []
    for console in CONSOLES:
        cards.append(f'''
        <article class="console-card">
          <img src="{console['image_url']}" alt="{escape(console['name'])}" loading="lazy">
          <div class="card-body">
            <p class="brand-pill">{escape(console['brand'])}</p>
            <h3>{escape(console['name'])}</h3>
            <p>{escape(console['summary'])}</p>
            <a href="pages/{console['slug']}.html" class="button">Ver consola</a>
          </div>
        </article>''')

    grouped = {}
    for console in CONSOLES:
        grouped.setdefault(console["brand"], []).append(console)

    sections = []
    for brand in ["Sega", "Nintendo", "Xbox", "PlayStation"]:
        items = grouped[brand]
        section_cards = "".join(
            f'<a class="mini-link" href="pages/{console["slug"]}.html">{escape(console["name"])}</a>' for console in items
        )
        sections.append(f'''<section class="brand-block">
            <h2>{brand}</h2>
            <div class="mini-links">{section_cards}</div>
          </section>''')

    content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Retro Console Vault</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <div class="page-shell">
    <header class="hero">
      <p class="eyebrow">Colección retro</p>
      <h1>Retro Console Vault</h1>
      <p>Una guía visual de las consolas más emblemáticas de Sega, Nintendo, Xbox y PlayStation.</p>
    </header>

    <main>
      <section class="intro-panel">
        <p>Explora cada sistema, descubre su fecha de lanzamiento y revisa algunos de los juegos que la hicieron inolvidable.</p>
        <div class="stats">
          <div><strong>20</strong><span>consolas</span></div>
          <div><strong>4</strong><span>marcas</span></div>
          <div><strong>100%</strong><span>estilo retro</span></div>
        </div>
      </section>

      <section class="console-grid">
        {"".join(cards)}
      </section>

      <section class="brand-list">
        {"".join(sections)}
      </section>
    </main>
  </div>
</body>
</html>'''
    write_file(ROOT / "index.html", content)


def render_console_page(console):
    highlights = "".join(f"<li>{escape(item)}</li>" for item in console["highlights"])
    games = "".join(f"<li>{escape(item)}</li>" for item in console["games"])
    content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(console['name'])} | Retro Console Vault</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <div class="page-shell">
    <a class="back-link" href="../index.html">← Volver al inicio</a>
    <article class="console-page">
      <header class="page-header">
        <p class="eyebrow">{escape(console['brand'])}</p>
        <h1>{escape(console['name'])}</h1>
        <p class="page-intro">{escape(console['summary'])}</p>
      </header>
      <img src="{console['image_url']}" alt="{escape(console['name'])}" loading="lazy">
      <div class="info-grid">
        <section>
          <h2>Datos clave</h2>
          <ul>
            <li><strong>Año:</strong> {escape(console['year'])}</li>
            <li><strong>Marca:</strong> {escape(console['brand'])}</li>
            <li><strong>Estilo:</strong> Retro clásico</li>
          </ul>
        </section>
        <section>
          <h2>Características</h2>
          <ul>{highlights}</ul>
        </section>
        <section>
          <h2>Juegos destacados</h2>
          <ul>{games}</ul>
        </section>
      </div>
    </article>
  </div>
</body>
</html>'''
    write_file(PAGES_DIR / f"{console['slug']}.html", content)


if __name__ == "__main__":
    for path in [ROOT, PAGES_DIR, ASSETS_DIR, IMAGES_DIR]:
        path.mkdir(parents=True, exist_ok=True)

    for console in CONSOLES:
        write_file(IMAGES_DIR / f"{console['slug']}.svg", build_svg(console))

    render_index()
    for console in CONSOLES:
        render_console_page(console)

    print("Site generated successfully.")
