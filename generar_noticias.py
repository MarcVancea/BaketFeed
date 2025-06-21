import feedparser

# Feeds por categoría
feeds = {
    "nba": {
        "url": "https://www.espn.com/espn/rss/nba/news",
        "titulo": "Noticias NBA - BasketFeed",
        "archivo": "nba.html"
    },
    "acb": {
        "url": "https://e00-marca.uecdn.es/rss/baloncesto/acb.xml",
        "titulo": "Noticias ACB - BasketFeed",
        "archivo": "acb.html"
    },
    "euroliga": {
        "url": "https://e00-marca.uecdn.es/rss/baloncesto/euroliga.xml",
        "titulo": "Noticias Euroliga - BasketFeed",
        "archivo": "euroliga.html"
    }
}

# HTML base (título se sustituye dinámicamente)
plantilla_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo}</title>
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
  <style>
    body {{ margin: 0; font-family: 'Inter', sans-serif; background-color: #0f0f0f; color: #fff; line-height: 1.6; }}
    header {{ background-color: #181818; padding: 30px 20px 15px; text-align: center; border-bottom: 2px solid #fcb900; }}
    header img {{ height: 50px; margin-bottom: 10px; }}
    header p {{ font-size: 1.1rem; color: #bbb; }}
    nav {{ text-align:center; margin-top: 10px; }}
    nav a {{ color:#fcb900; margin: 0 15px; text-decoration:none; }}
    nav a:hover {{ text-decoration: underline; }}
    h2 {{ margin-top: 40px; font-size: 1.6rem; color: #fcb900; border-left: 5px solid #fcb900; padding-left: 10px; }}
    .news-container {{ max-width: 1000px; margin: 0 auto; padding: 20px; }}
    .news-item {{ background-color: #1d1d1d; padding: 20px; margin: 20px 0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); transition: transform 0.2s ease, box-shadow 0.2s ease; }}
    .news-item:hover {{ transform: translateY(-2px); box-shadow: 0 6px 16px rgba(0,0,0,0.4); }}
    .news-item h3 {{ margin: 0 0 10px; color: #fff; font-size: 1.3rem; }}
    .news-item p {{ color: #ddd; font-size: 1rem; }}
    .news-item a {{ color: #fcb900; text-decoration: none; }}
    .news-item a:hover {{ text-decoration: underline; }}
    footer {{ text-align: center; padding: 30px 20px; background-color: #181818; color: #888; font-size: 0.9rem; border-top: 1px solid #333; }}
    @media (max-width: 600px) {{
      header img {{ height: 40px; }}
      header p {{ font-size: 1rem; }}
      .news-item {{ padding: 16px; }}
      .news-item h3 {{ font-size: 1.1rem; }}
      .news-item p {{ font-size: 0.95rem; }}
    }}
  </style>
</head>
<body>
  <header>
    <img src="logo.svg" alt="BasketFeed Logo">
    <p>Últimas noticias de baloncesto - {seccion}</p>
  </header>
  <nav>
    <a href="index.html">Inicio</a>
    <a href="nba.html">NBA</a>
    <a href="acb.html">ACB</a>
    <a href="euroliga.html">Euroliga</a>
  </nav>
  <div class="news-container">
    <h2>Noticias de {seccion}</h2>
    {noticias}
  </div>
  <footer>
    &copy; 2025 BasketFeed. Proyecto automatizado por Marc.
  </footer>
</body>
</html>
"""

def obtener_noticias(feed_url, max_noticias=6):
    feed = feedparser.parse(feed_url)
    noticias = ""
    for entry in feed.entries[:max_noticias]:
        titulo = entry.title
        descripcion = entry.summary if hasattr(entry, "summary") else ""
        link = entry.link if hasattr(entry, "link") else "#"
        noticias += f'''
        <div class="news-item">
            <h3>{titulo}</h3>
            <p>{descripcion} <a href="{link}" target="_blank">Leer más</a></p>
        </div>'''
    return noticias

def generar_archivo(categoria, datos):
    noticias_html = obtener_noticias(datos["url"])
    html_final = plantilla_html.format(
        titulo=datos["titulo"],
        seccion=categoria.upper(),
        noticias=noticias_html
    )
    with open(datos["archivo"], "w", encoding="utf-8") as f:
        f.write(html_final)

def main():
    for categoria, datos in feeds.items():
        generar_archivo(categoria, datos)

if __name__ == "__main__":
    main()
