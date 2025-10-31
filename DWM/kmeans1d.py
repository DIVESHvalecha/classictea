import random

def kmeans_1d(arr, k, max_iterations=100):
    # Step 1: Choose K random elements as initial means
    means = random.sample(arr, k)
    
    # Initialize clusters
    clusters = [[] for _ in range(k)]
    
    for _ in range(max_iterations):
        new_clusters = [[] for _ in range(k)]
        
        # Step 2: Assign elements to nearest mean
        for num in arr:
            distances = [abs(num - m) for m in means]
            nearest_mean_index = distances.index(min(distances))
            new_clusters[nearest_mean_index].append(num)
        
        # Step 3: Calculate new means
        new_means = []
        for cluster in new_clusters:
            if cluster:
                new_means.append(sum(cluster) / len(cluster))
            else:
                # If any cluster empty, randomly assign a number again
                new_means.append(random.choice(arr))
        
        # Step 4: Check if clusters did not change (converged)
        if new_clusters == clusters:
            break
        
        clusters = new_clusters
        means = new_means
    
    return clusters, means

# ---- MAIN PROGRAM ----
arr = list(map(int, input("Enter array elements (space separated): ").split()))
k = int(input("Enter number of clusters (k): "))

clusters, means = kmeans_1d(arr, k)

print("\nFinal Clusters:")
for i, c in enumerate(clusters):
    print(f"Cluster {i+1}: {c}")

print("\nCluster Means:")
for m in means:
    print(m)