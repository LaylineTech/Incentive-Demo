# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    start_time = fields.Float()
    end_time = fields.Float()

    @api.onchange('start_time','end_time')
    def _onchange_times(self):
        self.unit_amount = self.end_time - self.start_time if self.end_time > self.start_time else self.unit_amount

    # @api.model
    # def conv_time_float(self, value): 
    #     value = value.replace('.',':')
    #     vals = value.split(':')
    #     t , hours = divmod(float(vals[0]), 24) 
    #     t , minutes = divmod(float(vals[1]), 60) 
    #     minutes = minutes / 60.0 
    #     return hours + minutes

    # @api.model
    # def fix_date_fields(self):
    #     for line in self:
    #         if line.x_studio_start_time_1:
    #             line.start_time = line.conv_time_float(line.x_studio_start_time_1)
    #         if line.x_studio_end_time_1:
    #             line.end_time = line.conv_time_float(line.x_studio_end_time_1)