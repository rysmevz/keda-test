from odoo.tests import common


class TestKeda(common.TransactionCase):

    def test_create_data(self):
        test_supplier = self.env['res.supplier'].create({
            'name': 'Ari Wibisono'
            'code': '1'
        })

        self.assertEqual(test_supplier.name, 'Ari Wibisono')
        self.assertEqual(test_material.code, '1')

        test_material = self.env['res.material'].create({
            'name': 'Material Test',
            'code': 'mt01',
            'material_type': 'fabric',
            'buy_price': 10000.0,
            'supplier_id': test_supplier.id
        })

        self.assertEqual(test_material.name, 'Material Test')
        self.assertEqual(test_material.code, 'mt01')
        self.assertEqual(test_material.material_type, 'fabric')
        self.assertEqual(test_material.buy_price, 10000.0)
        self.assertEqual(test_material.supplier_id, test_supplier.id)
