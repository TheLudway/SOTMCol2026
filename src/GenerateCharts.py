import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def graph(dataFile: str, title: str):
    df = pd.read_csv(dataFile)
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%H:%M:%S")

    plt.figure(figsize=(14, 4))

    sns.lineplot(
        data=df,
        x="timestamp",
        y="PM25",
        estimator=None
    )

    plt.title(title, size=15)
    plt.ylabel("PM2.5 (µg/m³)", size=15)
    plt.xlabel("Tiempo", size=15)
    plt.xlim(df["timestamp"].min(), df["timestamp"].max())
    plt.tight_layout()

    # Thresholds for air quality
    ax = plt.gca()
    ax.tick_params(axis='x', labelbottom=False, labelsize=15)
    ax.tick_params(axis='y', labelsize=15)

    maxi_pm25 = df["PM25"].max()
    if (maxi_pm25 >= 0):
        plt.axhspan(0, 12, facecolor="green", alpha=0.2,  label="Buena")
    if (maxi_pm25 >= 12):
        plt.axhspan(12, 37, facecolor="yellow", alpha=0.2, label="Aceptable")
    if (maxi_pm25 >= 37):
        plt.axhspan(37, 55, facecolor="orange", alpha=0.2, label="Dañina a la salud de grupos sensibles")
    if (maxi_pm25 >= 55):
        plt.axhspan(55, 150, facecolor="red",  alpha=0.2, label="Dañina a la salud")
    if (maxi_pm25 >= 150):
        plt.axhspan(150, 250, facecolor="purple",  alpha=0.2, label="Muy dañina a la salud")
    
    plt.legend(fontsize="x-large")
    plt.savefig(f"./img/{title}.svg", format="svg")
