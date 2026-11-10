from odoo import fields, models

class ProductTemplate(models.Model):
  _inherit = 'product.template'

  catalog_section = fields.Selection(
    selection=[('machine', 'Máquina'),
               ('spare', 'Refacción'),
               ('extra', 'Aditamento'),
               ('service', 'Servicio'),
    ],
    string='Categoría de catálogo'
  )

  machine_ids = fields.Many2many(
    comodel_name='product.template',
    relation='compat_machine_part_rel',
    column1='part_id',
    column2='machine_id',
    string='Máquinas compatibles',
    domain=[('catalog_section', '=', 'machine')]
  )

  part_ids = fields.Many2many(
    comodel_name='product.template',
    relation='compat_machine_part_rel',
    column1='machine_id',
    column2='part_id',
    string='Refacciones y aditamentos',
    domain=[('catalog_section', '=', ['spare', 'extra', 'service'])]
  )