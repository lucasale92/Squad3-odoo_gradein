{
    "name": "Squad3-odoo_gradein",
    "version": "1.0",
    "author": "Squad3",
    "depends": ["base"],
    "installable": True,
    "application": True,
    "data": [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        # 'views/odoo_gradein_view.xml',
        # 'reports/odoo_gradein_report.xml',
        'views/gradein_answer_views.xml',
    ],
    
}