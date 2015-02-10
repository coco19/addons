# -*- coding: utf-8 -*-

from openerp import fields, models, api

class Medico (models.Model):
    
    _inherits = {
        'res.partner' : 'partner_id'
    }
    
    _name = 'farmacia.medico'
    
    nombre = fields.Char(string = "Nombre", required=True)
    apellido = fields.Char(string = "Apellido", required=True)
    numero_matricula = fields.Integer(string = "Número Matricula")
    
    #Restriccion sql
    _sql_constraints = [
        ('numero_matricula_unico',
         'UNIQUE(numero_matricula)',
         "La matricula del medico debe ser unica"),
    ]

    
# seteo del atributo _name de la clase res_partner usando decorador depends

    @api.onchange('nombre', 'apellido')
    def _onchange_nombre_apellido(self):
        self.name = str(self.nombre) + " " + str(self.apellido)