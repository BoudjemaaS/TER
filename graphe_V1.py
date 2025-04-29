import random
import copy

import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import unittest

class Graphe_1:
    def __init__(self, etats, transitions, etat_ini):
        self.etats = etats  # Liste des états
        self.transitions = transitions  # Dico de transitions: {"A":["B","C"],"B":[],"C":[]}
                                                 #les etats sans transition sortantes sont renseignées
        self.etat_ini = etat_ini #etat initial

    def supprimer_etat_1(self,etat_a_sup):
        """
        Permet de supprimer un etat, ainsi que les transitions dont il fait partie

        :param etat_a_sup: etat à supprimer
        """

        self.etats.remove(etat_a_sup) #On retire l'etat de la liste d'etat

        #if self.etat_ini == etat_a_sup:
            #self.etat_ini = self.etats[random.randint(0,len(self.etats))-1]

        del self.transitions[etat_a_sup] #On retire l'etat  du dico

        for cle, valeurs in self.transitions.items():   #Parcours du dico pour
            if etat_a_sup in valeurs:                    # retirer toute occurence
                valeurs.remove(etat_a_sup)                  # de l'etat

    def visualiser_1(self):
        """
        Permet de créer un objet de type Graphe pour le visualiser_1
        L'état inital est en rouge, le reste des noeuds est bleu
        """

        graphe = nx.DiGraph() #Objet Graphe
        graphe.add_nodes_from(self.etats)  #On y ajoute les etats

        transi = []
        for k in self.transitions.keys():  #On transforme l'ecriture des transitions
            for v in self.transitions[k]:   # {A:[B],B:[C],C:[A]}
                transi.append((k,v))          # |-> [(A,B),(B,C),(C,A)]

        graphe.add_edges_from(transi)    # Ajout au Graphe des transitions
        graphe_colors=['blue']*len(self.etats) #couleur des noeuds
        graphe_colors[self.etats.index(self.etat_ini)]='red' #couleur du noeud initial

        nx.draw(graphe, with_labels=True, font_weight='bold',node_color=graphe_colors) # Visuel du Graphe
        plt.show()

    def trouver_cycles_1(self,etat_actuel="A",etats_visites=[]):
        """
        Permet de determiner si une structure est cyclique ou non
        etat_actuel : la méthode doit etre appelée la premiere fois avec l'état initial
        etat_visités: la méthode doit etre appelée la premiere fois avec une liste vide
        return: True si c'est le cas, False si non
        """

        if len(self.transitions[etat_actuel])==0: # Si aucun voisins, pas de cycle possible
            return False

        if etat_actuel not in etats_visites:
            etats_visites.append(etat_actuel) #On enregistre le chemin parcouru

        else: # on retombe sur un etat deja visité
            return True

        for voisin in self.transitions[etat_actuel]: # Recursion sur les voisins
            if self.trouver_cycles_1(voisin,etats_visites):
                return True

        return False  #On a remonté un arbre, donc pas de cycle

    def etas_infinis_glouton_1(self):
        """
        Méthode brute force permettant de trouver, s'il existe, un etat présent infinimment souvent
        """
        test_sup=0 #nombre d'etat que l'on a supprimé

        for i in self.etats:
            # on teste une suppression de chacun des etats, un a un (avec remise)
            cycle=0 #compteur de cycle en focntion de l'etat initial

            temp_graphe=temp_graphe=copy.deepcopy(self)  #on créer une copie du graphe initial
            temp_graphe.supprimer_etat_1(i)                 #pour pouvoir y supprimer un etat
            for ini in temp_graphe.etats:
                #on verifie la presence d'un cycle pour chaque etat en tant qu'etat initial
                if temp_graphe.trouver_cycles_1(ini,[]):
                    cycle+=1


            if cycle==0:
                #s'il n'y a aucun cycle, alors l'etat en cours est
                #present infiniment souvent
                return i
            else:
                test_sup+=1

            if test_sup==len(self.etats):
                #aucun etat n'est suffisant (par sa suppression)
                #pour rendre le graphe acyclique
                return "plus de 1 état présent infiniment souvent"


