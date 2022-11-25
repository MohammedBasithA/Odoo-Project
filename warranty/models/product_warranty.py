from odoo import fields, models, api, _


class ProductWarranty(models.Model):
    _name = "product.warranty"
    _description = "Product Warranty"
    _rec_name = 'sequence_number'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    invoice_id = fields.Many2one('account.move', 'Invoice Number', domain="[('move_type', '=', 'out_invoice')]",
                                 required=True)
    product_id = fields.Many2one('product.product', string='Product')

    lot_id = fields.Many2one('stock.lot', 'Lot Number')
    request_date = fields.Date('Request Date', default=fields.Date.today())
    name = fields.Char('Customer Name', related='invoice_id.partner_id.name')
    purchase_date = fields.Date('Purchase Date', related='invoice_id.invoice_date')
    sequence_number = fields.Char(string='Reference Number ', required=True, readonly=True, default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approve', 'Approve'),
        ('cancel', 'Cancel')], default='draft', string='status')

    @api.onchange('invoice_id')
    def _onchange_invoice_id(self):
        products = self.invoice_id.invoice_line_ids.product_id
        return {'domain': {'product_id': [('id', 'in', products.ids),('warranty_ok','!=' , False)]}}

    @api.onchange('product_id')
    def _onchange_product_id(self):
        lots = self.product_id

        return {'domain': {'lot_id': [('product_id', 'in', lots.ids)]}}

    @api.model
    def create(self, vals):
        if vals.get('sequence_number', _('New')) == _('New'):
            vals['sequence_number'] = self.env['ir.sequence'].next_by_code(
                'product.warranty') or _('New')
        res = super(ProductWarranty, self).create(vals)
        return res






# sub_district_id' : fields.many2one('sna.sub.district', 'Sub District', domain="[('sub_district_id', '=', district_id)]", select=True, required=True),


# @api.onchange('product_id')
# def _onchange_product_id(self):
#
#
# # self.name_id = self.invoice_id.partner_id.name
# # self.purchase_date = self.invoice_id.invoice_date
# self.lot_number = self.product_id.name


# @api.model
# def _getUserGroupId(self):
#     return [('groups_id', '=', self.env.ref('module.xml_id').id)]
# rel_ids = fields.Many2many(comodel_name='res.users', relation='my_relation_table_name', column1='rel_id',
#                            column2='user_id', string='Relation field', domain=_getUserGroupId)




# domain="[('move_id', '=' , invoice_id),('product_id', '!=' , False)]", required=True)