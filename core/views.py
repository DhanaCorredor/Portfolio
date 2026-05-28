from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def cv_marketing(request):
    return render(request, 'cv-marketing.html')


def index(request):
    experience = [
        {
            'company': _('Independent — Asisty + clients'),
            'position': _('MarTech & Frontend (Freelance)'),
            'period': _('Oct 2025 — Present'),
            'location': _('Remote · Spain'),
            'description': _('Self-led MarTech platform Asisty (Next.js 15, healthcare sector) plus freelance work for SMEs: SEO, web optimization, analytics and A/B testing.'),
            'tech': ['Next.js', 'TypeScript', 'SEO', 'GA4'],
        },
        {
            'company': 'Quirónsalud',
            'position': _('Administrative Technician'),
            'period': _('Jun 2024 — Oct 2025'),
            'location': _('Madrid, Spain'),
            'description': _('Administrative management, process control and operational support in hospital environment.'),
            'tech': ['Process Mgmt', 'Healthcare'],
        },
        {
            'company': 'Future Retail S.L.',
            'position': _('Project Manager'),
            'period': _('Oct 2022 — May 2024'),
            'location': _('Madrid, Spain'),
            'description': _('Digital strategy, social media and web optimization for retail clients. Cross-departmental coordination and reporting to direction.'),
            'tech': ['HubSpot', 'Meta Ads', 'GA4', 'WordPress'],
        },
        {
            'company': 'Cultura Emprende Radio',
            'position': _('Communications Manager'),
            'period': _('May 2018 — Sep 2022'),
            'location': _('Madrid, Spain'),
            'description': _('Communication management for the leading entrepreneurship show on Radio Intereconomía 95.1FM. Web design, social media and guest agenda.'),
            'tech': ['WordPress', 'Mailchimp', 'Social Media'],
        },
        {
            'company': 'Urban Lab Madrid',
            'position': _('Project Manager'),
            'period': _('Feb 2017 — Sep 2022'),
            'location': _('Madrid, Spain'),
            'description': _('B2B marketing and communication for clients: social media strategy, email marketing in Mailchimp and HubSpot, Meta Ads campaigns, reporting to direction.'),
            'tech': ['HubSpot', 'Mailchimp', 'Meta Ads', 'WordPress'],
        },
        {
            'company': 'Apolo Agencia Digital',
            'position': _('Project Technician'),
            'period': _('Oct 2014 — Apr 2016'),
            'location': _('Madrid, Spain'),
            'description': _('Digital campaign analysis and optimization: paid social, email marketing and basic SEO. Google Ads and Meta Ads configuration.'),
            'tech': ['Google Ads', 'Meta Ads', 'WordPress', 'GA'],
        },
        {
            'company': 'Bancaribe International Bank',
            'position': _('Marketing Intern'),
            'period': _('Sep 2013 — May 2014'),
            'location': _('Venezuela'),
            'description': _('Internal communications, merchandising inventory, digital marketing campaign assistance and CRM database updates.'),
            'tech': ['CRM', 'Internal Comms'],
        },
    ]

    projects = [
        {
            'title': 'Lorena Velásquez Studio',
            'description': _('Active entrepreneurship project: website for a premium manicure studio and academy in Moratalaz, Madrid. Built with Vite + React 18 + TypeScript + Tailwind. Integrated booking flow (Confirmafy), social channels and conversion-oriented landing.'),
            'live_url': 'https://lorena-velasquez-studio.vercel.app',
            'github_url': 'https://github.com/DhanaCorredor/LorenaVelasquezStudio',
            'tags': ['React', 'TypeScript', 'Vite', 'Branding'],
            'featured': True,
        },
        {
            'title': 'Viandas de Salamanca',
            'description': _('E-commerce of gourmet products (jamones, embutidos, quesos). Web layout, content editing and brand uniform design as part of the Future Retail team. The most ambitious commercial collaboration in my path.'),
            'live_url': 'https://viandasstores.com',
            'github_url': '',
            'tags': ['E-commerce', 'UX', 'Branding', 'WordPress'],
            'featured': True,
        },
        {
            'title': 'Asisty',
            'description': _('Health marketing platform built with Next.js 15. Hybrid approach: clinical authority via minimalist UI, conversion-focused CTAs and SEO-ready structure for healthcare professionals and clinics.'),
            'live_url': 'https://loopy-laces.vercel.app',
            'github_url': 'https://github.com/DhanaCorredor/asisty',
            'tags': ['Next.js', 'TypeScript', 'MarTech', 'Healthcare'],
            'featured': True,
        },
        {
            'title': 'Tiro al Blanco',
            'description': _('Browser game inspired by carnival shooting galleries. Three difficulty levels, combo multiplier, daily leaderboard and live integrations with GNews and OpenWeatherMap APIs.'),
            'live_url': 'https://tiro-al-blanco-ten.vercel.app',
            'github_url': 'https://github.com/DhanaCorredor/tiro-al-blanco',
            'tags': ['Vanilla JS', 'Game', 'APIs', 'Mobile First'],
            'featured': False,
        },
        {
            'title': 'Covid Tracker',
            'description': _('React front-end for a dashboard that consumes the Disease covimap API and displays pandemic data dynamically with charts and country breakdowns.'),
            'live_url': '',
            'github_url': 'https://github.com/DhanaCorredor/Covid-Tracker',
            'tags': ['React', 'Dashboard', 'REST API'],
            'featured': False,
        },
        {
            'title': 'Google Store (Atomic)',
            'description': _('Pixel-perfect responsive layout of the Google Store. Designed in Figma using Atomic Design methodology and built with semantic HTML5, CSS3 and vanilla JavaScript.'),
            'live_url': '',
            'github_url': 'https://github.com/DhanaCorredor/Google_Store_Dynamic',
            'tags': ['HTML/CSS', 'Figma', 'Atomic Design'],
            'featured': False,
        },
    ]

    education = [
        {'school': 'Factoría F5', 'degree': _('AI Bootcamp — Python, Game Dev & Programming'), 'year': '2026'},
        {'school': 'freeCodeCamp', 'degree': _('Professional Certificate in Project Management'), 'year': '2023'},
        {'school': 'ThePower Business School', 'degree': _('Rock{TheCode} — Full Stack Development'), 'year': '2023'},
        {'school': 'ENEB Barcelona', 'degree': _('Master in Commercial Direction & Advertising'), 'year': '2017 — 2019'},
        {'school': _('International University of La Rioja'), 'degree': _('Bachelor in Business Administration'), 'year': '2013 — 2017'},
    ]

    industries = [
        _('Healthcare'),
        _('Retail & E-commerce'),
        _('Banking'),
        _('Media & Radio'),
        _('B2B Services'),
    ]

    references = [
        # {'name': 'Jane Doe', 'role': 'CMO at Future Retail', 'quote': 'She delivered ...'},
    ]

    return render(request, 'index.html', {
        'experience': experience,
        'projects': projects,
        'education': education,
        'industries': industries,
        'references': references,
    })
