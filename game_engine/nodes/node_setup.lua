-- node_setup.lua

-- nodes_state
local nodes_state = false

local function setup_nodes()
    print("setting up the nodes...")
    print("setting the node_stats = true...")
    nodes_state = true
    print("node state is now: ", nodes_state)
    print("its true. nice.")
    print("finishing setup. calling beam.lua.")
end

setup_nodes()
