
from itertools import product

# Evaluate implication: P -> Q
def implies(p, q):
    return (not p) or q


# Check whether Knowledge Base is true
def check_kb(p, q, r):
    sentence1 = implies(q, p)
    sentence2 = implies(p, not q)
    sentence3 = q or r

    return sentence1 and sentence2 and sentence3


# Truth Table Enumeration Algorithm
def tt_entails(query_function):

    print("\nTruth Table:")
    print("-" * 35)
    print("P\tQ\tR\tKB\tQuery")
    print("-" * 35)

    entailment = True

    for p, q, r in product([False, True], repeat=3):

        kb = check_kb(p, q, r)
        query = query_function(p, q, r)

        # Display T instead of True and F instead of False
        print(
            f"{'T' if p else 'F'}\t"
            f"{'T' if q else 'F'}\t"
            f"{'T' if r else 'F'}\t"
            f"{'T' if kb else 'F'}\t"
            f"{'T' if query else 'F'}"
        )

        if kb and not query:
            entailment = False

    return entailment


# Queries
query1 = lambda p, q, r: r
query2 = lambda p, q, r: implies(r, p)
query3 = lambda p, q, r: implies(q, r)


# Main program
print("1WA24CS217")

print("\nKnowledge Base:")
print("Q -> P")
print("P -> NOT Q")
print("Q OR R")

print("\nChecking KB entails R:")
print("Result:", tt_entails(query1))

print("\nChecking KB entails R -> P:")
print("Result:", tt_entails(query2))

print("\nChecking KB entails Q -> R:")
print("Result:", tt_entails(query3))
