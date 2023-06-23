from odoo import models, fields, api, _


class ResSupplier(models.Model):
    _name = "res.supplier"

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
