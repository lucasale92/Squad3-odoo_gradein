from odoo import models, fields

class GradeInAnswer(models.Model):
    _name = 'gradein.answer'
    _description = 'GradeIn Answer'

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    price_reduction = fields.Float(string="Price reduction")