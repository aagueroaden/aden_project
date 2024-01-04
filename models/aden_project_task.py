from odoo import models, fields


class AdenTask(models.Model):
    _name = 'aden_project.aden_task'
    _description = 'Customized version of project.task for ADEN'
    _inherit = 'project.task'

    priority = fields.Selection([
        ('0', 'Muy Baja'),
        ('1', 'Baja'),
        ('2', 'Media'),
        ('3', 'Alta'),
        ('4', 'Muy Alta'),
        ('5', 'Urgente'),
    ], string='Priority', default='0', tracking=True)
