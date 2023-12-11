from odoo import models, fields

class GradeInAnswer(models.Model):
    _name = 'gradein.answer'
    _description = 'GradeIn Answer'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activa", default=True)
    price_reduction = fields.Float(string="Reduce el precio en")