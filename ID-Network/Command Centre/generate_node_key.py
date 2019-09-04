from core.ple_id_tools import generate_new_node_keys

node_id = input("Please provide a name for the node keys")

generate_new_node_keys(node_id=node_id)

print("Done!, Please copy the keys to the correct paths and change config")