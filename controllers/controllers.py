# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class VitPortofolio(http.Controller):

	# <model("hr.employee"):employee_id> = parameter id employee
	@http.route("/portofolio/<model('hr.employee'):employee_id>", auth='public')
	def index(self, employee_id, **kw): # hasil parsing di masukan ke fungsi
		return request.render("vit_portofolio.index", {
			'employee_id'	: employee_id,
		})