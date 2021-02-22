import sys
import getopt

from src.structures.graph import Graph
from src.structures.node import Node
from src.structures.edge import Edge

# Options par defaut
DEFAULT_OPTIONS = {
    # chemin vers le fichier d'entree contenant les donnees
    # a traiter
    'i': './source.csv',

    # chemin vers le fichier de sortie contenant
    # les resultats
    'o': './affectation.txt',

    # algorithme a utiliser
    'a': 'kuhn'
}

options = {}

# si le programme est lance
# depuis la ligne de commande
# a l'aide de python main.py
if __name__ == '__main__':
    # on commence par recuperer les arguments
    # -i <chemin_fichier_entree>
    # -o <chemin_fichier_sortie>
    # -a <algorithme>

    try:
        # on enleve le nom du fichier des args
        opts, args = getopt.getopt(sys.argv[1:], 'i:o:a:')

    # au cas ou des options avec arguments manquent d'un argument
    # on redonne la syntaxe de la commande
    except getopt.GetoptError:
        print('Correct syntax: main.py -i <inputfile> -o <outputfile> -a <algorithm>\nExample: main.py -i ./source.csv -o ./output.txt -a kuhn')
        sys.exit(2)

    for opt, arg in opts:
        # on veut traiter les arguments sans le -
        opt = opt.replace('-', '')
        options[opt] = arg

    # on remplace les valeurs par defauts pour les arguments precises
    DEFAULT_OPTIONS.update(options)
    """
    graph = Graph()
    graph.add_node(starting_node=True)

    for i in range(0, 5):
        node = graph.add_node()
        graph.add_edge(graph.starting_node, node)

    print([edge.graph.next_id for edge in graph.starting_node.edges])
    """
    # lancer la recuperation des donnees
    # creer le graph
    # une fois le graph creer traiter le graph avec l'algo
    # une fois le graph traite retranscrire les resultats dans un fichier
