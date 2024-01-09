from odoo import models, fields, api


class AdenTask(models.Model):
    _description = 'Customized version of project.task for ADEN'
    _inherit = 'project.task'

    prioridad = fields.Selection(selection=[
        ('5', '5 [Muy Baja]'),
        ('4', '4 [Baja]'),
        ('3', '3 [Media]'),
        ('2', '2 [Alta]'),
        ('1', '1 [Muy Alta]'),
        ('0', '0 [Urgente]'),
    ], string='Prioridad', default='5', tracking=True)

    team_id = fields.Many2one(
        comodel_name="aden_project.team",
        string="Project Team",
    )

    @api.onchange('user_ids')
    def _onchange_user_ids_add_remove_team_id(self):
        # need to make a "for task in self", to also work in the kanban/list views
        for task in self:

            if task.user_ids:
                # toma al primer usuario en los user_ids
                first_user = task.user_ids[0]

                if not first_user.team_id:
                    task.user_ids = False
                    # muestra un pop up de error
                    return {
                        'warning': {
                            'title': 'Usuario sin equipo!',
                            'message': f"El usuario {first_user.name} no esta asociado a un equipo, asegurate de agregarlo a uno"}
                    }

                # asigna el equipo del usuario al equipo del la task
                task.team_id = first_user.team_id
