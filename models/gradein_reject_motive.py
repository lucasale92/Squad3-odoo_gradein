from odoo import models, fields, api
class GradeInRejectMotive(models.Model):
    _name = 'gradein.reject.motive'
    _description = 'Gradein Reject Motive'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)
