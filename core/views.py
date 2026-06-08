import logging

import resend
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _g
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)


def cv_marketing(request):
    return render(request, 'cv-marketing-web.html')


def cv_marketing_print(request):
    return render(request, 'cv-marketing.html')


def index(request):
    experience = [
        {
            'company': _('Independent — Asisty + clients'),
            'position': _('MarTech & Frontend (Freelance)'),
            'period': _('2022 — Present'),
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
            'company': 'Urban Lab Madrid',
            'position': _('Project Manager'),
            'period': _('Feb 2017 — Sep 2022'),
            'location': _('Madrid, Spain'),
            'description': _('In-house B2B marketing: lead-gen Meta Ads, email marketing in Mailchimp and HubSpot, corporate materials and reporting to direction. Launched and ran Cultura Emprende Radio — the company\'s own show on Radio Intereconomía 95.1FM — managing guest agenda, editorial production and digital presence.'),
            'tech': ['HubSpot', 'Mailchimp', 'Meta Ads', 'WordPress'],
        },
        {
            'company': 'Apolo Agencia Digital',
            'position': _('Project Manager Junior'),
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
            'live_url': 'https://asisty.vercel.app',
            'github_url': 'https://github.com/DhanaCorredor/asisty',
            'tags': ['Next.js', 'TypeScript', 'MarTech', 'Healthcare'],
            'featured': True,
        },
        {
            'title': 'Diagnóstico Centro de Salud',
            'description': _('Integral marketing for a Madrid health center since it opened in 2022: Meta Ads (Instagram + Facebook) lead-gen, brand and visual identity, and full social-media management from day one.'),
            'live_url': '',
            'github_url': '',
            'tags': ['Meta Ads', 'Branding', 'Healthcare', 'Social Media'],
            'featured': True,
        },
        {
            'title': 'Asahi Sushi Bar',
            'description': _('Sushi bar in Leganés, Madrid: website, social media and digital menu. In progress: a more robust v2 site and a custom table-to-kitchen order system.'),
            'live_url': '',
            'github_url': '',
            'tags': ['Web', 'Social Media', 'Hospitality'],
            'featured': False,
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
        {'school': 'Factoría F5', 'degree': _('Full Stack Bootcamp — Python'), 'year': '2026'},
        {'school': 'freeCodeCamp', 'degree': _('Professional Certificate in Project Management'), 'year': '2023'},
        {'school': 'ThePower Business School', 'degree': _('Rock{TheCode} — Full Stack Development'), 'year': '2023'},
        {'school': 'N+E Business School', 'degree': _('Specialist in Big Data & Business Analytics'), 'year': '2020'},
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


@require_POST
def contact(request):
    """Relay the contact form to the inbox via Resend, then redirect to #contact."""
    redirect_url = reverse('core:index') + '#contact'

    # Honeypot: real users leave this hidden field empty; bots fill it.
    if request.POST.get('company', '').strip():
        messages.success(request, _g('Thanks! Your message has been sent.'))
        return redirect(redirect_url)  # silently accept bots

    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        messages.error(request, _g('Please fill in your name, email and message.'))
        return redirect(redirect_url)

    if '@' not in email or '.' not in email.split('@')[-1]:
        messages.error(request, _g('That email address does not look valid.'))
        return redirect(redirect_url)

    if not settings.RESEND_API_KEY:
        logger.error('Contact form: RESEND_API_KEY is not configured.')
        messages.error(request, _g('Sorry, the form is unavailable right now. Please email me directly.'))
        return redirect(redirect_url)

    safe_name = name.replace('<', '').replace('>', '')
    body = message.replace('\n', '<br>')
    html = (
        f'<p><strong>From:</strong> {safe_name} &lt;{email}&gt;</p>'
        f'<hr><p>{body}</p>'
    )

    try:
        resend.api_key = settings.RESEND_API_KEY
        resend.Emails.send({
            'from': f'Portfolio <{settings.CONTACT_FROM_EMAIL}>',
            'to': [settings.CONTACT_TO_EMAIL],
            'reply_to': email,
            'subject': _g('New message from your portfolio — %(name)s') % {'name': name},
            'html': html,
        })
        messages.success(request, _g('Thanks! Your message has been sent.'))
    except Exception:
        logger.exception('Contact form: Resend send failed.')
        messages.error(request, _g('Something went wrong sending your message. Please email me directly.'))

    return redirect(redirect_url)
