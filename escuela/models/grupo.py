from odoo import models, fields

class Grupo(models.Model):
    _name = 'escuela.grupo'
    _description = 'Grupo'

    nombre = fields.Char(string='Descripción', required=True)
    modulo_profesional = fields.Selection(
        [('SMR', 'SMR'), ('DAM', 'DAM'), ('DAW', 'DAW'), ('ASIR', 'ASIR')],
        string='Módulo Profesional',
        default='SMR'
    )
    curso = fields.Selection(
        [('1', '1º'), ('2', '2º')],
        string='Curso',
        default='1'
    )
    estudiantes_ids = fields.One2many('escuela.estudiante', 'grupo_id', string='Estudiantes')
    asignaturas_ids = fields.Many2many('escuela.asignatura', string='Asignaturas')
