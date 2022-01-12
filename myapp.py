import pandas as pd

# Library-library Bokeh
from bokeh.plotting import figure, show, curdoc
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource, HoverTool, Div
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import column
from bokeh.models import NumeralTickFormatter

df2 = pd.read_csv('data/covid_19_indonesia_time_series_all.csv')

df2 = df2[['Date', 'Location', 'Island', 'New Cases',
           'New Recovered', 'New Deaths',
           'Total Cases', 'Total Recovered',
           'Total Deaths']]

df2['Date'] = pd.to_datetime(df2['Date'])
df2 = df2.rename(columns={"New Cases": "NewCases",
                          "New Recovered": "NewRecovered",
                          "NewDeaths": "NewDeaths",
                          "Total Cases": "TotalCases",
                          "Total Recovered": "TotalRecovered",
                          "Total Deaths": "TotalDeaths"})

# Proses output file data covid_19_indonesia_time_series_all.csv
output_notebook()
output_file('Covid-Indonesia.html',
            title='Covid Indonesia')


# Kasus untuk seluruh Indonesia
indonesia = df2[df2['Location'] == 'Indonesia']
indonesia['Island'] = 'Indonesia'
indonesia_cds = ColumnDataSource(indonesia)


# Definisikan figure untuk dijadikan sebagai plot diagram
tot_case_ind = figure(x_axis_type='datetime',
                      plot_height=500, plot_width=800,
                      title='Total Kasus Covid',
                      x_axis_label='Tanggal', y_axis_label='Total Kasus')

new_case_ind = figure(x_axis_type='datetime',
                      plot_height=500, plot_width=800,
                      title='Kasus Baru',
                      x_axis_label='Tanggal', y_axis_label='Kasus Baru')

# Definisikan y-axis
tot_case_ind.yaxis.formatter = NumeralTickFormatter(format="00")
new_case_ind.yaxis.formatter = NumeralTickFormatter(format="00")

# Definisikan line / proses render line
tot_case_ind.line('Date', 'TotalCases',
                  color='#CE1141', legend_label='Total Kasus di Seluruh Indonesia',
                  source=indonesia_cds)

new_case_ind.line('Date', 'NewCases',
                  color='#CE1141', legend_label='Kasus Baru di Seluruh Indonesia',
                  source=indonesia_cds)

# Definisikan legend dengan lokasi atas kiri
tot_case_ind.legend.location = 'top_left'
new_case_ind.legend.location = 'top_left'

# Definisikan tooltips
tooltips1 = [
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@TotalCases'),
]

tooltips2 = [
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@NewCases'),
]

# Defnisikan renderer sebagai hover
hover_glyph = tot_case_ind.circle(x='Date', y='TotalCases', source=indonesia_cds,
                                  size=5, alpha=0,
                                  hover_fill_color='black', hover_alpha=0.5)
hover_glyph2 = new_case_ind.circle(x='Date', y='NewCases', source=indonesia_cds,
                                   size=5, alpha=0,
                                   hover_fill_color='black', hover_alpha=0.5)

# Masukkan hover ke diagram / figure
tot_case_ind.add_tools(HoverTool(tooltips=tooltips1, formatters={
                       '@Date': 'datetime'}, renderers=[hover_glyph, hover_glyph2]))
new_case_ind.add_tools(HoverTool(tooltips=tooltips2, formatters={
                       '@Date': 'datetime'}, renderers=[hover_glyph, hover_glyph2]))

# Konfigurasi ukuran plot / diagram
tot_case_ind.plot_width = new_case_ind.plot_width = 1000

# Definisikan dua panel berisi total kasus dan kasus baru
tot_case_ind_panel = Panel(child=tot_case_ind, title='Total Kasus')
new_case_ind_panel = Panel(child=new_case_ind, title='Kasus Baru')

# Masukkan panel pada tabs button
tabs = Tabs(tabs=[tot_case_ind_panel, new_case_ind_panel])


## Plotting Kasus Covid-19 di seluruh Indonesia Selesai


## Plotting Kasus Covid-19 untuk setiap pulau di Indonesia 


# CDS Pulau Jawa dan Nusa Teanggara
jawa = df2[(df2['Island'] == 'Jawa') | (df2['Island'] == 'Nusa Tenggara')]
jawa = jawa.groupby(['Date']).sum().reset_index()
jawa['Island'] = 'Jawa dan Nusa Tenggara'
jawa_cds = ColumnDataSource(jawa)

# CDS Sumatera
sumatera = df2[df2['Island'] == 'Sumatera']
sumatera = sumatera.groupby(['Date']).sum().reset_index()
sumatera['Island'] = 'Sumatera'
sumatera_cds = ColumnDataSource(sumatera)

# CDS Kalimantan 
Kalimantan = df2[df2['Island'] == 'Kalimantan']
Kalimantan = Kalimantan.groupby(['Date']).sum().reset_index()
Kalimantan['Island'] = 'Kalimantan'
kalimantan_cds = ColumnDataSource(Kalimantan)

# CDS Sulawesi 
sulawesi = df2[df2['Island'] == 'Sulawesi']
sulawesi = sulawesi.groupby(['Date']).sum().reset_index()
sulawesi['Island'] = 'Sulawesi'
sulawesi_cds = ColumnDataSource(sulawesi)

# CDS Papua dan Maluku 
papua = df2[(df2['Island'] == 'Papua') | (df2['Island'] == 'Maluku')]
papua = papua.groupby(['Date']).sum().reset_index()
papua['Island'] = 'Papua dan Maluku'
papua_cds = ColumnDataSource(papua)

# Definisikan figure untuk dijadikan sebagai diagram 
tot_case = figure(x_axis_type='datetime',
                  plot_height=500, plot_width=800,
                  title='Total Kasus Covid',
                  x_axis_label='Tanggal', y_axis_label='Total Kasus')

new_case = figure(x_axis_type='datetime',
                  plot_height=500, plot_width=800,
                  title='Kasus Baru',
                  x_axis_label='Tanggal', y_axis_label='Kasus Baru')

# Definisikan y-axis
tot_case.yaxis.formatter = NumeralTickFormatter(format="00")
new_case.yaxis.formatter = NumeralTickFormatter(format="00")

# Definisikan line / proses render line
tot_case.line('Date', 'TotalCases',
              color='green', legend_label='Total Kasus Pulau Sumatera',
              source=sumatera_cds)
tot_case.line('Date', 'TotalCases',
              color='blue', legend_label='Total Kasus Pulau Jawa dan Nusa Tenggara',
              source=jawa_cds)
tot_case.line('Date', 'TotalCases',
              color='black', legend_label='Total Kasus Pulau Kalimantan',
              source=kalimantan_cds)
tot_case.line('Date', 'TotalCases',
              color='yellow', legend_label='Total Kasus Pulau Sulawesi',
              source=sulawesi_cds)
tot_case.line('Date', 'TotalCases',
              color='purple', legend_label='Total Kasus Pulau Papua dan Maluku',
              source=papua_cds)

new_case.line('Date', 'NewCases',
              color='green', legend_label='Kasus Baru Pulau Sumatera',
              source=sumatera_cds)
new_case.line('Date', 'NewCases',
              color='blue', legend_label='Kasus Baru Pulau Jawa dan Nusa Tenggara',
              source=jawa_cds)
new_case.line('Date', 'NewCases',
              color='black', legend_label='Kasus Baru Pulau Kalimantan',
              source=kalimantan_cds)
new_case.line('Date', 'NewCases',
              color='yellow', legend_label='Kasus Baru Pulau Sulawesi',
              source=sulawesi_cds)
new_case.line('Date', 'NewCases',
              color='purple', legend_label='Kasus Baru Pulau Papua dan Maluku',
              source=papua_cds)

# Definisikan legend dengan lokasi atas kiri
tot_case.legend.location = 'top_left'
new_case.legend.location = 'top_left'

# Definisikan tooltips
tooltips3 = [
    ('Pulau', '@Island'),
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@TotalCases'),
]

tooltips4 = [
    ('Pulau', '@Island'),
    ('Tanggal', '@Date{%F}'),
    ('Total Kasus', '@NewCases'),
]

# Masukkan hover ke diagram / figure
tot_case.add_tools(HoverTool(tooltips=tooltips3,
                             formatters={'@Date': 'datetime'}))
new_case.add_tools(HoverTool(tooltips=tooltips4,
                             formatters={'@Date': 'datetime'}))

# Konfigurasi ukuran plot / diagram
tot_case.plot_width = new_case.plot_width = 1000

# Definisikan dua panel berisi total kasus dan kasus baru
tot_case_panel = Panel(child=tot_case, title='Total Kasus')
new_case_panel = Panel(child=new_case, title='Kasus Baru')

# Masukkan panel pada tabs button
tabs2 = Tabs(tabs=[tot_case_panel, new_case_panel])

# Tambahkan judul untuk Figure 1 yaitu Jumlah Kasus Covid-19 di Seluruh Indonesia
html = """<h3>Persebaran Jumlah Kasus Covid-19 Di Indonesia</h3>
<b><i>2020-2021</i>
<br>
"""

# Tambahkan judul untuk Figure 2 yaitu Jumlah Kasus Covid-19 untuk setiap Pulau di Indonesia
html2 = """<h3>Perbandingan Persebaran Jumlah Kasus Covid-19 Di Pulau-Pulau Indonesia</h3>
<b><i>2020-2021</i>
<br>
"""

# Tambahkan spasi satu line
space = "<br>"

sup_title1 = Div(text=html)
sup_title2 = Div(text=html2)
spacing = Div(text=space)

# Lakukan running untuk hasil akhir
curdoc().add_root(column(sup_title1, tabs, spacing, sup_title2, tabs2))
