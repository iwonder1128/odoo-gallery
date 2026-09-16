from odoo import models


class FSMOrder(models.Model):
    _name = "fsm.order"
    _inherit = ["fsm.order", "base_multi_image.owner"]
