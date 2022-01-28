import dash
from dash import html

app = dash.Dash()

app.layout = html.H1("Hello World!")

if __name__ == "__main__":
    app.run_server()