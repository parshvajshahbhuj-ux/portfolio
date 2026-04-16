# Parshva Shah — Developer Portfolio

A production-grade personal portfolio website built with Django and vanilla JavaScript. Designed with an Apple + Stripe inspired dark UI featuring glassmorphism cards, particle animations, and a fully dynamic backend.

**Live:** [parshva-portfolio.onrender.com](https://parshva-portfolio.onrender.com)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.2, Python 3.12 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Static Files | WhiteNoise |
| Deployment | Render |
| Fonts | Inter, JetBrains Mono (Google Fonts) |

---

## Features

- **Dynamic project listing** — projects and skills managed via Django admin and database
- **Slug-based project detail pages** — clean URLs for each project
- **Contact form** — with validation and database storage
- **Interactive particle canvas** — mouse-reactive WebGL-style background
- **Typing animation** — role cycling in the hero section
- **Scroll-based fade-in** — IntersectionObserver animations
- **Dark / Light theme toggle** — persisted via localStorage
- **Scroll progress bar** — fixed top indicator
- **Project tech filter** — client-side filtering with no page reload
- **Resume download** — direct PDF serving from static files
- **Back to top button** — appears after scrolling, smooth scroll
- **Skeleton loading states** — shimmer placeholders for project cards
- **Custom SVG illustrations** — unique themed banners per project
- **Responsive** — mobile-first, works on all screen sizes
- **Django Admin** — customized with search, filters, and branding

---

## Pages

| Route | Page |
|---|---|
| `/` | Home — Hero, Bento stats, Why Hire Me, Projects, Hackathons, Skills |
| `/about/` | About — Bio, Skills, Certificates, Education, Timeline |
| `/projects/` | Projects — Full grid with tech filter |
| `/projects/<slug>/` | Project Detail — Description, tech stack, GitHub/demo links |
| `/contact/` | Contact — Form with validation |
| `/admin/` | Django Admin Panel |

---

## Project Structure

```
portfolio/
├── core/                   # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/              # Main app
│   ├── models.py           # Project, Skill, ContactMessage
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── seed_data.py
├── templates/
│   ├── base.html
│   ├── components/
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   ├── project_card.html
│   │   └── project_illustrations.html
│   └── portfolio/
│       ├── home.html
│       ├── about.html
│       ├── projects.html
│       ├── project_detail.html
│       └── contact.html
├── static/
│   ├── css/main.css
│   ├── js/
│   │   ├── main.js
│   │   └── hero-canvas.js
│   ├── certificates/       # PDF certificates
│   └── resume.pdf
├── .env                    # Local environment variables
├── requirements.txt
├── Procfile
├── build.sh
└── runtime.txt
```

---

## Local Setup

**1. Clone the repository**

```bash
git clone https://github.com/parshvajshahbhuj-ux/portfolio.git
cd portfolio
```

**2. Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment**

Create a `.env` file in the root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

**5. Run migrations and seed data**

```bash
python manage.py migrate
python manage.py seed_data
```

**6. Create admin user**

```bash
python manage.py createsuperuser
```

**7. Start the development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## Database Models

### Project
| Field | Type | Notes |
|---|---|---|
| title | CharField | |
| slug | SlugField | Auto-generated, unique |
| description | TextField | |
| tech_stack | CharField | Comma-separated |
| github_link | URLField | |
| live_demo | URLField | Optional |
| image | ImageField | Optional |
| created_at | DateTimeField | Auto |

### Skill
| Field | Type | Notes |
|---|---|---|
| name | CharField | |
| category | CharField | Programming / Web / Tools / Database |

### ContactMessage
| Field | Type | Notes |
|---|---|---|
| name | CharField | |
| email | EmailField | |
| message | TextField | |
| created_at | DateTimeField | Auto |

---

## Deployment (Render)

**Environment Variables required on Render:**

| Key | Value |
|---|---|
| `SECRET_KEY` | A long random string |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app.onrender.com` |

**Build Command:**
```
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start Command:**
```
python manage.py migrate --noinput && python manage.py seed_data && gunicorn core.wsgi:application
```

---

## Admin Panel

Access at `/admin/` with your superuser credentials.

- **Projects** — Add/edit with slug auto-fill, search by title/tech, filter by date
- **Skills** — Manage by category
- **Contact Messages** — Read-only inbox, searchable

---

## License

MIT — free to use as a template. Attribution appreciated.

---

*Built by [Parshva Shah](https://github.com/parshvajshahbhuj-ux)*
