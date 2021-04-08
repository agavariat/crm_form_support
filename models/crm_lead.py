# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError

class CountryStateCity(models.Model):
    """
    Model added to manipulate separately the cities on Partner address.
    """
    _description = 'Model to manipulate Cities'
    _name = 'res.country.state.city'

    code = fields.Char('City Code', size=5, help='Code DANE - 5 digits-',)
    name = fields.Char('City Name', size=64, )
    state_id = fields.Many2one('res.country.state', 'State')
    country_id = fields.Many2one('res.country', 'Country', default='Colombia')
    _order = 'code'

class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'

    name = fields.Char('Beneficios')

class modelo69form(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.form.many2many'

    name = fields.Char('69form')

class modelo72inf(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.inf.many2many'

    name = fields.Char('72inform')

class modelo72form(models.Model):
    _description = 'Modelo para Manipular Many2many72'
    _name = 'model.many2many72'

    name = fields.Char('72form')

class modelo73form(models.Model):
    _description = 'Modelo para Manipular Many2many73'
    _name = 'model.many2many73'

    name = fields.Char('73form')

class modelo75inf(models.Model):
    _description = 'Modelo para Manipular Many2many75'
    _name = 'model.many2many75'

    name = fields.Char('75form')

class modelo76inf(models.Model):
    _description = 'Modelo para Manipular Many2many76'
    _name = 'model.many2many76'

    name = fields.Char('76form')

class modelo102inf(models.Model):
    _description = 'Modelo para Manipular Many2many102'
    _name = 'model.many2many102'

    name = fields.Char('102form')

class modelo176form(models.Model):
    _description = 'Modelo para Manipular Many2many176'
    _name = 'model.many2many176'

    name = fields.Char('176form')

class modelo176form(models.Model):
    _description = 'Modelo para Manipular Many2many177'
    _name = 'model.many2many177'

    name = fields.Char('177form')

class Lead(models.Model):
    _inherit = "crm.lead"

    x_nombre = fields.Char(
    	related ="name",
        string="2. Nombre del Propietario",
        help="Ingrese el nombre del propietario",
        readonly=False
    )

    x_nombre_negocio = fields.Char(
        string="1. Nombre del Negocio",
        help="Ingrese el nombre del negocio",
        readonly=False
    )

    x_datos1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "SELECCIONE SI PARA COMENZAR",
    )

    doctype = fields.Selection(
        [
            ('sin_identificacion', 'Sin identificación'),
            ('cedula', 'Cédula'),
            ('cedula_de_extranjeria', 'Cédula de extranjería'),
            ('pasaporte', 'Pasaporte'),
            ('permiso_especial_de_permanencia_pep', 'Permiso especial de permanencia (PEP)'),

        ], "3. Tipo de identificación", default='cedula'
    )

    x_identification = fields.Integer(
        string="4. Número de identificación",
        help="Ingrese el tipo de identificación ",
        store=True,
    )

    _sql_constraints = [
        ('x_identification',
         'UNIQUE (x_identification)',
         "El número de documento debe ser único!"),
    ]

    x_cont1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "1. Una vez comprendido el programa de acompañamiento, ¿usted desea continuar?",
    )

    x_datos3 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "DESEA CONTINUAR CON EL DIAGNOSTICO",
    )
    
    #MÓDULO planear diagnostico
    x_dcont1 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_proto1 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "1. ¿ Su empresa afilia a todos sus empleados a la Seguridad Social (pensiones, salud y ARL)?",
    )

    x_proto2 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "2. ¿Ha definido una Política de Seguridad y Salud en el trabajo?",
    )

    x_proto3 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "3. ¿Ha creado un Documento del Sistema de Gestión de Seguridad y Salud SGSST en el Trabajo?",
    )

    x_proto4 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "4. ¿Están definidos los objetivos del SG-SST, son medibles, coherentes con el Plan de trabajo Anual en SST, se encuentran documentados, comunicados a los trabajadores y son evaluados periódicamente y actualizados de ser necesario?",
    )

    x_proto5 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "5. ¿Cuenta con un documento “deberes y responsabilidades del Empleador y del trabajador”; está divulgado a sus trabajadores y se le hace seguimiento?",
    )

    x_proto6 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "6. ¿Sus empleados conocen sus responsabilidades en cuanto al Sistema de Seguridad y Salud en el Trabajo?",
    )

    x_proto7 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "7. ¿La empresa ha diseñado una herramienta de comunicación en doble dirección del (empleador con el empleado ), se encuentra documentada en algún documento especificando su procedimiento?",
    )

    x_proto8 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "8. ¿La empresa cuenta con Indicadores del sistema de gestión de seguridad y salud en el trabajo?",
    )

    x_proto9 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "9. ¿Su empresa Cuenta con el Vigía Ocupacional o con el Comité Paritario de Seguridad y salud en el Trabajo (COPASST)?",
    )

    x_proto10 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "10. ¿Su empresa Cuenta con el Reglamento interno de trabajo y lo divulga entre los trabajadores?",
    )

    x_proto11 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "11. ¿Cuenta con el Reglamento de Higiene y seguridad industrial y lo divulga?",
    )

    x_proto12 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "12. ¿Identifica sus Peligros, Evalua y Valora los Riesgos?",
    )

    x_proto13 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "13. ¿Cuenta con Programa anual de capacitación y lo divulga?",
    )

 

   
    #hacer
    x_dcont2 = fields.Boolean(
        string="continuar con el Formulario",
    )
    x_proto14 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "14. Realiza Inspecciones planeadas y Realiza correctivos?",
    )

    x_proto15 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "15. Cuenta con Fichas de seguridad de las sustancias quimicas que utiliza?",
    )

    x_proto16 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "16. Cuenta con Procedimientos, instructivos y normas de seguridad para riesgos prioritarios?",
    )
    
    x_model21 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "17. Cuenta con un Programa de Elementos de Protección Personal, donde se identifique cuales necesita, como se utilizan, se capacite al personal y se tenga un plan de reposición?",
        oldname="model21"
    )
    x_model22 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "18. Realiza Exámenes médicos de ingreso, periódicos y de retiro a sus trabajadores?",
        oldname="model22"
    )
    x_model23 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "19. Cuenta con Programas de Vigilancia Epidemiológica específicos de sus riesgos prioritarios que puedan generar una enfermedad laboral?",
        oldname="model23"
    )
    x_model24 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "20. Cuenta con un Plan de prevención, preparación y respuesta ante emergencias",
        oldname="model24"
    )
    x_model25 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),     
        ], "21. Cuenta con una Brigada de emergencias capacitada?",
        oldname="model25"
    )
    x_model26 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),    
        ], "22. Cuenta con un Plan de evacuación y sus responsables?",
        oldname="model26"
    )
    x_model27 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "23. Realiza Simulacros por lo menos una vez al año?",
        oldname="model27"
    )
    x_model28 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "24. Realiza la Investigación de los Accidentes de Trabajo en los tiempos establecidos por la legislación Nal?",
        oldname="model28"
    )
    x_model29 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "25. Cumple con el desarrollo del programa de Capacitación?",
        oldname="model29"
    )

    ##validar
    x_model30 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "26. Valida la gerencia el cumplimiento del sistema de gestión de seguridad y salud en el trabajo?",
        oldname="model30"
    )
    x_model31 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "27. Gestiona los Correctivos generadados por la investigación de accidentes de trabajo?",
        oldname="model31"
    )
    x_model32 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "28. Cuenta con indicadores para medir la gestión en seguridad y salud en el trabajo?",
        oldname="model32"
    )

    ##actuar
    x_model33 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "29. Genera y gestiona Acciones preventivas y correctivas?",help="Una acción correctiva es aquella que llevamos a cabo para eliminar la causa de un problema. Las correcciones atacan los problemas, las acciones correctivas sus causas. Las acciones preventivas se anticipan a la causa, y pretenden eliminarla antes de su existencia. Evitan los problemas identificando los riesgos. Cualquier acción que disminuya un riesgo es una acción preventiva",
        oldname="model33"
    )
    x_model34 = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),
        ], "30. Mejora continua: Da las directrices y otorgar los recursos necesarios PARA mejorar la eficacia de sus actividades en el sistema de gestión de seguridad y salud en el trabajo?",
        oldname="model34"
    )
    
    #gavii
#FORMALIZACION SECCION 3: ADMINISTRACION
    x_dcont3 = fields.Boolean(
        string="Continuar con el Formulario",
    )
 
    x_dcont4 = fields.Boolean(
        string="Continuar con el Formulario",
    )
   
    x_dcont5 = fields.Boolean(
        string="Continuar con el Formulario",
    )
 
    x_dcont6 = fields.Boolean(string="Continuar con el Formulario")
    
    x_dcont7 = fields.Boolean(string="Continuar con el Formulario")
   
    x_dcont8 = fields.Boolean(string="Continuar con el Formulario")
    

    country_id = fields.Many2one('res.country', "Country")
    xcity = fields.Many2one('res.country.state.city', "9. Municipio de Residencia")
    city = fields.Char(related="xcity.name")


    x_state_id = fields.Many2one('res.country.state', '21. Departamento donde se ubica su negocio')
    x_city_id = fields.Many2one('res.country.state.city', '22. Municipio donde se ubica su negocio')

    @api.onchange('country_id', 'state_id')
    def onchange_location(self):
        """
        This functions is a great helper when you enter the customer's
        location. It solves the problem of various cities with the same name in
        a country
        @param country_id: Country Id (ISO)
        @param state_id: State Id (ISO)
        @return: object
        """

        if self.state_id:
            mymodel = 'res.country.state.city'
            filter_column = 'state_id'
            check_value = self.state_id.id
            domain = 'xcity'
        else:
            return {}

        obj = self.env[mymodel]
        ids = obj.search([(filter_column, '=', check_value)])
        id_domain = []
        for id in ids:
            id_domain.append(id.id)
        
        return {
            'domain': {domain: [('id', 'in', id_domain)]},
            'value': {domain: ''}
        }
        #