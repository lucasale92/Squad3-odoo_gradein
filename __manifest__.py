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
        # 'views/odoo_gradein_view.xml',
        # 'reports/odoo_gradein_report.xml',
        'views/menu_services.xml',
        'views/gradein_answer_views.xml',
        #'views/gradein_question_views.xml',
    ],
    
}