# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PortofolioSkills(models.Model):
    _name = 'portofolio.skills'

    name = fields.Char(string='Nama', required=True)
    score = fields.Integer(string='Score', required=True)