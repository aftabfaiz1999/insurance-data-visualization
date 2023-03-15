import dash
import dash_bootstrap_components as dbc


from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

Insurance = pd.read_csv('insurance.csv')
sex_value=Insurance['sex'].value_counts()
sex_name=sex_value.keys()
smoker_value=Insurance['smoker'].value_counts()
smoker_name=smoker_value.keys()
region_value=Insurance['region'].value_counts()
region_name=region_value.keys()


app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.H1('Insurance Data Visualization'),
        )
    ]),
    dbc.Row([
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='pie-chart',
                        figure=px.pie(
                    
                            names=sex_name,
                            values=sex_value,
                            hole=.3,
                            title='Gender',
                            color_discrete_sequence=['gold','green'],
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='pie-chart2',
                        figure=px.pie(
                    
                            names=smoker_name,title='Smokers',color_discrete_sequence=['palegoldenrod','navy'],
                            values=smoker_value,
                            hole=.3,
                            
                            template='plotly_dark'
                        )
                    )
                ]),
        
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='pie-chart3',
                        figure=px.pie(
                    
                            names=region_name,values=region_value,title='Regions',color_discrete_sequence=['cadetblue','crimson','darkorchid','darkkhaki'],
                            
                            hole=.3,
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram1',
                        figure=px.histogram(
                    
                            Insurance.age,color_discrete_sequence=['orange'],histnorm='percent',
                            title='Age',
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram2',
                        figure=px.histogram(
                    
                            Insurance['age'],nbins=15,color=Insurance.sex,x='age',title='Age By Gender',color_discrete_sequence=['orange','violet'],histnorm='percent',
                            
                            
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram3',
                        figure=px.histogram(
                    
                            Insurance.children,color_discrete_sequence=['mediumvioletred'],title='Childrens',histnorm='percent',
                            
                            template='plotly_dark'
                        )
                    )
                ])
        ,dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram4',
                        figure=px.histogram(
                    
                            Insurance['smoker'],color=Insurance['sex'],color_discrete_sequence=['mediumvioletred','green'],histnorm='percent',
                            title='Smoker By Gender',
                            template='plotly_dark'
                        )
                    )
                ])
        ,dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram5',
                        figure=px.histogram(
                    
                            Insurance['charges'],color=Insurance['sex'],animation_frame=Insurance['smoker'],color_discrete_sequence=['violet','honeydew'],histnorm='percent',
                            title='Charges For Smokers By Gender',
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='histogram6',
                        figure=px.histogram(
                    
                            Insurance['age'],color=Insurance['sex'],animation_frame=Insurance['smoker'],histnorm='percent',
                            title='Age For Smoker By Gender',
                            template='plotly_dark'
                        )
                    )
                ]),
        dbc.Col(width=6,
            children=[
            dcc.Graph(
                        id='scatter1',
                        figure=px.scatter(
                    
                            Insurance,x="age",y="charges",color="smoker",animation_frame="sex",size="bmi",color_discrete_sequence=['red','dodgerblue'],
                            title='Charges By Smoker , Gender ,Age, BMI',
                            template='plotly_dark'
                        )
                    )
                ]),
    
    ])
])

if __name__ == '__main__':
 app.run_server()
