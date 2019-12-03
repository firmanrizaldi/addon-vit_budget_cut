from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class budget_lines(models.Model):
    _name = 'crossovered.budget.lines'
    _inherit = 'crossovered.budget.lines'


    name = fields.Char("Name", compute="_get_name")


    @api.depends('general_budget_id')
    def _get_name(self):
        for rec in self:
            rec.name = rec.general_budget_id.name