import pandas as pd  # type: ignore
import numpy as np   # type: ignore
import matplotlib.pyplot as plt  # type: ignore


def check_dependencies() -> None:
    """Check if required packages are installed."""
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    packages = {
        "pandas": pd.__version__,
        "numpy": np.__version__,
        "matplotlib": plt.__version__
    }

    for name, version in packages.items():
        print(f"[OK] {name} ({version}) - Ready")


def generate_matrix_data() -> "pd.DataFrame":  # type: ignore
    """Generate simulated Matrix data using numpy."""
    np.random.seed(42)
    n = 1000

    data = {
        "agent_id": np.arange(1, n + 1),
        "signal_strength": np.random.normal(50, 15, n),
        "red_pill_probability": np.random.uniform(0.1, 0.9, n),
        "anomaly_level": np.random.randint(1, 11, n)
    }

    return pd.DataFrame(data)


def analyze_and_visualize() -> None:
    """Analyze data and create visualization."""
    print("\nAnalyzing Matrix data...")
    df = generate_matrix_data()

    print(f"Processing {len(df)} data points...")

    avg_signal = df["signal_strength"].mean()
    high_anomaly = df[df["anomaly_level"] > 7]

    print(f"Average signal strength: {avg_signal:.2f}")
    print(f"High anomaly agents detected: {len(high_anomaly)}")

    plt.figure(figsize=(10, 6))
    plt.scatter(df["signal_strength"], df["red_pill_probability"],
                c=df["anomaly_level"], cmap="viridis", alpha=0.6)
    plt.title("The Matrix - Signal Strength vs Red Pill Probability")
    plt.xlabel("Signal Strength")
    plt.ylabel("Red Pill Probability")
    plt.colorbar(label="Anomaly Level")
    plt.grid(True, alpha=0.3)
    plt.savefig("matrix_analysis.png")
    print("Generating visualization...")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    check_dependencies()
    analyze_and_visualize()
    print("\nAnalysis complete! Welcome to the Real World.")


if __name__ == "__main__":
    main()
