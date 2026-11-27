
# USN: 1WA24CS217

# Initial Knowledge Base Facts
facts = [
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Missile", "t1"),
    ("Owns", "A", "t1")
]

# Store derivation information
proof = {}
derivation_steps = []


# Display facts in readable format
def display(fact):
    predicate = fact[0]
    arguments = ", ".join(fact[1:])
    return f"{predicate}({arguments})"


# Forward Chaining Algorithm
def forward_chaining():

    global facts

    changed = True

    while changed:
        changed = False

        # Rule 1: American(p) AND Missile(q) AND Owns(r,q)
        #         -> Sells(p,q,r)

        for p in facts:
            if p[0] != "American":
                continue

            for q in facts:
                if q[0] != "Missile":
                    continue

                for r in facts:
                    if r[0] == "Owns" and r[2] == q[1]:

                        new_fact = ("Sells", p[1], q[1], r[1])

                        if new_fact not in facts:
                            substitution = {
                                "p": p[1],
                                "q": q[1],
                                "r": r[1]
                            }

                            premises = [p, q, r]

                            facts.append(new_fact)
                            proof[new_fact] = (
                                "R_sells_by_robert",
                                premises
                            )

                            derivation_steps.append(
                                (new_fact, "R_sells_by_robert",
                                 substitution, premises)
                            )

                            print(
                                f"Derived: {display(new_fact)} "
                                f"by rule R_sells_by_robert "
                                f"with substitution {substitution}"
                            )

                            changed = True

        # Rule 2: Missile(x) -> Weapon(x)

        for f in list(facts):
            if f[0] == "Missile":

                new_fact = ("Weapon", f[1])

                if new_fact not in facts:
                    substitution = {"x": f[1]}
                    premises = [f]

                    facts.append(new_fact)
                    proof[new_fact] = (
                        "R_missile_weapon",
                        premises
                    )

                    derivation_steps.append(
                        (new_fact, "R_missile_weapon",
                         substitution, premises)
                    )

                    print(
                        f"Derived: {display(new_fact)} "
                        f"by rule R_missile_weapon "
                        f"with substitution {substitution}"
                    )

                    changed = True

        # Rule 3: Enemy(x, America) -> Hostile(x)

        for f in list(facts):
            if f[0] == "Enemy" and f[2] == "America":

                new_fact = ("Hostile", f[1])

                if new_fact not in facts:
                    substitution = {"x": f[1]}
                    premises = [f]

                    facts.append(new_fact)
                    proof[new_fact] = (
                        "R_enemy_hostile",
                        premises
                    )

                    derivation_steps.append(
                        (new_fact, "R_enemy_hostile",
                         substitution, premises)
                    )

                    print(
                        f"Derived: {display(new_fact)} "
                        f"by rule R_enemy_hostile "
                        f"with substitution {substitution}"
                    )

                    changed = True

        # Rule 4:
        # American(p) AND Weapon(q) AND Sells(p,q,r)
        # AND Hostile(r) -> Criminal(p)

        for p in list(facts):
            if p[0] != "American":
                continue

            for q in list(facts):
                if q[0] != "Weapon":
                    continue

                for s in list(facts):
                    if s[0] != "Sells":
                        continue

                    if s[1] != p[1] or s[2] != q[1]:
                        continue

                    for h in list(facts):
                        if h[0] == "Hostile" and h[1] == s[3]:

                            new_fact = ("Criminal", p[1])

                            if new_fact not in facts:
                                substitution = {
                                    "p": p[1],
                                    "q": q[1],
                                    "r": s[3]
                                }

                                premises = [p, q, s, h]

                                facts.append(new_fact)
                                proof[new_fact] = (
                                    "R_crime",
                                    premises
                                )

                                derivation_steps.append(
                                    (new_fact, "R_crime",
                                     substitution, premises)
                                )

                                print(
                                    f"Derived: {display(new_fact)} "
                                    f"by rule R_crime "
                                    f"with substitution {substitution}"
                                )

                                changed = True


# Display proof tree
def print_proof(fact, level=0):

    indent = "  " * level

    if fact in proof:
        rule, premises = proof[fact]

        print(
            f"{indent}- {display(fact)} "
            f"[derived by: {rule}]"
        )

        for premise in premises:
            print_proof(premise, level + 1)

    else:
        print(f"{indent}- {display(fact)}")


# Main Program
print("1WA24CS217")

print("\n=== Initial Knowledge Base Facts ===")

for fact in facts:
    print("-", display(fact))


print("\n=== Forward Chaining Derivations ===")

forward_chaining()


print("\n=== Knowledge Base Facts after Forward Chaining ===")

for fact in facts:
    print("-", display(fact))


print("\n=== Derivation Steps ===")

for i, (fact, rule, substitution, premises) in enumerate(
    derivation_steps, 1
):

    print(f"\nStep {i}: rule {rule}")
    print("  substitution:", substitution)

    print("  premises used:")

    for premise in premises:
        print("  -", display(premise))

    print("  derived:", display(fact))


# Query
query = ("Criminal", "Robert")

print("\n=== Query Result ===")

if query in facts:
    print(
        "Query '" + display(query) +
        "' is TRUE (derived)"
    )

    print(
        "\nProof tree for query '" +
        display(query) + "':"
    )

    print_proof(query)

else:
    print(
        "Query '" + display(query) +
        "' is FALSE (not derived)"
    )
