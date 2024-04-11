import math

def distance(city1, city2):
    # Calculate the Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tsp(cities):
    # Start from the first city and build the tour by selecting the nearest neighbor
    num_cities = len(cities)
    unvisited_cities = set(range(1, num_cities))
    tour = [0]  # Start from city 0 (the first city)

    current_city = 0
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(0)  # Return to the starting city to complete the tour
    return tour

def total_distance(tour, cities):
    # Calculate the total distance of the tour
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_dist

if __name__ == "__main__":
    # Example usage
    cities = [(0, 0), (1, 2), (2, 3), (5, 1), (4, 6)]
    tour = nearest_neighbor_tsp(cities)
    total_dist = total_distance(tour, cities)

    print("Optimal Tour Order:", tour)
    print("Total Distance:", total_dist)
