import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# def fit_choose_for_potentialfind_force ( res_sliced_data_minima[0], res_sliced_data_minima[1], gaussian, lorentzian, polynomial):
# def fit_choose_for_potentialfind_force ( distance,potential, gaussianfit, lorentzianfit, polynomialfit,degree_poly):

def fit_choose_for_potentialfind_force ( res_sliced_data_minima, gaussianfit, lorentzianfit, polynomialfit,degree_poly):

    
    """

    sliced data , whatever you give, it will work on it.
    best_fitted --> will be the fit for the potential
    gradient --> force after differentiating the best_fitted(i.e. potential)
    By the default all are None, whichever you want to choose make it one.

    """

    def gaussian(x, a, b, c):
        return a * np.exp(-0.5 * ((x - b) / c) ** 2)

    def lorentzian(x, a, b, c):
        return a / (1 + ((x - b) / c) ** 2)

    def polynomial(x, *coeffs):
        return np.polyval(coeffs, x)

    def chi_square(y_obs, y_exp):
        return np.sum((y_obs - y_exp) ** 2 / y_exp)

    # data = pd.read_csv('smooth_data.csv')  # Extract distance and potential columns
    # print(data.head())

    distance =   res_sliced_data_minima[0]
    potential =  res_sliced_data_minima[1]
  

    # Check for and remove NaN or infinite values
    mask = np.isfinite(distance) & np.isfinite(potential)
    distance = distance[mask]
    potential = potential[mask]

    # Initial guesses for the parameters
    initial_gaussian = [max(potential), np.mean(distance), np.std(distance)]
    initial_lorentzian = [max(potential), np.mean(distance), np.std(distance)]
    # degree = 8  # Polynomial degree
    degree = degree_poly  # Polynomial degree

    # Initialize chi-square values
    chi2_gaussian = np.inf
    chi2_lorentzian = np.inf
    chi2_polynomial = np.inf

    # Fit the data 
    if gaussianfit is not None:
        try:
            popt_gaussian, _ = curve_fit(gaussian, distance, potential, p0=initial_gaussian)
            fitted_gaussian = gaussian(distance, *popt_gaussian)
            chi2_gaussian = chi_square(potential, fitted_gaussian)
            print(f"Gaussian: {chi2_gaussian}")
        except RuntimeError as e:
            print(f"Gaussian fit failed: {e}")
            chi2_gaussian = np.inf
            print(f"Gaussian: {chi2_gaussian}")

    if lorentzianfit is not None:
        try:
            popt_lorentzian, _ = curve_fit(lorentzian, distance, potential, p0=initial_lorentzian)
            fitted_lorentzian = lorentzian(distance, *popt_lorentzian)
            chi2_lorentzian = chi_square(potential, fitted_lorentzian)
            print(f"Lorentzian: {chi2_lorentzian}")
        except RuntimeError as e:
            print(f"Lorentzian fit failed: {e}")
            chi2_lorentzian = np.inf
            print(f"Lorentzian: {chi2_lorentzian}")

    if polynomialfit is not None:
        try:
            popt_polynomial, _ = curve_fit(lambda x, *params: polynomial(x, *params), distance, potential, p0=[1]*(degree+1))
            fitted_polynomial = polynomial(distance, *popt_polynomial)
            chi2_polynomial = chi_square(potential, fitted_polynomial)
        except RuntimeError as e:
            print(f"Polynomial fit failed: {e}")
            chi2_polynomial = np.inf
            print(f"Polynomial: {chi2_polynomial}")

    # Determine the best fit if allfit are enabled. ------------------------------------------------------------->
    if gaussianfit and lorentzianfit and polynomialfit is not None:  
        # print the all values when you enable all the fit otherwise it will not print any value.
        chi2_values = {
            'Gaussian': chi2_gaussian,
            'Lorentzian': chi2_lorentzian,
            'Polynomial': chi2_polynomial
        }

        best_fit = min(chi2_values, key=chi2_values.get)
        print(f"Best fit: {best_fit}")

        plt.figure(figsize=(10, 6))
        plt.scatter(distance, potential, label='Data', s=10, color='black')

        if chi2_gaussian != np.inf:
            plt.plot(distance, fitted_gaussian, label='Gaussian Fit', color='red')
        if chi2_lorentzian != np.inf:
            plt.plot(distance, fitted_lorentzian, label='Lorentzian Fit', color='blue')
        if chi2_polynomial != np.inf:
            plt.plot(distance, fitted_polynomial, label=f'Polynomial Fit (degree {degree})', color='green')
        plt.xlabel('Distance')
        plt.ylabel('Potential')
        plt.title('Fit Comparison')
        plt.legend()
        plt.show()
        # Calculate and plot the gradient of the best fit
        if best_fit == 'Gaussian':
            best_fitted = fitted_gaussian
        elif best_fit == 'Lorentzian':
            best_fitted = fitted_lorentzian
        else:
            best_fitted = fitted_polynomial

        gradient = -np.gradient(best_fitted, distance)

        plt.figure(figsize=(10, 6))
        plt.plot(distance, gradient, label='Gradient of Best Fit', color='red') # color='purple'
        plt.xlabel('Distance')
        plt.ylabel('Force')
        plt.title('Force or Gradient of vs. Distance')
        plt.legend()
        plt.show()
        return fitted_gaussian,fitted_lorentzian,fitted_polynomial,gradient
    # end of the block of plot for all, i.e.-> Determine the best fit if allfit are enabled. ------------------------------------------------------------->

    # Plot the results

    plt.figure(figsize=(10, 6))
    plt.scatter(distance, potential, label='Data', s=10, color='black')

    if chi2_gaussian != np.inf and gaussianfit is not None:
        plt.plot(distance, fitted_gaussian, label='Gaussian Fit', color='red')
    if chi2_lorentzian != np.inf and lorentzianfit is not None:
        plt.plot(distance, fitted_lorentzian, label='Lorentzian Fit', color='blue')
    if chi2_polynomial != np.inf and polynomialfit is not None:
        plt.plot(distance, fitted_polynomial, label=f'Polynomial Fit (degree {degree})', color='green')

    plt.xlabel('Distance')
    plt.ylabel('Potential')
    plt.title('Fit Comparison')
    plt.legend()
    plt.show()

    # Calculate and plot the gradient of the best fit
    if gaussianfit is not None:
        best_fitted = fitted_gaussian
    elif lorentzianfit is not None:
        best_fitted = fitted_lorentzian
    else:
        best_fitted = fitted_polynomial

    gradient = -np.gradient(best_fitted, distance)

    plt.figure(figsize=(10, 6))
    plt.plot(distance, gradient, label='Gradient of Best Fit', color='red')
    plt.xlabel('Distance')
    plt.ylabel('Force')
    plt.title('Force or Gradient of vs. Distance')
    plt.legend()
    plt.show()
    return best_fitted,gradient   # best_fitted -> fit_potential, gradient -> force.

if __name__== "__main__":
    data = pd.read_csv('smooth_data.csv')
    distance = data['distance'].values
    potential = data['potential'].values
    # data = pd.concat([distance,potential],axis=0)
    data = (distance,potential)
    data = np.array(data)
    print(data)
    fit_choose_for_potentialfind_force(data,gaussianfit=None,lorentzianfit=1,polynomialfit=None,degree_poly=4)
    # fit_choose_for_potentialfind_force(data,gaussianfit=1,lorentzianfit=1,polynomialfit=3,degree_poly=4)

    # sliced_data_index = sliced_data_min_zero_potential_force_and_index(distance,potential,no_timesofwhm_beforeminima=10,no_timesofwhm_afterminina=20)



