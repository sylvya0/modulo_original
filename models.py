from odoo import models, fields, api

class Socio(models.Model):
    _name = 'basico.socio'
    _description = 'socio'
    name = fields.Char(required=True)
    orden = fields.One2many(comodel_name='basico.orden', inverse_name='socio')


class Orden(models.Model):
    _name = 'basico.orden'
    _description = 'orden'
    name = fields.Char(required=True)
    socio = fields.Many2one(comodel_name='basico.socio', string='socio')
    cantidad = fields.Float()
