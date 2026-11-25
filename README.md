# Dev-Bio-Bioinformatic-Practices
I am trying to solve different biological problems using Python to deepen my understanding of quantitative developmental biology. The problems are created by AI, and my aim is to construct a solid understanding in this area by using different tools and mathematical approaches.


My plan is to write down what I've learned from each problem, and sometimes the problems themselves.





 🎯 ***Problem 1) Principal Component Analysis (PCA)***

PCA is a widely used method to reduce the size of the dataset while preserving the variance. PCA does not simply reduce the size of a dataset. It reduces its dimensionality by constructing new axes that capture the greatest possible variance.

-I've performed a CPM normalization followed by a log transform.
-After pre-processing the data, I've performed the PCA and scattered the point.
-Positive and negative component values do not necessarly mean negative variance or negative expression, it give us the relative postiion of the component.
-We sum PC1 and PC2 to see how much of the varinace is preserved in the reduced-dataset. 
-Genes with large absolute component coefficients can help explain why cells separate along a principal component. However, PCA alone cannot establish cell identity or developmental trajectories.
-PCA is sensitive to outliers and doesn't necessarily preserve importana biological information.
