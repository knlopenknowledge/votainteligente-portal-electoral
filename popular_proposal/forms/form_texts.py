# coding=utf-8
from collections import OrderedDict

WHEN_CHOICES = [
    ('', '----'),
    ('6_months', u'6 Meses'),
    ('1_year', u'1 año'),
    ('2_year', u'2 años'),
    ('3_year', u'3 años'),
    ('4_year', u'4 años'),
]

TOPIC_CHOICES = (('', u'Selecciona una categoría'),
                 ('salud', u'Salud'),
                 ('educacion', u'Educación'),
                 ('cultura', u'Cultura y patrimonio'),
                 ('asistencia', u'Asistencia y protección social'),
                 ('empleabilidad', u'Empleabilidad y emprendimiento'),
                 ('deporte', u'Deporte y recreación'),
                 ('conectividad', u'Conectividad y obras'),
                 ('areasverdes', u'Áreas verdes y espacios públicos'),
                 ('seguridad', u'Seguridad y prevención de catástrofes'),
                 ('medioambiente', u'Medio ambiente y recolección de basura'),
                 ('participacion', u'Participación y sociedad civil'),
                 )

TEXTS = OrderedDict({
    'problem': {'label': u' ',
                'preview_question': u'¿Cuál es el problema?',
                'help_text': u'',
                'placeholder': u'¿Cuál es el problema que afecta a la comuna (o barrio) de la que el alcalde debe hacerse cargo?',
                'long_text': "paso1.html"},
    'causes': {'label': u' ',
               'preview_question': u'¿Cuáles son las causas?',
               'help_text': u'',
               'placeholder': u'Utiliza el ejercicio que te mostramos arriba para encontrar las causas del problema',
               'long_text': "paso2.html"},
    'solution': {'label': u'Escribe tu propuesta',
                 'preview_question': u'¿Cual sería la solución?',
                 'help_text': u'',
                 'placeholder': u'Siguiendo el ejemplo, propongan la(s) medida(s) que el alcalde debe tomar para solucionar la causa del problema y poder alcanzar la situación ideal.',
                 'long_text': "paso3.html"},
    'solution_at_the_end': {'label': u' ',
                            'preview_question': u'¿Cuál sería la solución?',
                            'help_text': u'',
                            'placeholder': u'Que la Municipalidad de Pelarco destine un 20% más de recursos al año para colegios o liceos.\n\rQue la Municipalidad de Pelarco elabore e implemente un plan junto a los profesores de Educación Media para optimizar los recursos en educación.',
                            'long_text': "paso4a.html"},
    'when': {'label': u'¿Cuándo?',
             'preview_question': u'¿Cuándo debería estar esto listo?',
             'help_text': u'6_months',
             'placeholder': u'',
             'long_text': "paso4b.html"},
    'title': {'label': u'Colócale título',
              'preview_question': u'Título',
              'help_text': u'',
              'placeholder': u'Mejoremos la educación en la comuna',
              'long_text': "paso5a.html"},
    'clasification': {'label': u'Primero elige una categoría',
                      'preview_question': u'Clasificación',
                      'help_text': u'educacion',
                      'placeholder': u'',
                      'long_text': "paso5b.html"},
    'organization': {'label': u'',
                     'preview_question': u'Organización',
                     'help_text': u'',
                     'placeholder': u'',
                     'long_text': "organization.html"},
    'terms_and_conditions': {'label': u'Términos y condiciones',
                             'preview_question': u'',
                             'help_text': u'',
                             'placeholder': u'',
                             'long_text': "terms_and_conditions.html"},
}
