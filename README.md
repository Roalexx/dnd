# DnD – Character Builder & Game Data API

Modern bir **Dungeons & Dragons (5e)** web projesi.  
Backend: **Flask + SQLAlchemy** (PostgreSQL) • Frontend: **React**  
Amaç: DnD sınıfları, büyüler, ekipmanlar ve ırklar gibi verilerle **karakter oluşturma**, **detay görüntüleme** ve **oyun mekaniği** için sağlam bir temel sağlamak.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-336791)
![License](https://img.shields.io/badge/License-Choose--one-green)

---

## İçindekiler
- [Özellikler](#özellikler)
- [Mimari](#mimari)
- [Hızlı Başlangıç](#hızlı-başlangıç)
  - [Önkoşullar](#önkoşullar)
  - [Backend (Flask) Kurulum](#backend-flask-kurulum)
  - [Frontend (React) Kurulum](#frontend-react-kurulum)
- [Ortam Değişkenleri](#ortam-değişkenleri)
- [Veritabanı ve Veri Kaynakları](#veritabanı-ve-veri-kaynakları)
- [Örnek API Uçları](#örnek-api-uçları)
- [Proje Yapısı](#proje-yapısı)
- [Geliştirme Rehberi](#geliştirme-rehberi)
- [Yol Haritası](#yol-haritası)
- [Katkı](#katkı)
- [Lisans](#lisans)
- [Teşekkür](#teşekkür)

---

## Özellikler
- **Karakter Oluşturma**: Sınıf, ırk, yetenek puanları (point-buy), diller, ekipman ve başlangıç yetenekleri.
- **Detay Sayfaları**: Karaktere ait tüm ilişkili verilerin (spells, equipment, traits, skills, conditions) salt okunur görünümü.
- **DnD 5e Verileri**: Sınıflar, büyüler ve ekipmanlar gibi referans verilerle ilişkili şema.
- **JWT Tabanlı Kimlik Doğrulama**: Kendi karakterlerini oluşturma ve listeleme.
- **Swagger/Flasgger Dokümantasyonu**: API’yi canlı keşfetme / test etme.
- **Modüler Mimari**: Ayrık “backend” ve “frontend” klasörleri, temiz API katmanı.

---

## Mimari
- **Backend**: Flask + SQLAlchemy, Marshmallow şemaları, opsiyonel Alembic migrasyonları.  
- **Frontend**: React (Vite), modern component yapısı, Form ve dropdown’lar ile dinamik seçimler.  
- **DB**: PostgreSQL (ilişkisel model + DnD referans verileri).  

---

## Hızlı Başlangıç

### Önkoşullar
- **Python** 3.11+
- **Node.js** 18/20+
- **PostgreSQL** 13+ (lokal veya docker)

### Backend (Flask) Kurulum
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
createdb dnd_test
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Frontend (React) Kurulum
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

---

## Ortam Değişkenleri
Backend `.env` (örnek):
```
FLASK_ENV=development
SECRET_KEY=change-me
JWT_SECRET_KEY=change-me-too
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/dnd_test
CORS_ORIGINS=http://localhost:5173
DEEPL_API_KEY=
```

Frontend `.env` (örnek):
```
VITE_API_BASE_URL=http://localhost:5000
```

---

## Veritabanı ve Veri Kaynakları
- **PostgreSQL** üzerinde normalize tablolar.
- Kaynak veriler: [5e-bits/5e-database](https://github.com/5e-bits/5e-database)  

---

## Örnek API Uçları
```http
POST /auth/login
POST /auth/register
GET  /classes
GET  /classes/{id}
GET  /class-levels/{class_id}/{level}
GET  /spells
GET  /spells/{id}
POST /characters
GET  /characters/my-characters
GET  /characters/{id}
```

---

## Proje Yapısı
```
dnd/
├─ backend/
│  ├─ app.py
│  ├─ config/
│  ├─ models/
│  ├─ schemas/
│  ├─ routes/
│  ├─ services/
│  ├─ utils/
│  ├─ migrations/
│  ├─ requirements.txt
│  └─ .env.example
├─ frontend/
│  ├─ src/
│  │  ├─ pages/
│  │  ├─ components/
│  │  ├─ services/
│  │  └─ styles/
│  ├─ index.html
│  ├─ package.json
│  └─ .env.example
├─ docs/
│  └─ images/
└─ README.md
```

---

## Yol Haritası
- [ ] proficiency_choices için dinamik dropdown
- [ ] Point-Buy bütçe kontrolü
- [ ] Race ability bonus çoklu desteği
- [ ] Starting equipment otomatik doldurma
- [ ] Spell seçimlerinde tooltip desteği
- [ ] Read-only detay sayfası geliştirme
- [ ] Performans optimizasyonu

---

## Katkı
1. Issue aç.
2. Fork & branch oluştur.
3. Test et, linter çalıştır.
4. PR aç.


---

## Teşekkür
- **5e-bits/5e-database** topluluğuna teşekkürler.
- Kırıkkale Üniversitesi Bilgisayar Mühendisliği projesi kapsamında geliştirildi.
