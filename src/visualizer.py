import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:

    def __init__(self, dataframe):
        self.df = dataframe

    def productivity_histogram(self):

        plt.figure(figsize=(8, 5))

        plt.hist(
            self.df["productivity_score"],
            bins=20
        )

        plt.title("Productivity Score Distribution")
        plt.xlabel("Productivity Score")
        plt.ylabel("Frequency")

        plt.savefig("../outputs/graphs/productivity_histogram.png")

        plt.show()

        print("\nHistogram Yorumu:")
        print("Productivity scores are distributed across a wide range.")

    def social_media_vs_productivity(self):

        plt.figure(figsize=(8, 5))

        plt.scatter(
            self.df["social_media_hours"],
            self.df["productivity_score"]
        )

        plt.title("Social Media Usage vs Productivity")
        plt.xlabel("Social Media Hours")
        plt.ylabel("Productivity Score")

        plt.savefig("../outputs/graphs/scatter_plot.png")

        plt.show()

        print("\nScatter Plot Yorumu:")
        print("Social media usage appears weakly related to productivity.")

    def correlation_heatmap(self):

        plt.figure(figsize=(10, 6))

        numeric_df = self.df.select_dtypes(include=["int64", "float64"])

        correlation_matrix = numeric_df.corr()

        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Correlation Heatmap")

        plt.savefig("../outputs/graphs/heatmap.png")

        plt.show()

        print("\nHeatmap Yorumu:")
        print("Some variables show correlations between each other.")