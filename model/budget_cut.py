#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
import time


SESSION_STATES =[('draft','Draft'),('confirmed','Confirmed'),
('done','Done')]


class budget_cut(models.Model):

    _name = "vit.budget_cut"
    _inherit = "mail.thread"



    name = fields.Char(string="Name", readonly=True )
    
    
    nomor_sk_direksi = fields.Char( string="Nomor sk direksi",  help="")
    state = fields.Selection(selection=SESSION_STATES,  string="State",default=SESSION_STATES[0][0],  help="")
    date_budget_cut = fields.Date( string="Date budget cut",  help="", default=lambda self: time.strftime("%Y-%m-%d"))


    budget_id = fields.Many2one(comodel_name="crossovered.budget",  string="Budget",  help="")
    line_ids = fields.One2many(comodel_name="vit.budget_cut_line",  inverse_name="budget_cut_id",  string="Lines",  help="")

    @api.multi
    def action_draft(self):
        self.state = SESSION_STATES[0][0]

    @api.multi
    def action_confirm(self):
        self.state = SESSION_STATES[1][0]

    @api.multi
    def action_done(self):
        self.state = SESSION_STATES[2][0]
        for line in self.line_ids:
            line.budget_line_id.planned_amount = line.new_amount


    @api.model
    def create(self, vals):
        if not vals.get('name', False) or vals['name'] == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('vit.budget_cut') or 'Error Number!!!'
        return super(budget_cut, self).create(vals)

