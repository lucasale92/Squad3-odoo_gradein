{
    "name": "Squad3-odoo_gradein",
    "version": "1.0",
    "author": "Squad3",
    "depends": ["base"],
    "installable": True,
    "application": True,
    "data": [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/menu_services.xml',
        'views/gradein_rejection_motive.xml',
        'views/gradein_answer_views.xml',
        'views/gradein_question_views.xml',
        'views/gradein_equipment_type_views.xml',
        'views/gradein_equipment_views.xml',
        'views/gradein_order_views.xml',
        'reports/gradein_reports.xml',        
    ],
        'images': [
        'static/description/icon.png',
    ],
}