import sympy as sp

class Component:
    def __init__(self, type, value, connections):
        self.type = type               # Component type ("resistor", "capacitor", "inductor", "voltage_source")
        self.value = value             # Value of the component
        self.connections = connections # List of connected nodes


def identify_nodes(components):
    nodes = set()
    for component in components:
        nodes.update(component.connections)
    return nodes


def create_adjacency_list(components):
    adjacency_list = {}  # Dictionary to store node relationships

    for component in components:
        node1, node2 = component.connections
        component_type = component.type
        value = component.value

        # Calculate impedance based on component type
        if component_type == "resistor":
            impedance = str(value)  # Ohms
        elif component_type == "capacitor":
            impedance = f"1/(s*{value})"  # 1 / (sC)
        elif component_type == "inductor":
            impedance = f"s*{value}"      # sL
        elif component_type == "voltage_source":
            impedance = "0"               # Ideal voltage source has zero impedance
        else:
            raise ValueError("Unknown component type")

        # Update adjacency list with impedance information
        if node1 not in adjacency_list:
            adjacency_list[node1] = {}
        if node2 not in adjacency_list:
            adjacency_list[node2] = {}

        adjacency_list[node1][node2] = (component_type, impedance)
        adjacency_list[node2][node1] = (component_type, impedance)

    return adjacency_list


def solve_kcl(adjacency_list, components, ground_node):
    nodes = set(adjacency_list.keys())
    voltages = {}

    # Define voltage symbols for each node
    for node in nodes:
        if node != ground_node:
            voltages[node] = sp.symbols(f"V_{node}")  # Define voltage symbols

    # Find voltage source to set ground and source nodes
    pos_node, neg_node, voltage_value = -1, -1, 0
    for component in components:
        if component.type == "voltage_source":
            pos_node, neg_node = component.connections
            voltage_value = component.value
            break

    if pos_node == -1 or neg_node == -1:
        raise ValueError("Circuit must contain a voltage source.")

    # Assign ground node and voltage source node
    voltages[ground_node] = 0  # Ground node voltage is 0
    voltages[pos_node] = sp.symbols("V_source")  # Voltage source as a symbolic variable

    # Create KCL equations
    equations = []

    for node in nodes:
        if node == ground_node or node == pos_node:
            continue

        node_equation = 0
        for neighbor_node, (comp_type, impedance) in adjacency_list[node].items():
            current_expr = (voltages[node] - voltages[neighbor_node]) / sp.sympify(impedance)
            node_equation += current_expr

        equations.append(sp.Eq(node_equation, 0))  # KCL equation: sum of currents = 0

    # Solve the system of equations
    solution = sp.linsolve(equations, *voltages.values())
    results = {str(voltage): sol for voltage, sol in zip(voltages.values(), solution.args[0])}

    return results  # Return solution as a dictionary
