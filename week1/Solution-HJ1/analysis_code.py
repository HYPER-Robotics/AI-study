"""로봇 데이터를 읽어서 time-speed 그래프로 변환함"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def main():
    # Resolve paths relative to this file, regardless of the terminal directory.
    folder = Path(__file__).resolve().parent
    data = pd.read_csv(folder.parent / "robot_log.csv")

    required_columns = {"time_s", "speed_mps"}
    if not required_columns.issubset(data.columns):
        raise ValueError("CSV must contain time_s and speed_mps columns.")
    if data.empty:
        raise ValueError("CSV must contain at least one data row.")

    time = pd.to_numeric(data["time_s"], errors="raise")
    speed = pd.to_numeric(data["speed_mps"], errors="raise")
    for values in (time, speed):
        if values.isna().any() or values.isin([float("inf"), -float("inf")]).any():
            raise ValueError("Time and speed values must be finite numbers.")
    if not time.is_monotonic_increasing:
        raise ValueError("Time values must be in chronological order.")

    duration = time.iloc[-1] - time.iloc[0]
    print(f"Data count: {len(data)}")
    print(f"Recording duration: {duration:g} s")
    # The assignment asks for the arithmetic mean of the recorded samples.
    print(f"Average speed: {speed.mean():.2f} m/s")
    print(f"Maximum speed: {speed.max():.2f} m/s")

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(time, speed, color="tab:blue", marker="o", linewidth=2)
    ax.set_title("Robot Speed over Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Speed (m/s)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    output_path = folder / "speed_plot.png"
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Graph saved to: {output_path}")


if __name__ == "__main__":
    main()
