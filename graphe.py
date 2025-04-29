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
        self.transitions_entrantes =  {}


        for i in self.etats:
            self.transitions_entrantes[i]=[]


        for k in self.etats:
            for v in self.transitions_sortantes.keys():
                if k in self.transitions_sortantes[v]:
                    self.transitions_entrantes[k].append(v)

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
        
        while pile:
            
            sommet, voisins, index = pile.pop() 
            
            # l'index permet de savoir quel voisin on est en train d'explorer
            
            if index < len(voisins):# On verifie s'il reste des voisins à explorer
                
                voisin = voisins[index]
                pile.append((sommet, voisins, index + 1))

                if voisin in chemin:
                    # Si le voisin est déjà dans le chemin, on a trouvé un cycle
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

        intersection = set(self.cycles[0])

        for cycle in self.cycles[1:]:
            # On compare les cycles entre eux
            intersection&= set(cycle)
            # On garde l'intersection des cycles

        if len(intersection)==0: # Si l'intersection est vide
            return "plus de 1 état présent infiniment souvent"
        else:
            return list(intersection)[random.randint(0,len(intersection)-1)] 
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
            etat_a_supp=sorted(self.get_etats_dans_cycles(),reverse=True, key=lambda cle: len(self.transitions_sortantes[cle]))[0]
            
            #La liste est mise à jour en fonction de la suppression des cycles
                #(si le cycle est supprimé, la liste etat_dans_cycless est réduite)

            temp_cycles=copy.deepcopy(self.cycles)
            #on travail sur une copie, pour ne pas modifier la liste que l'on parcourt

            for cycle in self.cycles:

                if etat_a_supp in cycle:
                    # Suppression des cycles comportant l'état à supprimer
                    temp_cycles.remove(cycle)

            self.cycles=temp_cycles
            #mise a jour des cycles restants

            etats_infinis.append(etat_a_supp)

        return etats_infinis



graphe = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["C"]}, "A")
print(graphe.etat_infini_brute_force())



