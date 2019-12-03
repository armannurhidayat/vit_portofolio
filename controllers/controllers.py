# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class VitPortofolio(http.Controller):

	# (hr.employee.id)
	@http.route('/portofolio/', auth='public')
	def index(self, **kw):
		employees	= request.env['hr.employee'].search([])
		skills 		= request.env['portofolio.skills'].search([])

		return request.render("vit_portofolio.index", {
			'karyawan'	: employees,
			'skills' 	: skills,
		})