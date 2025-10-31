# Step 1: Create link matrix (which page is linked to what)
link = [
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0]
]

# Create variables
n = len(link)
damping_factor = 0.85
tolerance = 0.0001

# Create initial PageRank matrix and initialize with 1/n
page_rank = [1.0 / n] * n

# Step 2: Calculate outgoing links for each page
out_going = []
for i in range(n):
    sum_links = 0
    for j in range(n):
        sum_links += link[i][j]
    out_going.append(sum_links)

# Step 3: Calculate PageRank until convergence
convergence = False
iteration = 0

while not convergence:
    new_page_rank = [0.0] * n
    for i in range(n):
        sum_val = 0
        for j in range(n):
            if link[i][j] == 1:
                sum_val += page_rank[j] / out_going[j]
        new_page_rank[i] = (1 - damping_factor) / n + damping_factor * sum_val

    convergence = True
    for i in range(n):
        if abs(new_page_rank[i] - page_rank[i]) > tolerance:
            convergence = False
            break

    page_rank = new_page_rank
    iteration += 1

# Step 4: Print result
print("PageRank after", iteration, "iterations:")
for i in range(n):
    print("Page", i + 1, ":", page_rank[i])