from odoo import models, fields

class GradeInEquipmentType(models.Model):
    _name = 'models.gradein.equipment.type'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Imagen')
    active = fields.Boolean(string='Activo', default=True)
    question_ids = fields.One2many('models.gradein.question', 'equipment_type_id', string='Preguntas')


class GradeInQuestion(models.Model):
    _name = 'models.gradein.question'

    name = fields.Char(string='Pregunta', required=True)
    equipment_type_id = fields.Many2one('tu_modulo.gradein.equipment.type', string='Tipo de Equipo')

