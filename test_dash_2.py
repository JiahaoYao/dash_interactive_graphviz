import dash
from dash import html, dcc, Output, Input
import dash_interactive_graphviz

# Initialize the Dash app
app = dash.Dash(__name__)

# Initial DOT graph
def generate_dot(selected_node=None):
    color = "red" if selected_node else "black"
    return f"""
    digraph {{
        A [color={color if selected_node == 'A' else 'black'}];
        B [color={color if selected_node == 'B' else 'black'}];
        C [color={color if selected_node == 'C' else 'black'}];
        A -> B;
        B -> C;
        C -> A;
    }}
    """

# Define the layout of the app
app.layout = html.Div([
    dash_interactive_graphviz.DashInteractiveGraphviz(
        id='graph',
        dot_source=generate_dot()
    ),
    html.Div(id='node-output')  # This div will display the clicked node
])

# Callback to update the text component
@app.callback(
    Output('graph', 'dot_source'),
    Input('graph', 'selected_node')
)
def display_selected_node(node):
    return generate_dot(node)



# Run the app
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='8050')
