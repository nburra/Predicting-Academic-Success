"""
Names: Noah Burra, Ethan Xin, Vaunshal Sariaya, Rocky Lin
DS2000
Description: Predicting students academic success based on Admission Grade and First Semester GPA.
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import skew, kendalltau


def read_file(filename, location_1, location_2):
    """
    Parses the data file and returns two lists of the columns specified by the user.

    Parameters
    ----------
    filename : str
        The data CSV file.
    location_1 : int
        The column number for the first data set.
    location_2 : int
        The column number for the second data set.

    Returns
    -------
    final : list of lists
        A list containing two lists with data from the specified columns.
    """
    with open(filename, "r") as file:
        file.readline()  # Skip the header
        var1, var2 = [], []

        for line in file:
            vals = line.strip().split(";")
            var1.append(float(vals[location_1]))
            var2.append(float(vals[location_2]))

    return [var1, var2]


def plot_whole(data):
    """
    Plots all values in the data set with a regression line.

    Parameters
    ----------
    data : list of lists
        The data to be plotted.

    Returns
    -------
    None
    """
    plt.scatter(data[1], data[0], marker=".", color="black")
    plt.plot(np.unique(data[1]), np.poly1d(np.polyfit(data[1], data[0], 1))(np.unique(data[1])), linewidth=4, label="Regression Line")
    plt.xlabel("Admission Grade")
    plt.ylabel("GPA First Semester")
    plt.title("First Sem. GPA to Admission Grade")
    plt.legend()
    plt.savefig("project.png")
    plt.show()


def plot_focused_1(data):
    """
    Plots a focused view of the data from x values 100-130.

    Parameters
    ----------
    data : list of lists
        The data to be plotted.

    Returns
    -------
    None
    """
    plt.scatter(data[1], data[0], marker=".", color="black")
    plt.plot(np.unique(data[1]), np.poly1d(np.polyfit(data[1], data[0], 1))(np.unique(data[1])), linewidth=4, label="Regression Line")
    plt.xlim(100, 130)
    plt.ylim(10, 20)
    plt.xlabel("Admission Grade (100-130)")
    plt.ylabel("GPA First Semester")
    plt.title("First Sem. GPA to Admission Grade Focused (100-130)")
    plt.legend()
    plt.savefig("project_focused_100-130.png")
    plt.show()


def plot_focused_2(data):
    """
    Plots a focused view of the data from x values 120-200.

    Parameters
    ----------
    data : list of lists
        The data to be plotted.

    Returns
    -------
    None
    """
    plt.scatter(data[1], data[0], marker=".", color="black")
    plt.plot(np.unique(data[1]), np.poly1d(np.polyfit(data[1], data[0], 1))(np.unique(data[1])), linewidth=4, label="Regression Line")
    plt.xlim(120, 200)
    plt.ylim(10, 20)
    plt.xlabel("Admission Grade (120-200)")
    plt.ylabel("GPA First Semester")
    plt.title("First Sem. GPA to Admission Grade Focused (120-200)")
    plt.legend()
    plt.savefig("project_focused_120-200.png")
    plt.show()


def statistics(data):
    """
    Provides detailed statistical analysis of the data.

    Parameters
    ----------
    data : list of lists
        The data to be analyzed.

    Returns
    -------
    None
    """
    admission_grade = data[1]
    gpa = data[0]
    
    #statistical caluclations for admission grade data set
    mean_admin = np.mean(admission_grade) #citation 1
    sem_admin = stats.sem(admission_grade) #citation 2
    median_admin = np.median(admission_grade) #citation 1
    con_intv_admin = stats.t.interval(0.95, len(data) - 1, loc = mean_admin, scale = sem_admin) #citation 2
    skew1 = skew(admission_grade) #citation 2
    
    #statistical calculations for GPA data set
    mean_gpa = np.mean(gpa) #citation 1
    sem_gpa = stats.sem(gpa) #citation 2
    median_gpa = np.median(gpa) #citation 1
    con_intv_gpa = stats.t.interval(0.95, len(data) - 1, loc = mean_gpa, scale = sem_gpa) #citation 2
    skew2 = skew(gpa) #citation 2
    
   
    #prinitng results for both
    print("Skew of Admission Grade:" , skew1)
    print("Sample mean for Admission Grade: ", mean_admin )
    print("95% Confidence interval for Admission Grade: ", con_intv_admin)
    print("Median for Admission Grade:", median_admin)
    
    #prinitng blank line to seperate both stats
    print("")
    
    
    print("Skew of GPA", skew2)
    print("Sample mean for GPA: ", mean_gpa)
    print("95% Confidence interval for GPA: ", con_intv_gpa)
    print("Median for GPA:", median_gpa)

    
    correlation_coefficient, p_value = kendalltau(admission_grade, gpa) #citation 2
    
    print(correlation_coefficient, p_value)


def main():
    data = read_file("data.csv", 25, 12)
    plot_whole(data)
    plot_focused_1(data)
    plot_focused_2(data)
    statistics(data)



main()
