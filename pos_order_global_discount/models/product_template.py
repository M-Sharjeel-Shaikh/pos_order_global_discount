from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_discount = fields.Boolean(
        string="Is a Discount",
        help="Check this box if you use this product to realize"
        " discount on sale. If check the sale lines will be"
        " ignored when computing the amount without discount."
        " If you use 'Pos Discount' Odoo module, you should"
        " check this box for the product you configured"
        " as the 'Discount Product' on your PoS config.",
    )
