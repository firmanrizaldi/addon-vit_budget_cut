#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class budget_cut_line(models.Model):

    _name = "vit.budget_cut_line"

    # budgetary_position_id = fields.Char( string="Budgetary position",  help="")
    current_amount = fields.Float( string="Current amount",  help="")
    new_amount = fields.Float( string="New amount",  help="")
    name = fields.Char( required=True, string="Name",  help="")

    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)
    company_id = fields.Many2one(related='budget_cut_id.budget_id.company_id', comodel_name='res.company',
        string='Company', store=True, readonly=True)

    budget_cut_id = fields.Many2one(comodel_name="vit.budget_cut",  string="Budget cut",  help="")
    budget_line_id = fields.Many2one(comodel_name="crossovered.budget.lines", string="Budget Lines", help="")

    @api.onchange('budget_line_id')
    def onchange_budget_line(self):
        self.current_amount = self.budget_line_id.planned_amount


    @api.depends('budget_line_id')
    def _get_name(self):
        for rec in self:
            rec.name = rec.budget_line_id.general_budget_id.name