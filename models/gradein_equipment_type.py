from odoo import models, fields

class GradeInEquipmentType(models.Model):
    _name = 'gradein.equipment.type'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Imagen')
    active = fields.Boolean(string='Activo', default=True)
    question_ids = fields.One2many('gradein.question', 'answer_ids', string='Preguntas')
