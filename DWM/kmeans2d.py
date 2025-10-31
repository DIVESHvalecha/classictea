import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kmeans_2d(points, k, max_iterations=100):
    # Step 1: Choose k random initial centroids from the points
    centroids = random.sample(points, k)
    
    clusters = [[] for _ in range(k)]
    
    for _ in range(max_iterations):
        new_clusters = [[] for _ in range(k)]
        
        # Step 2: Assign each point to nearest centroid
        for p in points:
            distances = [euclidean_distance(p, c) for c in centroids]
            nearest_index = distances.index(min(distances))
            new_clusters[nearest_index].append(p)
        
        # Step 3: Calculate new centroids (mean of clusters)
        new_centroids = []
        for cluster in new_clusters:
            if cluster:
                x_avg = sum([p[0] for p in cluster]) / len(cluster)
                y_avg = sum([p[1] for p in cluster]) / len(cluster)
                new_centroids.append((x_avg, y_avg))
            else:
                # Handle empty cluster: randomly choose a new point
                new_centroids.append(random.choice(points))
        
        # Step 4: Stop if clusters stop changing (convergence)
        if new_clusters == clusters:
            break
        
        clusters = new_clusters
        centroids = new_centroids
    
    return clusters, centroids

# ---- HARD CODED 2D DATA ----
points = [(2, 3), (3, 4), (5, 8), (6, 7), (8, 3), (7, 2), (4, 9)]
k = 2

clusters, centroids = kmeans_2d(points, k)

print("\nFinal Clusters:")
for i, c in enumerate(clusters):
    print(f"Cluster {i+1}: {c}")

print("\nCentroids:")
for cen in centroids:
    print(cen)

