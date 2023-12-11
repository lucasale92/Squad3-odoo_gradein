from odoo import models, fields

class Preguntas(models.Model):
    _name = 'servicios.preguntas'
    _description = 'Modelo para registrar preguntas prefijadas'

    # Restricción para permitir lectura a Vendedores y escritura, creación y borrado a Administradores
    def _check_permission(self):
        user = self.env.user
        if user.has_group('servicios.group_vendedor'):
            return [('active', '=', True)]
        return []

    # Definir restricciones de acceso para la vista lista
    def _compute_domain(self):
        domain = self._check_permission()
        return domain

    # Restringir los registros según el grupo de usuarios
    def read(self, fields=None, load='_classic_read'):
        domain = self._compute_domain()
        return super(Preguntas, self.with_context(active_test=False)).search_read(domain=domain, fields=fields, load=load)

    # Restringir la creación, escritura y borrado de registros
    def create(self, vals):
        if not self.env.user.has_group('services.group_administrador'):
            raise AccessError("No tiene permisos para crear preguntas.")
        return super(Preguntas, self).create(vals)

    def write(self, vals):
        if not self.env.user.has_group('services.group_administrador'):
            raise AccessError("No tiene permisos para editar preguntas.")
        return super(Preguntas, self).write(vals)

    def unlink(self):
        if not self.env.user.has_group('services.group_administrador'):
            raise AccessError("No tiene permisos para borrar preguntas.")
        return super(Preguntas, self).unlink()
