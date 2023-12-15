from odoo import models, api

class GradeinReport(models.AbstractModel):
    _name = 'report.gradein_order.gradein_order_report'
    _description = 'Gradein Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("****************************************************")
        print("GET REPORT VALUES")
        print("DATA", data)
        print("DOCIDS", docids)
        print("DOCSIDS FROM WIZARD", data.get('docs'))
        print("****************************************************")
        if data and data.get('docs'):
            docids = data.get('docs')
        docs = self.env['gradein.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'gradein.order',
            'docs': docs,
        }
