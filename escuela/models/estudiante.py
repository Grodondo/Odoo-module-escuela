from odoo import models, fields

class Estudiante(models.Model):
    _name = 'escuela.estudiante'
    _description = 'Estudiante'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos')
    edad = fields.Integer(string='Edad')
    grupo_id = fields.Many2one('escuela.grupo', string='Grupo')

