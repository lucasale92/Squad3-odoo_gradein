from odoo import models, fields

class GradeInEquipmentType(models.Model):
    _name = 'gradein.equipment.type'
    _description = "GradeIn Equipment Type"    

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image')
    active = fields.Boolean(string='Active', default=True)
    question_ids = fields.Many2many('gradein.question', string='Questions')

