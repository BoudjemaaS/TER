import random
import copy

import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import unittest

class Graphe_3:
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

    def supprimer_etat_3(self,etat_a_sup):
        """
        Permet de supprimer un etat, ainsi que les transitions dont il fait partie

        :param etat_a_sup: etat à supprimer
        """

        self.etats.remove(etat_a_sup) #suppression de la liste d'etats

        for etat in self.transitions_sortantes[etat_a_sup]:
            self.transitions_entrantes[etat].remove(etat_a_sup)

        del self.transitions_sortantes[etat_a_sup]

        for etat in self.transitions_entrantes[etat_a_sup]:
            self.transitions_sortantes[etat].remove(etat_a_sup)
            if len(self.transitions_sortantes[etat])==0:  #suppression des puits
                self.supprimer_etat_3(etat)
                del self.transitions_entrantes[etat]

    def trouver_cycles_3(self):
        """
        Permet de trouver les differents cycles present dans un graophe
        :return:
        """
        cycles = []
        for etat in self.etats:
            chemin = [etat]
            visites = {etat}
            pile = [(etat, self.transitions_sortantes[etat],0)]

            while pile:
                sommet, voisins, index = pile.pop()

                if index < len(voisins):
                    voisin = voisins[index]
                    pile.append((sommet, voisins, index + 1))

                    if voisin in chemin:
                        cycles.append(chemin[chemin.index(voisin):])
                    elif voisin not in visites:
                        chemin.append(voisin)
                        visites.add(voisin)
                        pile.append((voisin, self.transitions_sortantes[voisin], 0))
                else:
                    chemin.pop()
                    visites.remove(sommet)

        cycles_uniques = []
        for cycle in cycles:
            cycle_trié = tuple(sorted(cycle))
            if cycle_trié not in [tuple(sorted(c)) for c in cycles_uniques]:
                cycles_uniques.append(cycle)

        return cycles_uniques

    def etats_multi_cycle_3(self):
        """
        Determine les etats presents dans plus d'un cycle

        :return:
        """
        cpt_etat={}
        for etat in self.etats:
            cpt_etat[etat]=0
        for cycle in self.trouver_cycles_3():
            for etat in cycle:
                cpt_etat[etat]+=1

        etat_multi_cycle = [etat for etat, count in cpt_etat.items() if count > 1]
        return etat_multi_cycle

    def etats_dans_cycles_3(self):
        """
        Crée une liste des etats qui forment les cycles
        ex:
            cycles[[1,3,3],[6,8,5],[1,3]]
            return: [1,3,3,5,6,8]
        """

        dico_cycle={}
        for cycle in self.trouver_cycles_3():
            for etat in cycle:
                dico_cycle[etat]=etat

        return list(dico_cycle.keys()) #listes des etats qui forment les cycles

    def visualiser_3(self):
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

    def etat_infini_brute_force_3(self):
        """
        Méthode brute force permettant de trouver, s'il existe, un etat pressent infinimment souvent
        """
        

        etats_a_verifier=self.etats_dans_cycles_3()
        if len(self.etats_multi_cycle_3())!=0:
            etats_a_verifier=self.etats_multi_cycle_3()

        for i in etats_a_verifier:

            # on teste la suppression de chacun des etats, un a un (avec remise)
            temp_graphe=temp_graphe=copy.deepcopy(self)  #on créer une copie du graphe initial
            temp_graphe.supprimer_etat_3(i)                 #pour pouvoir y supprimer un etat

            if len(temp_graphe.trouver_cycles_3())== 0:
                #Il n'y a plus de cycle
                return i

        return "plus de 1 état présent infiniment souvent"

    def etas_infinis_glouton_3(self):
        """
        Algo glouton qui supprime les sommet savec le plus d'arc sortant
        jusqu'a ce qu'il n'y ait plus de cycle

        :return: Les etats presents infinments souvent, determinés
        """



        temp_graphe=copy.deepcopy(self)
        etas_infins=[]

        etats_a_supp = sorted(self.etats_dans_cycles_3(),reverse=True, key=lambda cle: len(self.transitions_sortantes[cle]))

        for etat in etats_a_supp:
            if etat in temp_graphe.etats:
                if temp_graphe.trouver_cycles_3()!=0:
                    #s'il y a encore un cycle

                    temp_graphe.supprimer_etat_3(etat)
                    etas_infins.append(etat)

        return etas_infins




