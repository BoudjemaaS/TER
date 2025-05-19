from graphe import *
from graphe_V3 import *
from graphe_V2 import *
from graphe_V1 import *
import time

graphes = [
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 2) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 2) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 3) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 4) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 5) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 6) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 7) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 8) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 9) % 20}"] for i in range(20)}, "S0"),
Graphe([f"S{i}" for i in range(20)] + ["A"], {**{f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "A": ["S0", "S1"]}, "S0")
]

methodes = [
    "etat_infini_brute_force",
    "etas_infinis_glouton",
    "trouver_cycles"
]

graphes_3 = [
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 2) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 2) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 3) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 4) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 5) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 6) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 7) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 8) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)], {f"S{i}": [f"S{(i + 1) % 20}", f"S{(i + 9) % 20}"] for i in range(20)}, "S0"),
Graphe_3([f"S{i}" for i in range(20)] + ["A"], {**{f"S{i}": [f"S{(i + 1) % 20}"] for i in range(20)}, "A": ["S0", "S1"]}, "S0")
]

methodes_3 = [
    "etat_infini_brute_force_3",
    "etas_infinis_glouton_3",
    "trouver_cycles_3"
]

start_time = time.time()
graphes = [Graphe([f"S{i}" for i in range(10)], {f"S{i}": [f"S{j}" for j in range(10) if j != i] for i in range(10)}, "S0")]
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"{execution_time:.6f} ms")

start_time = time.time()
graphes_3 = [Graphe_3([f"S{i}" for i in range(10)], {f"S{i}": [f"S{j}" for j in range(10) if j != i] for i in range(10)}, "S0")]
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"{execution_time:.6f} ms")

def bench(methode,graphes_list,iteration=5):
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

