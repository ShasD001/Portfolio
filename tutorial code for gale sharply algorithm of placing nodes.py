import numpy as np

# Example dataset: WiFi nodes and city areas ranked by preference
wifi_nodes = ["Node_A", "Node_B", "Node_C"]
city_areas = ["Area_1", "Area_2", "Area_3"]

# Preference rankings (higher means more desirable)
wifi_preferences = {
    "Node_A": ["Area_1", "Area_2", "Area_3"],
    "Node_B": ["Area_2", "Area_3", "Area_1"],
    "Node_C": ["Area_3", "Area_1", "Area_2"]
}

area_preferences = {
    "Area_1": ["Node_B", "Node_A", "Node_C"],
    "Area_2": ["Node_A", "Node_C", "Node_B"],
    "Area_3": ["Node_C", "Node_B", "Node_A"]
}

# Gale-Shapley Algorithm
def stable_matching(wifi_preferences, area_preferences):
    free_nodes = list(wifi_preferences.keys())
    matches = {}
    proposals = {node: 0 for node in free_nodes}  # Track proposals count

    while free_nodes:
        node = free_nodes[0]
        preferred_area = wifi_preferences[node][proposals[node]]
        proposals[node] += 1

        if preferred_area not in matches:
            matches[preferred_area] = node
            free_nodes.pop(0)
        else:
            current_node = matches[preferred_area]
            if area_preferences[preferred_area].index(node) < area_preferences[preferred_area].index(current_node):
                matches[preferred_area] = node
                free_nodes.pop(0)
                free_nodes.append(current_node)

    return matches

# Run the algorithm
result = stable_matching(wifi_preferences, area_preferences)

# Display results
print("Optimal Node Placements:")
for area, node in result.items():
    print(f"{area} → {node}")