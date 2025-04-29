from graphe import *
import unittest

class TestGraphe(unittest.TestCase):
    def test_1(self):
        graphe1 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["C"]}, "A")
        
        self.assertEqual(set(graphe1.get_etats_dans_cycles()),{"C"})
        self.assertEqual(graphe1.etat_infini_brute_force(),"C")
        self.assertEqual(set(graphe1.etas_infinis_glouton()),{"C"})

        graphe1 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["C"]}, "A")
        # La méthode glouton supprime des états

      

        test_cycles_1=[{"C"}]
        for cycle in range(len(graphe1.cycles)):
            graphe1.cycles[cycle]=set(graphe1.cycles[cycle])
            self.assertTrue(graphe1.cycles[cycle] in test_cycles_1)
        self.assertEqual(len(graphe1.cycles),len(test_cycles_1))
        

    def test_2(self):
        graphe2 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["A"]}, "A")
        
        self.assertEqual(set(graphe2.get_etats_dans_cycles()),{"A","B","C"})
        self.assertTrue(graphe2.etat_infini_brute_force() in ["A" , "B" , "C"])
        self.assertEqual(len(graphe2.etas_infinis_glouton()),1)  

        graphe2 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["A"]}, "A")
        # La méthode glouton supprime des états

        

        test_cycles_2=[{"A","B","C"}]
        for cycle in range(len(graphe2.cycles)):
            graphe2.cycles[cycle]=set(graphe2.cycles[cycle])
            self.assertTrue(graphe2.cycles[cycle] in test_cycles_2)
        self.assertEqual(len(graphe2.cycles),len(test_cycles_2))

    def test_3(self):
        graphe3 = Graphe(["A", "B", "C"], {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, "A")

        self.assertEqual(set(graphe3.get_etats_dans_cycles()),{"A","B","C"})
        self.assertEqual(graphe3.etat_infini_brute_force(),"plus de 1 état présent infiniment souvent")
        self.assertEqual(len(graphe3.etas_infinis_glouton()),2)

        graphe3 = Graphe(["A", "B", "C"], {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, "A")
        # La méthode glouton supprime des états

      

        test_cycles_3=[{"A","B"},{"A","C"},{"B","C"},{"A","B","C"}]
        for cycle in range(len(graphe3.cycles)):
            graphe3.cycles[cycle]=set(graphe3.cycles[cycle])
            self.assertTrue(graphe3.cycles[cycle] in test_cycles_3)
        self.assertEqual(len(graphe3.cycles),len(test_cycles_3))
        



    def test_4(self):
        graphe4 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}, "A")

        self.assertEqual(set(graphe4.get_etats_dans_cycles()),{"A","B","C"})
        self.assertEqual(graphe4.etat_infini_brute_force(),"B")
        self.assertEqual(set(graphe4.etas_infinis_glouton()),{"B"})

        graphe4 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}, "A")
        # La méthode glouton supprime des états

         

        test_cycles_4=[{"B","C"},{"A","B"}]
        for cycle in range(len(graphe4.cycles)):
            graphe4.cycles[cycle]=set(graphe4.cycles[cycle])
            self.assertTrue(graphe4.cycles[cycle] in test_cycles_4)
        self.assertEqual(len(graphe4.cycles),len(test_cycles_4))
        

    def test_5(self):
        graphe5 = Graphe(["A", "B", "C"], {"A": ["C"], "B": ["C"], "C": ["C"]}, "A")

        self.assertEqual(set(graphe5.get_etats_dans_cycles()),{"C"})
        self.assertEqual(graphe5.etat_infini_brute_force(),"C")
        self.assertEqual(set(graphe5.etas_infinis_glouton()),{"C"})

        graphe5 = Graphe(["A", "B", "C"], {"A": ["C"], "B": ["C"], "C": ["C"]}, "A")
        # La méthode glouton supprime des états 

       

        test_cycles_5=[{"C"}]
        for cycle in range(len(graphe5.cycles)):
            graphe5.cycles[cycle]=set(graphe5.cycles[cycle])
            self.assertTrue(graphe5.cycles[cycle] in test_cycles_5)
        self.assertEqual(len(graphe5.cycles),len(test_cycles_5))
        

    def test_6(self):
        graphe6 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C", "A"], "C": ["A"]}, "A")

        self.assertEqual(set(graphe6.get_etats_dans_cycles()),{"A","B","C"})
        self.assertTrue(graphe6.etat_infini_brute_force() in ["A" , "B"])
        self.assertEqual(set(graphe6.etas_infinis_glouton()),{"B"})  

        graphe6 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C", "A"], "C": ["A"]}, "A")
        # La méthode glouton supprime des états

       

        test_cycles_6=[{"A","B"},{"A","B","C"}]
        for cycle in range(len(graphe6.cycles)):
            graphe6.cycles[cycle]=set(graphe6.cycles[cycle])
            self.assertTrue(graphe6.cycles[cycle] in test_cycles_6)
        self.assertEqual(len(graphe6.cycles),len(test_cycles_6))
        

    def test_7(self):
        graphe7 = Graphe(["A", "B"], {"A": ["A", "B"], "B": ["A"]}, "A")

        self.assertEqual(set(graphe7.get_etats_dans_cycles()),{"A","B"})
        self.assertEqual(graphe7.etat_infini_brute_force(),"A")
        self.assertEqual(set(graphe7.etas_infinis_glouton()),{"A"})

        graphe7 = Graphe(["A", "B"], {"A": ["A", "B"], "B": ["A"]}, "A")
        # La méthode glouton supprime des états

     

        test_cycles_7=[{"A"},{"A","B"}]
        for cycle in range(len(graphe7.cycles)):
            graphe7.cycles[cycle]=set(graphe7.cycles[cycle])
            self.assertTrue(graphe7.cycles[cycle] in test_cycles_7)
        self.assertEqual(len(graphe7.cycles),len(test_cycles_7))
        

    def test_8(self):
        graphe8 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["B"]}, "A")

        self.assertEqual(set(graphe8.get_etats_dans_cycles()),{"B","C"})
        self.assertTrue(graphe8.etat_infini_brute_force() in ["B","C"])
        self.assertEqual(len(graphe8.etas_infinis_glouton()),1)

        graphe8 = Graphe(["A", "B", "C"], {"A": ["B"], "B": ["C"], "C": ["B"]}, "A")
        # La méthode glouton supprime des états 

        test_cycles_8=[{"B","C"}]
        for cycle in range(len(graphe8.cycles)):
            graphe8.cycles[cycle]=set(graphe8.cycles[cycle])
            self.assertTrue(graphe8.cycles[cycle] in test_cycles_8)
        self.assertEqual(len(graphe8.cycles),len(test_cycles_8))

        

    def test_9(self):
        graphe9 = Graphe(["A", "B"], {"A": ["A", "B"], "B": ["A", "B"]}, "A")

        self.assertEqual(set(graphe9.get_etats_dans_cycles()),{"A","B"})
        self.assertEqual(graphe9.etat_infini_brute_force(),"plus de 1 état présent infiniment souvent")
        self.assertEqual(len(graphe9.etas_infinis_glouton()),2)

        graphe9 = Graphe(["A", "B"], {"A": ["A", "B"], "B": ["A", "B"]}, "A") 
        #La méthode glouton supprime des états

        test_cycles_9=[{"A"},{"A","B"},{"B"}]
        for cycle in range(len(graphe9.cycles)):
            graphe9.cycles[cycle]=set(graphe9.cycles[cycle])
            self.assertTrue(graphe9.cycles[cycle] in test_cycles_9)
        self.assertEqual(len(graphe9.cycles),len(test_cycles_9))
       
    

        
        

    def test_10(self):
        graphe10 = Graphe(["A", "B", "C", "D"], {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}, "A")

        self.assertEqual(set(graphe10.get_etats_dans_cycles()),{"A","B","C","D"})
        self.assertTrue(graphe10.etat_infini_brute_force() in ["A","B","C","D"])
        self.assertEqual(len(graphe10.etas_infinis_glouton()),1)

        graphe10 = Graphe(["A", "B", "C", "D"], {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]}, "A")
        # La méthode glouton supprime des états

       

        test_cycle_10=[{"A","B","C","D"}]
        for cycle in range(len(graphe10.cycles)):
            graphe10.cycles[cycle]=set(graphe10.cycles[cycle])
            self.assertTrue(graphe10.cycles[cycle] in test_cycle_10)
        self.assertEqual(len(graphe10.cycles),len(test_cycle_10))
        


if __name__ == '__main__':
    unittest.main()