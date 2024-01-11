from odoo import fields, models


class User(models.Model):
    # _inherit = "res.users"
    _inherit = "res.partner"
    _description = "Extension of res.partner, adding extra features to users"

    team_id = fields.Many2one(
        comodel_name="aden_project.team",
        string="Project Team"
    )


class Team(models.Model):
    _name = "aden_project.team"
    _description = "Teams for the Aden project system, allow users to be part of a team"

    name = fields.Char(string='Team Name', required=True)
    team_area = fields.Char(string='Team Area', required=True)

    project_ids = fields.One2many(
        comodel_name='project.project',
        inverse_name="team_id",
        string='Project',
        readonly=True
    )

    user_ids_members = fields.One2many(
        comodel_name='res.users',  # uses res.users instead of res.partner to not show the sales fields, etc
        inverse_name="team_id",
        string='Members',
        help='Team Members',
        readonly=True
    )

    task_ids = fields.One2many(
        comodel_name='project.task',
        inverse_name="team_id",
        string='Task',
        readonly=True
    )
