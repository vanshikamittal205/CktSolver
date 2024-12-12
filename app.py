from flask import Flask, request, render_template
from kclsolve import create_adjacency_list, solve_kcl, Component

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Get user input
        components_data = request.form.get('components')
        ground_node = int(request.form.get('ground_node'))

        # Parse components
        components = []
        for line in components_data.strip().split('\n'):
            comp_type, value, node1, node2 = line.split(',')
            components.append(Component(comp_type, float(value), [int(node1), int(node2)]))

        # Create adjacency list
        adjacency_list = create_adjacency_list(components)

        # Solve circuit
        solution = solve_kcl(adjacency_list, components, ground_node)

        return render_template('index.html', solution=solution)

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
