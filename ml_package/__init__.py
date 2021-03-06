# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# python setup.py sdist

# Basic
import warnings
warnings.filterwarnings('ignore') # supress warnings

from IPython.display import HTML, display, Markdown, clear_output

import sklearn
from sklearn import preprocessing

import pandas as pd

## Adjusting display setttings

pd.set_option('display.max_columns', None) # Displaying all the columns in the dataset
pd.set_option('max_colwidth', None) # Displaying entire contents of columns
pd.set_option("max_rows", 100) # Displaying all rows
pd.set_option('max_seq_item', None) # Displaying everything in the list in the dataframe
pd.set_option('precision', 2) # Displaying precision to just 2 decimal places


# Reading any file
def read(path, sep = ',', col = None, row = None, type = None):
    return pd.read_table(filepath_or_buffer = path, sep= sep, usecols= col, nrows= row, dtype= type)


## Treating Categorical Data

# One Hot Encoding
def ohe_prep(main_data, col_ohe, prefx):
    bridge_df = main_data[[col_ohe]]
    # generate binary values using get_dummies
    dum_df = pd.get_dummies(bridge_df, columns=[col_ohe], prefix=[prefx] )
    # merge with main df bridge_df on key values
    del main_data[col_ohe]
    return main_data.join(dum_df)
def ohe(df, col):
  for i in col:
    df = ohe_prep(df,i,i)
  return df

# Label Encoding
def le():
  return preprocessing.LabelEncoder()


## Normalising Data

# Using min-max scaler
def norm(x_train, x_test):
    min_max_scaler = preprocessing.MinMaxScaler()
    x_train_scaled = min_max_scaler.fit_transform(x_train.values)
    out = []
    out.append(x_train_scaled)
    for i in x_test:
        out.append(min_max_scaler.transform(i.values))
    return out


## Hide your Code with a button

# HTML script to hide code in one button
def hide_code():
    return HTML('''<script>
            code_show=true; 
            function code_toggle() {
             if (code_show){
             $('div.input').hide();
             } else {
             $('div.input').show();
             }
             code_show = !code_show
            } 
            $( document ).ready(code_toggle);
            </script>
            <form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')
display(HTML("""
<style>
.output_png img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
 
.loader {
  border: 5px solid #f3f3f3;
  border-radius: 50%;
  border-top: 5px solid teal;
  border-right: 5px solid grey;
  border-bottom: 5px solid maroon;
  border-left: 5px solid tan;
  width: 20px;
  height: 20px;
  -webkit-animation: spin 1s linear infinite;
  animation: spin 1s linear infinite;
  float: left;`
}

@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>
"""))


## Add a rotating loading icon

def load_icon(): 
    return display(Markdown('<div><div class="loader"></div><h3>&nbsp;LOADING</h3></div>'))






# # enabling bokeh plots to be rendered in HTML report

# from jinja2 import Template
# from bokeh.embed import components

# html_plot = Template("""
# <!DOCTYPE html>
# <html lang="en-US">

# <link
#     href="http://cdn.pydata.org/bokeh/release/bokeh-1.4.0.min.css"
#     rel="stylesheet" type="text/css"
# >
# <script src="http://cdn.pydata.org/bokeh/release/bokeh-1.4.0.min.js"></script>
# <script src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-1.4.0.min.js"></script>
# <script src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-1.4.0.min.js"></script>

# <body>
#     {{ script }}
#     {{ div }}
# </body>

# </html>
# """)



# # The code in the following cell is a function that will help to display dataframes using Plotly with scrollable rows
# import plotly.graph_objects as go


# def display_data(data_table, sel_col=None):
#     data_table_series = [data_table[i] for i in data_table.columns]
    
#     cell_color = []
#     n = len(data_table)
#     for col in data_table.columns:
#         if sel_col is None:
#             cell_color.append(['rgba(0,191,255,0.5)']*n)
#         else:
#             if col!=sel_col:
#                 cell_color.append(['rgba(0,191,255,0.5)']*n)
#             else:
#                 cell_color.append(['paleturquoise']*n)

#     fig = go.Figure(data=[go.Table(
#         header=dict(values=list(data_table.columns),
#                     fill_color='grey',
#                     align='center',
#                     font=dict(color='white', size=15)
#                    ),
#         cells=dict(values=data_table_series,
#                    fill_color=cell_color,
#                    align='center',
#                    font=dict(color='black', size=10)
#                   ))
#     ])

#     if data_table.shape[0] == 1:
#         fig_ht = 75
#     elif data_table.shape[0] >= 2 and data_table.shape[0] <= 9:
#         fig_ht = 40*data_table.shape[0]
#     else:
#         fig_ht = 400
    
#     fig.update_layout(width=150*len(data_table.columns), 
#                       height=fig_ht,
#                       margin=dict(l=0,r=0,b=0,t=0,pad=0))
#     fig.show(config={'displaylogo': False})