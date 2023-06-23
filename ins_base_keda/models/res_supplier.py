from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResSupplier(models.Model):
    _name = "res.supplier"

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)

    @api.constrains('code')
    def _check_code(self):
        self.ensure_one()
        domain = [('code', '=ilike', self.code), ('id', '!=', self.id)]
        rec = self.search(domain)
        if rec:
            raise ValidationError('Code already exists!')
