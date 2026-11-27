
# USN: 1WA24CS217

print("USN: 1WA24CS217")

# STEP 1: Knowledge Base / Given Premises
print("\n=== STEP 1: Knowledge Base / Given Premises ===")

premises = [
    "a. For all x: food(x) -> likes(John, x)",
    "b. food(Apple) AND food(Vegetables)",
    "c. For all x, y: eats(x, y) AND NOT killed(x) -> food(y)",
    "d. eats(Anil, Peanuts) AND alive(Anil)",
    "e. For all x: eats(Anil, x) -> eats(Harry, x)",
    "f. For all x: NOT killed(x) -> alive(x)",
    "g. For all x: alive(x) -> NOT killed(x)",
    "h. likes(John, Peanuts)"
]

for p in premises:
    print(p)


# STEP 2: Remove Implications
print("\n=== STEP 2: After Removing Implications ===")

clauses = [
    "a. NOT food(x) OR likes(John, x)",
    "b1. food(Apple)",
    "b2. food(Vegetables)",
    "c. NOT eats(x, y) OR killed(x) OR food(y)",
    "d1. eats(Anil, Peanuts)",
    "d2. alive(Anil)",
    "e. NOT eats(Anil, x) OR eats(Harry, x)",
    "f. killed(x) OR alive(x)",
    "g. NOT alive(x) OR NOT killed(x)"
]

for c in clauses:
    print(c)


# STEP 3: Standardize Variables
print("\n=== STEP 3: Standardized Variables ===")

standardized = [
    "a. NOT food(x) OR likes(John, x)",
    "b1. food(Apple)",
    "b2. food(Vegetables)",
    "c. NOT eats(y, z) OR killed(y) OR food(z)",
    "d1. eats(Anil, Peanuts)",
    "d2. alive(Anil)",
    "e. NOT eats(Anil, w) OR eats(Harry, w)",
    "f. killed(g) OR alive(g)",
    "g. NOT alive(k) OR NOT killed(k)"
]

for c in standardized:
    print(c)


# STEP 4: Drop Universal Quantifiers
print("\n=== STEP 4: After Dropping Universal Quantifiers ===")

for c in standardized:
    print(c)


# STEP 5: Negate the Query
print("\n=== STEP 5: Negation of Query ===")

print("Original Query: likes(John, Peanuts)")
print("Negated Query: NOT likes(John, Peanuts)")


# STEP 6: Resolution
print("\n=== STEP 6: Resolution Steps ===")

print("\nClause 1:")
print("NOT food(x) OR likes(John, x)")

print("\nClause 2:")
print("food(Peanuts)")

print("\nSubstitution: x = Peanuts")
print("Resolvent 1: likes(John, Peanuts)")


print("\nClause 3:")
print("NOT eats(y, z) OR killed(y) OR food(z)")

print("\nClause 4:")
print("eats(Anil, Peanuts)")

print("\nSubstitution: y = Anil, z = Peanuts")
print("Resolvent 2: killed(Anil) OR food(Peanuts)")


print("\nClause 5:")
print("NOT alive(k) OR NOT killed(k)")

print("\nClause 6:")
print("alive(Anil)")

print("\nSubstitution: k = Anil")
print("Resolvent 3: NOT killed(Anil)")


print("\nResolving:")
print("killed(Anil) OR food(Peanuts)")
print("NOT killed(Anil)")
print("Resolvent 4: food(Peanuts)")


print("\nResolving:")
print("likes(John, Peanuts)")
print("NOT likes(John, Peanuts)")
print("Resolvent 5: EMPTY CLAUSE (NIL)")


# FINAL RESULT
print("\n=== FINAL RESULT ===")

print("Empty Clause (NIL) obtained.")
print("Contradiction found.")
print("Therefore, the query is PROVED.")

print("\nQuery: likes(John, Peanuts)")
print("Result: TRUE (PROVED BY RESOLUTION)")
