# -*- coding: utf-8 -*-
{
    'name': 'Sakya Website',
    'summary': 'Sakya — Sakya Webiste',
    'version': '1.0',
    'description': """
Sakya — Sakya — Sakya Webiste
================================================
        """,
    'category': 'Theme/Ecommerce',
    'author': 'Kanak Infosystems LLP.',
    'support': "info@kanakinfosystems.com",
    'depends': [
        'website',
        'website_crm',
        'auth_signup',
        'website_blog',
    ],
    'data': [
        'data/website_menu_data.xml',
        'views/views_temp.xml',
        'views/assets.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/contact_us.xml',
        'views/customize_modal.xml',
        'views/homepage.xml',
        'views/solution.xml',
        'views/blog.xml',
        'views/snippets.xml',

        # 'views/website_shop.xml',
    ],
    'demo': [
        
    ],
    'images': [
        'static/description/IMG_9782.JPG',
        'static/description/IMG_9782.JPG',
    ],
    'price': '150',
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'license': 'OPL-1',
    'live_test_url': 'http://v11.kanakinfosystems.com/web?db=theme_sakya_kanak',
}
