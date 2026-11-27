
# USN: 1WA24CS217

import math

print("USN: 1WA24CS217")

# Game Tree
tree = {
    "A": {
        "type": "MAX",
        "children": {
            "B": {
                "type": "MIN",
                "children": {
                    "D": {
                        "type": "MAX",
                        "children": {
                            "L1": 10,
                            "L2": 9
                        }
                    },
                    "E": {
                        "type": "MAX",
                        "children": {
                            "L3": 14,
                            "L4": 18
                        }
                    }
                }
            },
            "C": {
                "type": "MIN",
                "children": {
                    "F": {
                        "type": "MAX",
                        "children": {
                            "L5": 5,
                            "L6": 4
                        }
                    },
                    "G": {
                        "type": "MAX",
                        "children": {
                            "L7": 50,
                            "L8": 3
                        }
                    }
                }
            }
        }
    }
}


# Display Game Tree
print("\nGame Tree Structure:\n")

print("             A (MAX)")
print("            /       \\")
print("       B (MIN)     C (MIN)")
print("       /    \\       /    \\")
print("   D (MAX) E (MAX) F (MAX) G (MAX)")
print("    / \\     / \\    / \\     / \\")
print("   10  9   14 18   5  4   50  3")


# Alpha-Beta Pruning Algorithm
def alpha_beta(node, name, alpha, beta, depth=0):

    indent = "  " * depth

    # Leaf node
    if isinstance(node, int):
        print(indent + "Reached leaf " + name +
              " with value " + str(node))
        return node

    node_type = node["type"]
    children = node["children"]

    print(indent + "Exploring " + node_type +
          " node " + name +
          " (depth=" + str(depth) +
          "), alpha=" + str(alpha) +
          ", beta=" + str(beta))

    if node_type == "MAX":

        value = -math.inf

        for child_name, child_node in children.items():

            print(indent + "--> Exploring child " +
                  child_name + " of " + name)

            child_value = alpha_beta(
                child_node,
                child_name,
                alpha,
                beta,
                depth + 1
            )

            value = max(value, child_value)
            alpha = max(alpha, value)

            print(indent + "Updated MAX node " + name +
                  ": value=" + str(value) +
                  ", alpha=" + str(alpha) +
                  ", beta=" + str(beta))

            # Pruning condition
            if beta <= alpha:
                print(indent +
                      "!!! Pruning at MAX node " + name +
                      " (beta=" + str(beta) +
                      " <= alpha=" + str(alpha) + ")")

                remaining = list(children.keys())
                current_index = remaining.index(child_name)

                for pruned in remaining[current_index + 1:]:
                    print(indent + "!!! Pruned subtree: " + pruned)

                break

        return value

    else:

        value = math.inf

        for child_name, child_node in children.items():

            print(indent + "--> Exploring child " +
                  child_name + " of " + name)

            child_value = alpha_beta(
                child_node,
                child_name,
                alpha,
                beta,
                depth + 1
            )

            value = min(value, child_value)
            beta = min(beta, value)

            print(indent + "Updated MIN node " + name +
                  ": value=" + str(value) +
                  ", alpha=" + str(alpha) +
                  ", beta=" + str(beta))

            # Pruning condition
            if beta <= alpha:
                print(indent +
                      "!!! Pruning at MIN node " + name +
                      " (beta=" + str(beta) +
                      " <= alpha=" + str(alpha) + ")")

                remaining = list(children.keys())
                current_index = remaining.index(child_name)

                for pruned in remaining[current_index + 1:]:
                    print(indent + "!!! Pruned subtree: " + pruned)

                break

        return value


# Main Program
print("\nStarting Alpha-Beta Pruning...\n")

result = alpha_beta(
    tree["A"],
    "A",
    -math.inf,
    math.inf
)

print("\n--------------------------------")
print("Best achievable value at root (A):", result)
print("--------------------------------")
