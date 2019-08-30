from odoo import api, fields, models
from odoo.exceptions import UserError

class ResConfigSettings(models.TransientModel):

  _inherit = 'res.config.settings'

  @api.multi 
  def check_menus(self):
    MenuObj = self.env['ir.ui.menu']
    domain = ['&', ('parent_id', '=', False), ('groups_id', '=', False)]
    names1 = MenuObj.search(domain).mapped('name')
    domain = ['&', ('parent_id', '=', False), 
      ('groups_id', '=', self.env.ref('hidemenu.group_hide_menus').id)]
    names2 = MenuObj.search(domain).mapped('name')
    msg = 'Visiable menus: %s\nHidden menus: %s' % (names1, names2)
    raise UserError(msg)
