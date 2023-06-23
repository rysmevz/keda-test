from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResMaterial(models.Model):
    _name = "res.material"

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'), ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
        ], string="Material Type", required=True)
    buy_price = fields.Float('Buy Price', default=0.0, required=True)
    supplier_id = fields.Many2one('res.supplier', 'Supplier', required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        if self.buy_price < 100:
            raise ValidationError(_('Buy price cannot be greater than 100'))
