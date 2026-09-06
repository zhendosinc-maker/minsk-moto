import json

with open('/tmp/minsk_full_site_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

html_template = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Мотоциклы MINSK | Официальный полный каталог и история</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary-red: #e61b24;
      --dark-red: #b00d14;
      --bg-main: #0c0d0e;
      --bg-card: #151719;
      --bg-card-hover: #1c1f22;
      --border: rgba(255, 255, 255, 0.08);
      --border-focus: rgba(230, 27, 36, 0.5);
      --text-main: #f0f2f5;
      --text-muted: #959da5;
      --accent-glow: rgba(230, 27, 36, 0.25);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-main);
      color: var(--text-main);
      font-family: 'Montserrat', sans-serif;
      line-height: 1.6;
      overflow-x: hidden;
    }

    h1, h2, h3, h4, .brand, .badge, .btn, .spec-value, .filter-btn, .modal-title {
      font-family: 'Oswald', sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }

    .mono { font-family: 'JetBrains Mono', monospace; }

    .container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Header */
    header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(12, 13, 14, 0.9);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
    }

    .nav-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 76px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 1.8rem;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
    }

    .brand span { color: var(--primary-red); }

    .nav-links {
      display: flex;
      gap: 24px;
      list-style: none;
    }

    .nav-links a {
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 500;
      font-size: 0.95rem;
      transition: color 0.2s;
    }

    .nav-links a:hover { color: #fff; }

    /* Hero */
    .hero {
      position: relative;
      padding: 90px 0 60px;
      text-align: center;
      background: radial-gradient(circle at 50% 20%, rgba(230, 27, 36, 0.18) 0%, transparent 70%);
    }

    .hero-tag {
      display: inline-block;
      padding: 6px 16px;
      background: rgba(230, 27, 36, 0.12);
      border: 1px solid rgba(230, 27, 36, 0.3);
      color: var(--primary-red);
      font-size: 0.85rem;
      font-weight: 600;
      border-radius: 4px;
      margin-bottom: 20px;
      letter-spacing: 0.1em;
    }

    .hero h1 {
      font-size: 3.8rem;
      line-height: 1.1;
      font-weight: 700;
      margin-bottom: 20px;
      background: linear-gradient(180deg, #ffffff 60%, #959da5 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    @media (max-width: 768px) { .hero h1 { font-size: 2.3rem; } }

    .hero p {
      font-size: 1.2rem;
      color: var(--text-muted);
      max-width: 760px;
      margin: 0 auto 32px;
      font-weight: 300;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--primary-red);
      color: #fff;
      padding: 14px 32px;
      border-radius: 4px;
      text-decoration: none;
      font-size: 1.05rem;
      font-weight: 600;
      transition: all 0.25s;
      box-shadow: 0 4px 20px rgba(230, 27, 36, 0.4);
      cursor: pointer;
      border: none;
    }

    .btn:hover {
      background: var(--dark-red);
      transform: translateY(-2px);
      box-shadow: 0 8px 30px rgba(230, 27, 36, 0.6);
    }

    .btn-secondary {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border);
      box-shadow: none;
      color: #fff;
      margin-left: 12px;
    }

    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.3);
      box-shadow: none;
    }

    /* Key Numbers Strip */
    .history-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
      margin: 30px 0 60px;
      padding: 28px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
    }

    .history-item { text-align: center; }
    .history-num {
      font-size: 2.6rem;
      font-weight: 700;
      color: var(--primary-red);
      line-height: 1;
      margin-bottom: 6px;
    }
    .history-label {
      font-size: 0.85rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Filter Bar */
    .filter-bar {
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 40px;
    }

    .filter-btn {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 10px 20px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.95rem;
      transition: all 0.2s;
    }

    .filter-btn:hover {
      color: #fff;
      border-color: rgba(255, 255, 255, 0.2);
    }

    .filter-btn.active {
      background: var(--primary-red);
      color: #fff;
      border-color: var(--primary-red);
      box-shadow: 0 4px 16px rgba(230, 27, 36, 0.3);
    }

    /* Catalog Cards */
    .catalog-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 32px;
      margin-bottom: 80px;
    }

    @media (max-width: 480px) { .catalog-grid { grid-template-columns: 1fr; } }

    .moto-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }

    .moto-card:hover {
      transform: translateY(-6px);
      border-color: rgba(230, 27, 36, 0.5);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6), 0 0 30px var(--accent-glow);
    }

    .card-img-wrap {
      position: relative;
      width: 100%;
      height: 240px;
      background: #000;
      overflow: hidden;
    }

    .card-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }

    .moto-card:hover .card-img-wrap img { transform: scale(1.05); }

    .category-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(12, 13, 14, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
    }

    .card-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .moto-title {
      font-size: 1.5rem;
      color: #fff;
      margin-bottom: 10px;
    }

    .moto-desc-preview {
      color: var(--text-muted);
      font-size: 0.92rem;
      line-height: 1.55;
      margin-bottom: 20px;
      flex-grow: 1;
    }

    .card-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 12px;
      padding-top: 16px;
      border-top: 1px solid var(--border);
    }

    .btn-detail {
      background: rgba(230, 27, 36, 0.15);
      border: 1px solid rgba(230, 27, 36, 0.3);
      color: #ff525a;
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-detail:hover {
      background: var(--primary-red);
      color: #fff;
    }

    /* Modal for Full Descriptions and Specs */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(10px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .modal-overlay.open { display: flex; animation: fadeIn 0.2s ease; }

    .modal-card {
      background: #15171a;
      border: 1px solid var(--border-focus);
      border-radius: 16px;
      max-width: 900px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 36px;
      position: relative;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px var(--accent-glow);
    }

    @media (max-width: 768px) { .modal-card { padding: 20px; } }

    .modal-close {
      position: absolute;
      top: 20px;
      right: 20px;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #fff;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      font-size: 1.2rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s;
    }

    .modal-close:hover { background: var(--primary-red); }

    .modal-header {
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }

    .modal-title { font-size: 2.2rem; color: #fff; margin-bottom: 6px; }

    .modal-section-title {
      font-size: 1.2rem;
      color: var(--primary-red);
      margin: 24px 0 12px;
      letter-spacing: 0.05em;
    }

    .modal-text {
      color: #d1d5db;
      font-size: 0.95rem;
      line-height: 1.7;
      white-space: pre-line;
      margin-bottom: 20px;
    }

    .modal-specs-box {
      background: #0d0e10;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.9rem;
      line-height: 1.6;
      color: #e5e7eb;
      white-space: pre-wrap;
    }

    .modal-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin: 20px 0;
    }

    .modal-gallery img {
      width: 100%;
      height: 160px;
      object-fit: cover;
      border-radius: 8px;
      border: 1px solid var(--border);
    }

    /* History & Detailed Story Section */
    .story-section {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 48px;
      margin-bottom: 60px;
    }

    @media (max-width: 768px) { .story-section { padding: 24px; } }

    .story-section h2 {
      font-size: 2.4rem;
      margin-bottom: 24px;
      color: #fff;
    }

    .story-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
    }

    @media (max-width: 768px) { .story-grid { grid-template-columns: 1fr; } }

    .story-text {
      color: #c9d1d9;
      font-size: 0.95rem;
      line-height: 1.7;
      white-space: pre-line;
    }

    .advantages-box {
      background: #0d0e10;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .adv-item {
      display: flex;
      gap: 14px;
    }

    .adv-icon {
      color: var(--primary-red);
      font-size: 1.2rem;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .adv-title {
      font-weight: 700;
      font-family: 'Oswald', sans-serif;
      font-size: 1.1rem;
      color: #fff;
      margin-bottom: 4px;
      text-transform: uppercase;
    }

    .adv-desc {
      color: var(--text-muted);
      font-size: 0.9rem;
      line-height: 1.5;
    }

    /* Contacts Footer */
    footer {
      background: #08090a;
      border-top: 1px solid var(--border);
      padding: 60px 0 40px;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 40px;
      margin-bottom: 40px;
    }

    .footer-col h4 {
      font-size: 1.2rem;
      color: #fff;
      margin-bottom: 16px;
      letter-spacing: 0.05em;
    }

    .footer-col p, .footer-col a {
      color: var(--text-muted);
      font-size: 0.95rem;
      text-decoration: none;
      display: block;
      margin-bottom: 8px;
    }

    .footer-col a:hover { color: var(--primary-red); }

    .copyright {
      text-align: center;
      padding-top: 30px;
      border-top: 1px solid var(--border);
      color: #666;
      font-size: 0.85rem;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.96); }
      to { opacity: 1; transform: scale(1); }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="container nav-container">
      <a href="#" class="brand">MINSK <span>MOTO</span></a>
      <ul class="nav-links">
        <li><a href="#models">Модельный ряд</a></li>
        <li><a href="#history">История бренда</a></li>
        <li><a href="#advantages">Преимущества</a></li>
        <li><a href="#contacts">Контакты</a></li>
      </ul>
    </div>
  </header>

  <!-- Hero -->
  <section class="hero">
    <div class="container">
      <div class="hero-tag">МОТОЦИКЛЫ С 1951 ГОДА</div>
      <h1>ЛЕГЕНДАРНЫЙ БЕЛОРУССКИЙ БРЕНД</h1>
      <p>Официальный полный каталог и техническое руководство модельного ряда мототехники MINSK. Создано для города, трасс и сурового бездорожья.</p>
      <div>
        <a href="#models" class="btn">Каталог моделей ↓</a>
        <a href="#history" class="btn btn-secondary">История завода</a>
      </div>
    </div>
  </section>

  <!-- Quick Facts -->
  <div class="container">
    <div class="history-strip">
      <div class="history-item">
        <div class="history-num">1951</div>
        <div class="history-label">Год основания</div>
      </div>
      <div class="history-item">
        <div class="history-num">6.5M+</div>
        <div class="history-label">Мотоциклов выпущено</div>
      </div>
      <div class="history-item">
        <div class="history-num">10</div>
        <div class="history-label">Моделей в каталоге</div>
      </div>
      <div class="history-item">
        <div class="history-num">5000+</div>
        <div class="history-label">Запчастей в наличии</div>
      </div>
    </div>
  </div>

  <!-- Models Catalog Section -->
  <section id="models" class="container">
    <div class="filter-bar">
      <button class="filter-btn active" onclick="filterCategory('ALL')">Все модели</button>
      <button class="filter-btn" onclick="filterCategory('CLASSIC')">Classic</button>
      <button class="filter-btn" onclick="filterCategory('URBAN')">Urban</button>
      <button class="filter-btn" onclick="filterCategory('ENDURO')">Enduro</button>
      <button class="filter-btn" onclick="filterCategory('ADVENTURE')">Adventure</button>
      <button class="filter-btn" onclick="filterCategory('SCOOTER')">Scooters</button>
    </div>

    <div class="catalog-grid" id="catalog-container">
      <!-- Generated via JS -->
    </div>
  </section>

  <!-- Detailed History Section -->
  <section id="history" class="container">
    <div class="story-section">
      <h2>История мотоциклов «МИНСК»</h2>
      <div class="story-grid">
        <div class="story-text">""" + data['history'] + """</div>
        <div>
          <div style="border-radius: 12px; overflow: hidden; margin-bottom: 24px; border: 1px solid var(--border);">
            <img src="images/page_02.jpg" alt="История Минск" style="width: 100%; display: block;">
          </div>
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--border);">
            <img src="images/page_45.jpg" alt="Завод МотоВело" style="width: 100%; display: block;">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Advantages Section -->
  <section id="advantages" class="container">
    <div class="story-section" style="margin-bottom: 80px;">
      <h2>Почему выбирают MINSK?</h2>
      <div class="advantages-box">
        <div class="adv-item">
          <div class="adv-icon">★</div>
          <div>
            <div class="adv-title">Надежность и контроль качества</div>
            <div class="adv-desc">Мы сотрудничаем только с лучшими и проверенными поставщиками комплектующих, производя тщательный отбор и контроль всех деталей и узлов для сборки мотоциклов MINSK.</div>
          </div>
        </div>
        <div class="adv-item">
          <div class="adv-icon">★</div>
          <div>
            <div class="adv-title">Популярность и сообщество</div>
            <div class="adv-desc">Марку ценят и любят, существует большой вторичный рынок мототехники, фан-клубы, группы владельцев, отзывы и отчеты по эксплуатации. Вам всегда будет с кем покататься и пообщаться.</div>
          </div>
        </div>
        <div class="adv-item">
          <div class="adv-icon">★</div>
          <div>
            <div class="adv-title">70+ лет опыта производства</div>
            <div class="adv-desc">Каждая модель тщательно прорабатывается и испытывается в лаборатории завода, все мотоциклы получают сертификаты качества. Сегодня производственная площадка «MINSK» — одна из самых крупных в Восточной Европе.</div>
          </div>
        </div>
        <div class="adv-item">
          <div class="adv-icon">★</div>
          <div>
            <div class="adv-title">Сервис и гарантия</div>
            <div class="adv-desc">Официальная гарантия — 1 год либо 3000 км. Обслуживание производится в авторизованных дилерских центрах. В наличии всегда более 5000 наименований запасных частей для оперативного ремонта.</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Contacts Footer -->
  <footer id="contacts">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="brand" style="margin-bottom: 16px;">MINSK <span>MOTO</span></div>
          <p>ООО «МотоВелоЗавод»</p>
          <p>Республика Беларусь, 220033, г. Минск, Партизанский пр-т, 8</p>
        </div>
        <div class="footer-col">
          <h4>Контакты</h4>
          <p>Приемная: +375 17 298-21-03</p>
          <p>Отдел продаж: +375 44 562-84-58</p>
          <a href="mailto:info@mvz.by">info@mvz.by</a>
          <a href="mailto:moto@motovelo.by">moto@motovelo.by</a>
        </div>
        <div class="footer-col">
          <h4>Сервис и веб-ресурсы</h4>
          <p>Сервисный центр: bgom@motovelo.by</p>
          <p>Instagram: @minsk.motorcycles</p>
          <a href="http://www.minsk-moto.by" target="_blank">www.minsk-moto.by</a>
        </div>
      </div>
      <div class="copyright">
        © 2026 ООО «МотоВелоЗавод». Полная интерактивная веб-презентация модельного ряда MINSK.
      </div>
    </div>
  </footer>

  <!-- Modal -->
  <div class="modal-overlay" id="modal" onclick="if(event.target === this) closeModal()">
    <div class="modal-card">
      <button class="modal-close" onclick="closeModal()">×</button>
      <div class="modal-header">
        <span class="hero-tag" id="modal-category" style="margin-bottom: 8px;">CATEGORY</span>
        <h2 class="modal-title" id="modal-title">MODEL NAME</h2>
      </div>
      
      <div class="modal-gallery" id="modal-gallery"></div>

      <div class="modal-section-title">ОПИСАНИЕ МОДЕЛИ</div>
      <div class="modal-text" id="modal-desc"></div>

      <div class="modal-section-title">ОСОБЕННОСТИ И КОНСТРУКЦИЯ</div>
      <div class="modal-text" id="modal-features"></div>

      <div class="modal-section-title">ПОЛНЫЕ ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</div>
      <div class="modal-specs-box" id="modal-specs"></div>
    </div>
  </div>

  <script>
    const modelsData = """ + json.dumps(data['models'], ensure_ascii=False) + """;

    function renderCards(list) {
      const container = document.getElementById('catalog-container');
      container.innerHTML = list.map(m => {
        const lines = m.desc.split('\\n').filter(x => x.length > 5);
        const previewDesc = lines.slice(0, 3).join(' ');
        return `
          <div class="moto-card" data-category="${m.category}">
            <div class="card-img-wrap">
              <img src="images/${m.img}" alt="${m.title}" loading="lazy">
              <span class="category-badge">${m.category}</span>
            </div>
            <div class="card-body">
              <h3 class="moto-title">${m.title}</h3>
              <p class="moto-desc-preview">${previewDesc}</p>
              <div class="card-actions">
                <span class="mono" style="font-size: 0.82rem; color: var(--text-muted);">Подробно из буклета</span>
                <button class="btn-detail" onclick="openModal('${m.id}')">Все детали →</button>
              </div>
            </div>
          </div>
        `;
      }).join('');
    }

    function openModal(id) {
      const m = modelsData.find(x => x.id === id);
      if (!m) return;

      document.getElementById('modal-title').innerText = m.title;
      document.getElementById('modal-category').innerText = m.category;
      document.getElementById('modal-desc').innerText = m.desc;
      document.getElementById('modal-features').innerText = m.features;
      document.getElementById('modal-specs').innerText = m.specs;

      const gallery = document.getElementById('modal-gallery');
      gallery.innerHTML = `
        <img src="images/${m.img}" alt="${m.title}">
        <img src="images/${m.subimg_1}" alt="Особенности ${m.title}">
        <img src="images/${m.subimg_2}" alt="Характеристики ${m.title}">
      `;

      document.getElementById('modal').classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function closeModal() {
      document.getElementById('modal').classList.remove('open');
      document.body.style.overflow = 'auto';
    }

    function filterCategory(cat) {
      document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');

      if (cat === 'ALL') {
        renderCards(modelsData);
      } else {
        const filtered = modelsData.filter(m => m.category === cat || (cat === 'SCOOTER' && m.category === 'SCOOTERS'));
        renderCards(filtered);
      }
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });

    renderCards(modelsData);
  </script>
</body>
</html>
"""

with open('/opt/data/minsk-moto-site/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Updated index.html successfully.')
