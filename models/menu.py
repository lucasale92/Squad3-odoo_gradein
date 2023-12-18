# from odoo import models, fields

# class MainServices(models.Model):
#     _name = "services"
#     _rec_name = "services_name"
#     _order = "services_name ASC"
#     _description = "Main Services"
    
from odoo import models, api
class GrupoServicios(models.Model):
    _name = 'grupo.servicios'
    _description = 'Group services'
    


    @api.model
    def _create_group(self):
        
        group = self.env['res.groups'].create({
            'name': 'Group Services',
            'implied_ids': [(6, 0, [self.env.ref('base.group_user').id])],
             
        })
        return group