def push_qualified(students, stack):
    for name, score in students.items():
        if score >= 75:
            stack.append(name)
    return stack


def pop_all(stack):
    items = []
    while stack:
        items.append(stack.pop())
    return items
    


students = {     
        "Vanna": 90, 
        "Tena": 70, 
        "Devi": 75,     
        "Mina": 74, 
        "Sok": 100,
    } 
stack = []

push_qualified(students, stack)
print(stack)   
result = pop_all(stack)           
print(result)             
print(stack)    

#Check and Explain

# Boundary marks
edge_cases = {"A": 74, "B": 75, "C": 76}
s = []
push_qualified(edge_cases, s)
print(s)  # should be ['B', 'C'] — 74 excluded, 75 included

# Empty dictionary
s2 = []
push_qualified({}, s2)
print(s2)  # []

# Nobody qualifies
s3 = []
push_qualified({"X": 50, "Y": 60}, s3)
print(s3)  # []

# Everybody qualifies
s4 = []
push_qualified({"X": 80, "Y": 90}, s4)
print(s4)  # ['X', 'Y']

# Why is 75 an important test? It's the exact boundary the rule is built on
# ("75 or higher qualifies"). Testing it catches an off-by-one bug — if the
# code mistakenly used > instead of >=, a score of exactly 75 would be
# wrongly excluded, and testing only clearly-passing (90) or clearly-failing
# (60) scores would never reveal that mistake.

# What happens when a dictionary key is reused? Dictionary keys must be
# unique — assigning to a key that already exists overwrites the previous
# value rather than keeping both. For example, {"Vanna": 90, "Vanna": 95}
# just becomes {"Vanna": 95}; the first pair is silently discarded
