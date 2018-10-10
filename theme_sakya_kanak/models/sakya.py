from odoo import fields, models

class BlogPost(models.Model):
    _inherit = "blog.post"

    url = fields.Char(string="Video url")