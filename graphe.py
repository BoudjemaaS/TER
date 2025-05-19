import random
import copy

import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import unittest

class Graphe:
    def __init__(self, etats, transitions, etat_ini):
     
        self.etats = etats  # Liste des états
        self.transitions_sortantes = transitions  # Dico de transitions: {"A":["B","C"],"B":[],"C":[]}
                                                 #les etats sans transition sortantes sont renseigné
        self.etat_ini = etat_ini #etat initial
        self.transitions_entrantes =  {etat:[] for etat in etats} 


        for src, dest_list in transitions.items():
            for dest in dest_list:
                self.transitions_entrantes[dest].append(src)
                # On remplit le dictionnaire des transitions entrantes
        
        
        self.cycles=self.trouver_cycles()
        
        self.etats_dans_cycles=self.get_etats_dans_cycles()

    def __eq__(self, other):
        """
        Permet de comparer deux graphes entre eux
        :param other: Graphe à comparer
        :return: True si les graphes sont identiques, False sinon
        """
        return self.etats == other.etats and self.transitions_sortantes == other.transitions_sortantes and self.etat_ini == other.etat_ini

    def __str__(self):
        """
        Permet d'afficher le graphe sous forme de chaine de caractères
        :return: Chaine de caractères représentant le graphe
        """
        return f" etats={self.etats},\n transitions_sortantes={self.transitions_sortantes},\n transitions_entrantes={self.transitions_entrantes},\n etat_ini={self.etat_ini}"

    def visualiser(self):
        """
        Permet de créer un objet de type Graphe pour le visualiser
        L'état inital est en rouge, le reste des noeuds est bleu
        """

        graphe = nx.DiGraph() #Objet Graphe
        graphe.add_nodes_from(self.etats)  #On y ajoute les etats

        transi = []
        for k in self.transitions_sortantes.keys():  #On transforme l'ecriture des transitions
            for v in self.transitions_sortantes[k]:   # {A:[B],B:[C],C:[A]}
                transi.append((k,v))          # |-> [(A,B),(B,C),(C,A)]

        graphe.add_edges_from(transi)    # Ajout au Graphe des transitions
        graphe_colors=['yellow']*len(self.etats) #couleur des noeuds
        graphe_colors[self.etats.index(self.etat_ini)]='red' #couleur du noeud initial

        nx.draw(graphe, with_labels=True, font_weight='bold',node_color=graphe_colors) # Visuel du Graphe
        
        plt.show()

    def trouver_cycles(self):
        """
        Permet de trouver les differents cycles present dans un graophe
        :return:
        """
        cycles = []
        cycles_set = []
            
        chemin = [self.etat_ini] # Liste des etats visités
        pile = [(self.etat_ini, self.transitions_sortantes[self.etat_ini],0)] # Pile pour la recherche en profondeur
        # On initialise la pile avec l'état de départ et ses voisins
        cp=0
        while pile:
            cp+=1
            sommet, voisins, index = pile.pop() 
            
            # l'index permet de savoir quel voisin on est en train d'explorer
            
            if index < len(voisins):# On verifie s'il reste des voisins à explorer
                
                voisin = voisins[index]
                pile.append((sommet, voisins, index + 1))

                if voisin in chemin:
                    # Si le voisin est déjà dans le chemin, on a trouvé un cycle
                    #print(chemin[chemin.index(voisin):])
                    if set(chemin[chemin.index(voisin):]) not in cycles_set:

                        # On ne rajoute le cycle que s'il n'est pas déjà présent
                        
                        cycles.append(chemin[chemin.index(voisin):])
                        cycles_set.append(set(chemin[chemin.index(voisin):]))
                       
                elif voisin not in chemin:
                    # Sinon, le voisin devient le nouvel etat à explorer
                    chemin.append(voisin)
                    pile.append((voisin, self.transitions_sortantes[voisin], 0))

            else:
                chemin.pop()
                # s'il n'y a pas de nouveau voisin a visiter, on depile 
        #print(cp)
        return cycles

    def get_etats_dans_cycles(self):
        """
        Crée une liste des etats qui forment les cycles
        ex:
            cycles[[1,4,3],[6,8,5],[1,3]]
            return: [1,3,4,5,6,8]
        """

        dico_cycle={}
        for cycle in self.cycles:
            # dans chaque cycle 
            for etat in cycle:
                # on ajoute l'etat dans le dico
                dico_cycle[etat]=etat

        return list(dico_cycle.keys()) #listes des etats qui forment les cycles

    def etat_infini_brute_force(self):
        """
        Méthode permettant de renvoyer un état de l'intersection des cycles
        """

        cycles_set=[set(cycle) for cycle in self.cycles]
        # On transforme les cycles en set pour permttre l'intersection


        intersection = set.intersection(*cycles_set)
        # On fait l'intersection de tous les cycles

        if len(intersection)==0: # Si l'intersection est vide
            return "plus de 1 état présent infiniment souvent"
        else:
            return list(intersection)[0]
            #return list(intersection)[random.randint(0,len(intersection)-1)] 
            #on renvoie un etat au hasard parmi ceux trouvés   

    def etas_infinis_glouton(self):
        """
        Algo glouton qui supprime les sommet savec le plus d'arc sortant
        jusqu'a ce qu'il n'y ait plus de cycle

        :return: Les etats presents infinments souvent, determinés
        """
        etats_infinis=[]
        

        while len(self.cycles)!=0:
        #On supprime les cycles jusqu'a ce qu'il n'y en ai plus
            
            # On cherche l'état à supprimer, celui qui a le plus de transitions sortantes
            etat_a_supp=sorted(self.etats_dans_cycles,reverse=True, key=lambda cle: len(self.transitions_sortantes[cle]))[0]
            self.etats_dans_cycles.remove(etat_a_supp)
            #La liste est mise à jour en fonction de la suppression des cycles
                #(si le cycle est supprimé, la liste etat_dans_cycless est réduite)

        
            self.cycles = [cycle for cycle in self.cycles if etat_a_supp not in cycle]


            etats_infinis.append(etat_a_supp)

        return etats_infinis




for _ in range (10):
    Graphe(["1", "2","3"], {"1":["2"],"2":["3"],"3":["1"]},"1").visualiser()
'''

print("2", end=" ")
Graphe(["A", "B"], {"A": ["B"], "B": ["A"]}, "A")
print("3", end=" ")
Graphe(["A", "B", "C"], {"A": ["B","C"], "B": ["A", "C"], "C": ["A", "B"]}, "A")
print("4", end=" ")
Graphe(["A", "B", "C","D"], {"A": ["B","C","D"], "B": ["A", "C","D"], "C": ["A", "B","D"],"D": ["A","B","C"]}, "A")
print("5", end=" ")
Graphe(["A", "B", "C","D","E"], {"A": ["B","C","D","E"], "B": ["A", "C","D","E"], "C": ["A", "B","D","E"],"D": ["A", "B","C","E"],"E": ["A", "B","C","D"]}, "A")

print("#############################")

Graphe(["A", "B"], {"A": ["B", "A"], "B": ["A", "B"]}, "A")
Graphe(["A", "B", "C"], {"A": ["B", "C", "A"], "B": ["A", "C", "B"], "C": ["A", "B", "C"]}, "A")
Graphe(["A", "B", "C", "D"], {"A": ["B", "C", "D", "A"], "B": ["A", "C", "D", "B"], "C": ["A", "B", "D", "C"], "D": ["A", "B", "C", "D"]}, "A")
Graphe(["A", "B", "C", "D", "E"], {"A": ["B", "C", "D", "E", "A"], "B": ["A", "C", "D", "E", "B"], "C": ["A", "B", "D", "E", "C"], "D": ["A", "B", "C", "E", "D"], "E": ["A", "B", "C", "D", "E"]}, "A")

'''