# from odoo import models, fields

# class MainServices(models.Model):
#     _name = "services"
#     _rec_name = "services_name"
#     _order = "services_name ASC"
#     _description = "Main Services"
    
from odoo import models, api
class GrupoServicios(models.Model):
    _name = 'grupo.servicios'
    _description = 'Grupo de Usuarios para Servicios'
    # Definición de campos (si es necesario)
    # ...
    @api.model
    def _create_group(self):
        """Método para crear el grupo de usuarios"""
        group = self.env['res.groups'].create({
            'name': 'Grupo de Servicios',
            'implied_ids': [(6, 0, [self.env.ref('base.group_user').id])],
            # Aquí puedes agregar más permisos según sea necesario
        })
        return group