from collections import Counter

def process_ranges_and_queries(arr, queries):
    # Step 1: Compute all point counts
    point_counts = Counter()
    for start, end in arr:
        for i in range(start, end + 1):
            point_counts[i] += 1

    # Step 2: Aggregate counts by their values
    counts = {}
    for key, value in point_counts.items():
        if value not in counts:
            counts[value] = 1
        else:
            counts[value] += 1

    print("Counts:", counts)  # Displays counts of counts
    # Step 3: Process queries to find maximum count in each range
    results = []
    for start, end in queries:
        max_count = 0
        for i in range(start, end + 1):
            if i in counts:
                max_count = max(max_count, counts[i])
        results.append(max_count)

    return results

# Example usage
arr = [(2, 3), (3, 4), (5, 5), (3, 4)]
queries = [(1, 2), (3, 4)]
results = process_ranges_and_queries(arr, queries)
print("Query Results:", results)  # Displays maximum counts for each query range
