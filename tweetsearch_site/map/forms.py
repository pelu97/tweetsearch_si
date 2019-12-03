from django import forms

class QueryConfig(forms.Form):
    dateini = forms.DateField(help_text="Insira a data inicial:",
                           input_formats=['%d/%m/%Y',
                                          '%d/%m/%y',
                                          '%Y-%m-%d'])
    datefim = forms.DateField(help_text="Insira a data final:",
                           input_formats=['%d/%m/%Y',
                                          '%d/%m/%y',
                                          '%Y-%m-%d'])
    est_mun = forms.CharField(help_text="Insira se deseja mostrar os resultados agrupados por Estado (E) ou Municipio (M).", max_length=1)
