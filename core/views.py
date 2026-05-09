from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    experience = [
        {
            'company': 'Loopy Laces',
            'position': _('Project Technician'),
            'period': _('Oct 2025 — Present'),
            'location': _('Spain'),
            'description': _('Supporting entrepreneurs and SMEs with their digital marketing projects since 2022.'),
            'achievements': [
                _('UX/UI & Web Optimization: design and improvement of user-centered interfaces, accessibility and conversion.'),
                _('SEO & Digital Marketing: organic positioning strategies and content optimization in WordPress.'),
                _('Web Project Management: design and development coordination for SMEs, integrating analytics and A/B testing.'),
            ],
            'tech': ['WordPress', 'SEO', 'GA4', 'Figma'],
        },
        {
            'company': 'Quirónsalud',
            'position': _('Administrative Technician'),
            'period': _('Jun 2024 — Oct 2025'),
            'location': _('Madrid, Spain'),
            'description': '',
            'achievements': [],
            'tech': [],
        },
        {
            'company': 'Future Retail S.L.',
            'position': _('Project Manager'),
            'period': _('Oct 2022 — May 2024'),
            'location': _('Madrid, Spain'),
            'description': _('Strategy, analysis and optimization of social media and Web for retail clients.'),
            'achievements': [
                _('Digital marketing project management and customer experience improvement in retail stores.'),
                _('Cross-departmental project follow-up and execution.'),
                _('Content, design and signage proposals aligned with client and franchise branding to boost in-store sales.'),
                _('Results analysis, reporting and process/cost optimization proposals.'),
            ],
            'tech': ['HubSpot', 'Meta Ads', 'GA4', 'WordPress'],
        },
        {
            'company': 'Cultura Emprende Radio',
            'position': _('Communications Manager'),
            'period': _('May 2018 — Sep 2022'),
            'location': _('Madrid, Spain'),
            'description': _('Spreading valuable content for the leading Entrepreneurship radio show on Radio Intereconomía 95.1FM.'),
            'achievements': [
                _('Show content editing.'),
                _('Web design and social media management.'),
                _('Guest agenda management.'),
            ],
            'tech': ['WordPress', 'Mailchimp', 'Social Media'],
        },
        {
            'company': 'Urban Lab Madrid',
            'position': _('Project Manager'),
            'period': _('Feb 2017 — Sep 2022'),
            'location': _('Madrid, Spain'),
            'description': _('Marketing and Communication project management for clients.'),
            'achievements': [
                _('Social media strategy and email marketing campaigns in Mailchimp and HubSpot.'),
                _('Advertising campaigns on Instagram and Facebook ads.'),
                _('Content management for Cultura Emprende Radio Intereconomía.'),
                _('Signage layout and digital content proposals for clients.'),
                _('Project follow-up with agencies, suppliers and collaborators.'),
                _('Analysis and reporting for management presentations.'),
            ],
            'tech': ['HubSpot', 'Mailchimp', 'Meta Ads', 'WordPress'],
        },
        {
            'company': 'Apolo Agencia Digital',
            'position': _('Project Technician'),
            'period': _('Oct 2014 — Apr 2016'),
            'location': _('Madrid, Spain'),
            'description': _('Analysis and optimization of digital campaigns: social media, email marketing and basic SEO.'),
            'achievements': [
                _('Monitoring metrics in Google Analytics, WordPress administration.'),
                _('Configuring ads in Google Ads and Meta Ads.'),
            ],
            'tech': ['Google Ads', 'Meta Ads', 'WordPress', 'GA'],
        },
        {
            'company': 'Bancaribe International Bank',
            'position': _('Marketing Intern'),
            'period': _('Sep 2013 — May 2014'),
            'location': _('Venezuela'),
            'description': _('Internal communications, merchandising inventory control, digital marketing campaign assistance and CRM database updates.'),
            'achievements': [],
            'tech': ['CRM'],
        },
    ]

    skill_categories = [
        {
            'title': _('Frontend & Data'),
            'icon': 'code',
            'skills': [
                {'name': 'JavaScript (ES6+)', 'level': 80},
                {'name': 'HTML5 / CSS3', 'level': 90},
                {'name': 'Angular', 'level': 70},
                {'name': 'Git & GitHub', 'level': 80},
                {'name': 'GA4 / GTM / Looker', 'level': 85},
                {'name': 'React / Python', 'level': 50},
            ],
        },
        {
            'title': _('Marketing & Growth'),
            'icon': 'chart',
            'skills': [
                {'name': 'SEO / SEMrush', 'level': 90},
                {'name': 'Meta Ads', 'level': 85},
                {'name': 'Klaviyo / Email', 'level': 80},
                {'name': 'Make.com / Zapier', 'level': 80},
                {'name': 'HubSpot / Salesforce', 'level': 85},
                {'name': 'Copywriting', 'level': 80},
            ],
        },
        {
            'title': _('Tools & Methods'),
            'icon': 'tools',
            'skills': [
                {'name': 'Figma (UX/UI)', 'level': 85},
                {'name': 'WordPress', 'level': 90},
                {'name': 'SCRUM', 'level': 80},
                {'name': 'Notion', 'level': 90},
                {'name': 'Jira', 'level': 75},
                {'name': 'Project Management', 'level': 90},
            ],
        },
    ]

    projects = [
        {
            'title': 'Aurora',
            'url': '',
            'description': _('Mental health support platform where users can book sessions or therapies with professionals at any time of the day.'),
            'bullets': [
                _('Content development modules support.'),
                _('Web layout & user panel modules.'),
                _('Blog implementation.'),
            ],
            'tags': ['WordPress', 'UX/UI', 'Blog'],
        },
        {
            'title': 'Viandas de Salamanca',
            'url': 'https://viandasstores.com',
            'description': _('E-commerce of gourmet products (jamones, embutidos, quesos). Web layout, content editing and price re-tagging for physical stores.'),
            'bullets': [
                _('Web layout and content editing support.'),
                _('Brand uniform proposal design with the team.'),
                _('Future Retail team member for sales-boosting UX proposals.'),
            ],
            'tags': ['E-commerce', 'UX', 'Branding'],
        },
        {
            'title': 'Cultura Emprende Radio',
            'url': 'https://culturaemprende.com',
            'description': _('Landing page for followers of the entrepreneurship radio show on Radio Intereconomía 95.1FM. Built end-to-end from client requirements.'),
            'bullets': [
                _('Full website creation per client needs.'),
            ],
            'tags': ['WordPress', 'Landing', 'SEO'],
        },
        {
            'title': 'PlayGreen',
            'url': '',
            'description': _('Betting platform partner portal where users can track their earnings and referred users.'),
            'bullets': [
                _('Layout support.'),
                _('Click strategy and featured panel design.'),
            ],
            'tags': ['UI', 'Dashboard', 'Strategy'],
        },
        {
            'title': 'Urban Lab Madrid',
            'url': 'https://urbanlabmadrid.com',
            'description': _('Website for the Urban Lab Madrid coworking and business center.'),
            'bullets': [
                _('Web layout support.'),
                _('Initial copywriting.'),
                _('Blog content writing.'),
            ],
            'tags': ['WordPress', 'Copywriting', 'Blog'],
        },
    ]

    education = [
        {'school': 'Factoría F5', 'degree': _('AI Bootcamp — Python, Game Dev & Programming'), 'year': '2026'},
        {'school': 'freeCodeCamp', 'degree': _('Professional Certificate in Project Management'), 'year': '2023'},
        {'school': 'ThePower Business School', 'degree': _('Rock{TheCode} — Full Stack Development'), 'year': '2023'},
        {'school': 'ENEB Barcelona', 'degree': _('Master in Commercial Direction & Advertising'), 'year': '2017 — 2019'},
        {'school': _('International University of La Rioja'), 'degree': _('Bachelor in Business Administration'), 'year': '2013 — 2017'},
    ]

    certifications = [
        _('Digital Content Design'),
        _('Content Marketing Strategies'),
        _('English B1 Intermediate'),
        _('Digital Marketing Fundamentals'),
    ]

    process = [
        {'title': _('Goals'), 'description': _('Define what success looks like before touching the keyboard. KPIs, scope and constraints.')},
        {'title': _('Research'), 'description': _('Audit the market, the competition and the audience. Data over opinion.')},
        {'title': _('Strategy'), 'description': _('Translate research into a clear positioning and channel mix.')},
        {'title': _('Ideas'), 'description': _('Generate creative concepts that fit the strategy and stretch the brand.')},
        {'title': _('Planning'), 'description': _('Roadmap, ownership and timelines so nothing falls through the cracks.')},
        {'title': _('Media plan'), 'description': _('Choose paid, owned and earned channels with a realistic budget.')},
        {'title': _('Promotion'), 'description': _('Launch, iterate and optimize creatives, audiences and bidding.')},
        {'title': _('Results analysis'), 'description': _('Read the numbers, separate signal from noise, share insights.')},
        {'title': _('Measurement'), 'description': _('Close the loop: report against KPIs and feed learnings into the next cycle.')},
    ]

    references = [
        # When user pastes recommendations, fill these dicts:
        # {'name': 'Jane Doe', 'role': 'CMO at Future Retail', 'quote': 'She delivered ...'},
    ]

    return render(request, 'index.html', {
        'experience': experience,
        'skill_categories': skill_categories,
        'projects': projects,
        'education': education,
        'certifications': certifications,
        'process': process,
        'references': references,
    })
