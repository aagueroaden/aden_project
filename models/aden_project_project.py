from odoo import fields, models


class AdenProject(models.Model):
    _description = 'Customized version of project.project for ADEN'
    _inherit = "project.project"

    team_id = fields.Many2one(
        comodel_name="aden_project.team",
        string="Project Team",
    )
