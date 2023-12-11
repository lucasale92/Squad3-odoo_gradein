from odoo import models, fields, api
class GradeInQuestion(models.Model):
    _name = 'gradein.question'
    _description = 'Gradein Model'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)
    equipment_type_ids = fields.Many2many('gradein_equipment', string='TypeEquipment')
    answer_ids = fields.Many2many('gradein.answer', string='Answers')