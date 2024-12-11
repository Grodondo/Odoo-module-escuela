from odoo import models, fields

class Asignatura(models.Model):
    _name = 'escuela.asignatura'
    _description = 'Asignatura'

    codigo = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    horas = fields.Integer(string='Horas', required=True)
