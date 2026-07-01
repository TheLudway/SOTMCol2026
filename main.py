from src.GenerateCharts import * 

def main():

    graph("./Data/LDU.csv", "Portal El Dorado - Universidades")
    graph("./Data/SM80.csv", "San Mateo - Portal 80")

    plt.show()


if __name__ == "__main__":
    main()
