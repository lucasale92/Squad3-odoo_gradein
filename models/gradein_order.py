from odoo import models, fields

class GradeInOrder(models.Model):
    _name = 'gradein.order'
    _description = 'Gradein Order'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected')],
        default='draft', string='State')
    equipment_id = fields.Many2one('gradein.equipment', string='Equipment')
    imei = fields.Char(string='IMEI')
    partner_id = fields.Many2one('res.partner', string='Client')
    price = fields.Float(string='Price')
    review = fields.Text(string='Review')
    answer_ids = fields.Many2many('gradein.answer', string='Answer')
    question_id = fields.Many2one('gradein.question', string='Question')
    reject_motive_id = fields.Many2one('gradein.reject.motive', string='Reject Motive')
    image_ids = fields.Many2many('ir.attachment', string='Image')