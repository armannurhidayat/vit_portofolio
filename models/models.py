# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PortofolioSkills(models.Model):
	_name = 'portofolio.skills'

	name = fields.Char(string='Nama', required=True)
	score = fields.Integer(string='Score', required=True)
	skills_id = fields.Many2one(comodel_name="hr.employee", string="Nama", required=False)


class PortofolioWorks(models.Model):
	_name = 'portofolio.works'

	name = fields.Char(string='Nama', required=True)
	link = fields.Char(string='Link', required=True)
	description = fields.Text(string='Description')


class Employees(models.Model):
	_name = 'hr.employee'
	_inherit = 'hr.employee'

	skills_ids = fields.One2many(
		'portofolio.skills',
		'skills_id',
		string='Skills',
	)