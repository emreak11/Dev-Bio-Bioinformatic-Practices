import numpy as np
from sklearn.decomposition import PCA

genes = [
    "TBXT", "SOX2", "TBX6", "MSGN1",
    "PAX6", "SOX1", "HES7", "GAPDH"
]

cell_ids = np.arange(1, 19)

counts = np.array([
    [ 45,  42,  8,  6,  7,  5, 12,  98],
    [ 16,   9, 78, 64,  3,  2, 35, 112],
    [  5,  65,  3,  2, 52, 46,  3, 105],
    [ 52,  48,  9,  7,  6,  5,  8, 110],
    [ 12,   7, 69, 57,  2,  3, 14,  96],
    [  4,  72,  2,  3, 63, 51,  4, 115],
    [ 39,  44, 12,  8,  9,  6, 17, 101],
    [ 18,  10, 83, 71,  4,  3, 48, 120],
    [  6,  58,  4,  2, 48, 42,  2,  92],
    [ 57,  51, 11,  9,  8,  7, 21, 118],
    [ 14,   8, 73, 62,  3,  2,  9, 103],
    [  3,  69,  2,  1, 59, 55,  3, 108],
    [ 43,  38, 10,  7,  6,  4, 10,  94],
    [ 20,  12, 91, 76,  4,  4, 42, 127],
    [  5,  77,  3,  2, 67, 60,  5, 122],
    [ 49,  46, 15, 11, 10,  8, 15, 109],
    [ 13,   6, 65, 59,  2,  3, 22,  99],
    [  4,  62,  3,  2, 55, 49,  3, 100]
], dtype=float)

library_sizes = np.array([
    4200, 4900, 4500, 4700, 4100, 5100,
    4300, 5300, 3900, 5200, 4400, 4800,
    4000, 5600, 5400, 4600, 4200, 4400
])

# I need to normalize the counts by library before performnig PCA. CPM method will be used.


#normalized_counts = (counts.T / library_sizes).T * 1e6 . This works as well, but I'll use:
normalized_counts = counts / library_sizes[:, np.newaxis] * 1e6
log_normalized_counts=np.log2(normalized_counts + 1)

pca = PCA(n_components=2)
pca_result= pca.fit_transform(log_normalized_counts)

print("Ratio of variance", pca.explained_variance_ratio_)
print("Coordinates", pca_result)
print("Components", pca.components_)

import matplotlib.pyplot as plt

#visualizing the results

plt.scatter(pca_result[:, 0], pca_result[:, 1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA of gene expression")
plt.grid()
plt.show()

for pc_index, component in enumerate(pca.components_):
    print(f"\nPC{pc_index + 1}")

    for gene, loading in zip(genes, component):
        print(f"{gene}: {loading:.3f}")


