from graphe import *
from graphe_V3 import *
from graphe_V2 import *
from graphe_V1 import *
import time

graphes = [
Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["C"]}, "A"),
Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["A"]}, "A"),
Graphe(["A", "B", "C"], {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, "A"),
Graphe(["A", "B", "C"], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}, "A"),
Graphe(["A", "B", "C"], {"A": ["C"], "B": ["C"], "C": ["C"]}, "A"),
Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C", "A"], "C": ["A"]}, "A"),
Graphe(["A", "B"], {"A": ["A", "B"], "B": ["A"]}, "A"),
Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["B"]}, "A"),
Graphe(["A", "B"], {"A": ["A", "B"], "B": ["A", "B"]}, "A"),
Graphe(["A", "B", "C", "D"], {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}, "A"),
Graphe([f"S{i}" for i in range(20)] + ["A"], {**{f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "A": ["S0", "S1"]}, "S0")
]

methodes = [
    "etat_infini_brute_force",
    "etas_infinis_glouton",
    "get_etats_dans_cycles",
    "get_etats_multi_cycles",
    "trouver_cycles"
]

graphes_3 = [
Graphe_3(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["C"]}, "A"),
Graphe_3(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["A"]}, "A"),
Graphe_3(["A", "B", "C"], {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, "A"),
Graphe_3(["A", "B", "C"], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}, "A"),
Graphe_3(["A", "B", "C"], {"A": ["C"], "B": ["C"], "C": ["C"]}, "A"),
Graphe_3(["A", "B", "C"], {"A": ["B"], "B": ["C", "A"], "C": ["A"]}, "A"),
Graphe_3(["A", "B"], {"A": ["A", "B"], "B": ["A"]}, "A"),
Graphe_3(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["B"]}, "A"),
Graphe_3(["A", "B"], {"A": ["A", "B"], "B": ["A", "B"]}, "A"),
Graphe_3(["A", "B", "C", "D"], {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}, "A"),
Graphe_3([f"S{i}" for i in range(20)] + ["A"], {**{f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "A": ["S0", "S1"]}, "S0")
]

methodes_3 = [
    "etat_infini_brute_force_3",
    "etas_infinis_glouton_3",
    "etats_dans_cycles_3",
    "etats_multi_cycle_3",
    "trouver_cycles_3"
]

graphes_2 = [
Graphe_2(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["C"]}, "A"),
Graphe_2(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["A"]}, "A"),
Graphe_2(["A", "B", "C"], {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, "A"),
Graphe_2(["A", "B", "C"], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}, "A"),
Graphe_2(["A", "B", "C"], {"A": ["C"], "B": ["C"], "C": ["C"]}, "A"),
Graphe_2(["A", "B", "C"], {"A": ["B"], "B": ["C", "A"], "C": ["A"]}, "A"),
Graphe_2(["A", "B"], {"A": ["A", "B"], "B": ["A"]}, "A"),
Graphe_2(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["B"]}, "A"),
Graphe_2(["A", "B"], {"A": ["A", "B"], "B": ["A", "B"]}, "A"),
Graphe_2(["A", "B", "C", "D"], {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}, "A"),
Graphe_2([f"S{i}" for i in range(20)] + ["A"], {**{f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "A": ["S0", "S1"]}, "S0")
]
methodes_2 = [
    "etat_infini_brute_force_2",
    "etas_infinis_glouton_2",
    "trouver_cycles_2"
]

graphes_1 = [
Graphe_1(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["C"]}, "A"),
Graphe_1(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["A"]}, "A"),
Graphe_1(["A", "B", "C"], {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, "A"),
Graphe_1(["A", "B", "C"], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}, "A"),
Graphe_1(["A", "B", "C"], {"A": ["C"], "B": ["C"], "C": ["C"]}, "A"),
Graphe_1(["A", "B", "C"], {"A": ["B"], "B": ["C", "A"], "C": ["A"]}, "A"),
Graphe_1(["A", "B"], {"A": ["A", "B"], "B": ["A"]}, "A"),
Graphe_1(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["B"]}, "A"),
Graphe_1(["A", "B"], {"A": ["A", "B"], "B": ["A", "B"]}, "A"),
Graphe_1(["A", "B", "C", "D"], {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}, "A"),
Graphe_1([f"S{i}" for i in range(20)] + ["A"], {**{f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "A": ["S0", "S1"]}, "S0")
]
methodes_1 = [
    "etas_infinis_glouton_1",
    "trouver_cycles_1"
]



def bench(methode,graphes_list,iteration=1000):
    start_time = time.time()
    for _ in range(iteration):
        for graphe in graphes_list:
            getattr(graphe, methode)

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print(f"{methode}: {execution_time:.6f} ms")



print("Last version")
for m in methodes:
    bench(m, graphes)
print("\n")



print("Version 3")
for m3 in methodes_3:
    bench(m3, graphes_3)
print("\n")


'''
print("Version 2")
for m2 in methodes_2:
    bench(m2, graphes_2)
print("\n")



print("Version 1")
print("On cherche S'IL Y A un cycle")
for m1 in methodes_1:
    if m1=="trouver_cycles_1":
        bench(m1, graphes_1)
    else:
        bench(m1, graphes_1,1)
print("\n")
'''
