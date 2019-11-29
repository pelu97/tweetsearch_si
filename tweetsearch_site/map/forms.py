from django import forms

class QueryConfig(forms.Form):
    date = forms.DateField(help_text="Insira a data de uma busca para mostrar no mapa.",
                           input_formats=['%d/%m/%Y',
                                          '%d/%m/%y',
                                          '%Y-%m-%d'])
    est_mun = forms.CharField(help_text="Insira se deseja mostrar os resultados agrupados por Estado (E) ou Municipio (M).", max_length=1)
