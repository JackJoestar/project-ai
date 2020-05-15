
#@authors: John Hernandez,Naomy Morales, Luis Diaz

from graph import *
from CSV_Parser import *
from csv import DictReader


def main():
    graph = Graph()
    with open('data.csv','r') as csv_file:
        reader = DictReader(csv_file)
        for line in reader:
            if line['first_town'] and line['second_town'] not in graph.get_vertices():
                graph.add_vertex(Vertex(line['first_town']))
                graph.add_vertex(Vertex(line['second_town']))
                graph.add_edge(line['first_town'], line['second_town'], line['distance'], line['speed'])
            
            elif line['first_town'] in graph.get_vertices() and line['second_town'] not in graph.get_vertices():
                graph.add_vertex(Vertex(line['second_town']))
                graph.add_edge(line['first_town'], line['second_town'], line['distance'], line['speed'])
            
            elif line['first_town'] not in graph.get_vertices() and line['second_town'] in graph.get_vertices():
                graph.add_vertex(Vertex(line['first_town']))
                graph.add_edge(line['first_town'], line['second_town'], line['distance'], line['speed'])
            
            else:
                graph.add_edge(line['first_town'], line['second_town'], line['distance'], line['speed'])

        
        graph.print_graph()
            
    

if __name__ == '__main__':
    main()