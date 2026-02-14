# Nagpur Metro Route and Cost using Graph


import heapq
from collections import defaultdict


class MetroGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_connection(self, src, dest, distance=1):
        self.graph[src].append((dest, distance))
        self.graph[dest].append((src, distance))

    def dijkstra(self, source, destination):
        heap = [(0, source)]
        distances = {station: float('inf') for station in self.graph}
        previous = {}
        distances[source] = 0

        while heap:
            current_distance, current_station = heapq.heappop(heap)
            if current_station == destination:
                break
            for neighbor, weight in self.graph[current_station]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_station
                    heapq.heappush(heap, (new_distance, neighbor))

        path = self._reconstruct_path(previous, source, destination)
        return path

    def _reconstruct_path(self, previous, source, destination):
        path = []
        current = destination
        while current != source:
            path.append(current)
            current = previous.get(current)
            if current is None:
                return []

        path.append(source)
        path.reverse()
        return path


def calculate_cost_by_stations(stations):
    if stations <= 3:
        return 10
    elif stations <= 9:
        return 20
    elif stations <= 14:
        return 30
    else:
        return 35

def nagpur_metro_station():
    metro = MetroGraph()
    stations = [
        "Prajapati Nagar",
        "Vaishnodevi Square",
        "Ambedkar Square",
        "Telephone Exchange",
        "Chitar Oli Chowk",
        "Agrasen Square",
        "Dosar Vaishya Square",
        "Nagpur Railway Station",
        "Cotton Market",
        "Sitabuldi",
        "Jhansi Rani Square",
        "Institution of Engineers",
        "Shankar Nagar Square",
        "LAD Square",
        "Dharampeth College",
        "Subhash Nagar",
        "Rachana Ring Road Junction",
        "Vasudev Nagar",
        "Bansi Nagar",
        "Lokmanya Nagar"
    ]

    for station in stations:
        metro.graph[station]
    for i in range(len(stations) - 1):
        metro.add_connection(stations[i], stations[i + 1])
    return metro

def main():
    metro = nagpur_metro_station()
    print("\nNAGPUR METRO ROUTE\n")
    print("Available Stations:")
    for station in metro.graph:
        print("#", station)
    source = input("\nEnter Source Station: ").strip()
    destination = input("Enter Destination Station: ").strip()

    if source not in metro.graph or destination not in metro.graph:
        print("\nInsert valid station")
        return

    path = metro.dijkstra(source, destination)
    if not path:
        print("\nNo route found.")
        return

    stations_travelled = len(path) - 1
    fare = calculate_cost_by_stations(stations_travelled)

    print("\nSHORTEST METRO ROUTE")
    print(" -> ".join(path))
    print(f"\nStations Travelled : {stations_travelled}")
    print(f"Cost : ₹{fare}")
    print("\n")

if __name__ == "__main__":
    main()
