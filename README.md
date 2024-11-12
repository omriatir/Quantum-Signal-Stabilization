# Quantum-Signal-Stabilization
Final Project - quantum signal stabilization analysis 


# Explanation about classical simulation
We modeled a classical Gaussian beam propagating through a noisy medium. We considered beam expansion in space and interaction with environmental particles, which cause propagation through varying refractive indices. The beam loses energy and amplitude. We aimed to determine if the beam becomes too distorted under windy and humid conditions as a prerequisite for proceeding to explore single-photon behavior in these conditions. we found that as long as the beam passes through turbulent air conditions, the change in the amplitude is not that significant compared to the beam divergance which makes hard to test without proper equipment.

change n2 = n(λ, t, p, h, xc) <br>
    # λ: wavelength, 0.3 to 1.69 μm <br>
    # t: temperature, -40 to +100 °C <br>
    # p: pressure, 80000 to 120000 Pa <br>
    # h: fractional humidity, 0 to 1 <br>
    # xc: CO2 concentration, 0 to 2000 ppm <br>
in Classical Beam Propagation.py , line 66 <br>
and step, step size at lines 55,56 <br>
to see their influence over the beam.

![WhatsApp Image 2024-08-29 at 21 24 17](https://github.com/user-attachments/assets/a726370f-f4e9-4a25-a23d-bd23a8c44558)

# Experiments Analysis & Results (Quantum Experiments)

This repository contains Jupyter Notebook scripts for analyzing the influence of Reynolds number on photon polarization, focusing on both classical and quantum optical properties. This project uses data processing, noise subtraction, data fitting, and graphical representation techniques to examine polarization effects under varying conditions.

## Project Structure

- **Data Collection and Noise Processing:** Processes raw experimental data, subtracts background noise, and prepares it for further analysis.
- **Data Fitting and Visualization:** Analyzes processed data through cos² fitting (Malus' Law) and visualizes results to observe patterns and draw conclusions.

## Files

- **`Final Proj. - last calc..ipynb`**: Main Jupyter Notebook containing all final scripts, including:
  - Noise approximation
  - Data after noise subtraction
  - Data visualization and graphing
  - Data fitting using Malus' Law

- **`Final proj - First Exp & validation of Last Exp`**: First scripts for the outdoor experiments and the validation scripts for the Last Experiment (Making sure we use single photons). The main Jupyter Notebook contain an ordered and improve version of this scripts.  

- **`Final proj - mes (before order)`**: a draft version of **`Final proj - First Exp & validation of Last Exp`**.

## Dependencies  
To run these notebooks, ensure you have the following libraries installed:

- `numpy`: For numerical computations.
- `scipy`: For data fitting and statistical analysis.
- `matplotlib`: For plotting graphs.
- `pandas`: For data manipulation and processing.

## Explanation of Sections

### 1. Noise Approximation

This section processes background noise data to calculate average photon counts and standard deviations. These values are critical for improving the accuracy of the main experiment measurements by allowing us to subtract noise from the signal.

#### Inputs:
- **`main_directory`**: The path to the experiment’s main folder, which should contain a subfolder named `noise`.

#### Variables:
- **`angles1`**: List of polarization angles used for the noise measurements.
- **`data_avgs1`**: List of average photon counts per angle in the noise subfolder.
- **`data_stds1`**: List of standard deviations per angle.

#### Outputs:
- **`Noise`**: Dictionary containing a zipped list of tuples, each with (angle, average photon count, standard deviation).
- **`noise_avg`**: Mean of the average photon counts across all measured angles.
- **`noise_std`**: Combined standard deviations across angles.

#### Notes:
The noise files should contain measurements at specific angles (typically 0° and 90°) for calibration and background noise characterization.

---

### 2. Data Processing after Noise Subtraction

This section processes experimental data from the main experiment subfolders (excluding the noise data). For each measurement, the average noise value is subtracted, and the combined standard deviation of noise and measurement is calculated.

#### Inputs:
- **`main_directory`**: The path to the main experiment folder.

#### Variables:
- **`angles1`**: List of angles where measurements were taken, corresponding to different polarization orientations.
- **`data_avgs1`**: List of mean photon counts or intensities per angle after subtracting the noise.
- **`data_stds1`**: List of combined standard deviations for each angle, including both measurement and noise components.

#### Outputs:
- **`results`**: Dictionary with subfolder names (e.g., wind speeds) as keys. Each value is a list of tuples, where each tuple contains values (angle, mean photon count, standard deviation).
- **`noise_avg`**: Mean of average photon counts or intensities across different angles after noise subtraction.
- **`noise_std`**: Combined standard deviation of averages across angles, representing uncertainty in the measurements.

#### Notes:
Each subfolder represents a different experimental condition, such as varying wind speeds, allowing for comparative analysis across different conditions.

---

### 3. Data Visualization

This section organizes and plots the processed data for all angles and conditions. This graphical representation provides a visual overview, enabling the identification of patterns and trends in photon counts or intensities across different polarization angles.

#### Variables:
- **`angles`**: Sorted list of measured angles, arranged from lowest to highest.
- **`values`**: List of photon count or intensity values corresponding to each angle.
- **`error`**: List of standard deviations for each measurement, corresponding to each angle.

#### Outputs:
- **Plot**: A graph comparing photon counts or intensities across all angles and experimental conditions, used for initial data exploration and to guide parameter fitting in the next section.

#### Notes:
This plot is essential for understanding the data distribution and provides guidance on choosing initial guesses for the fitting parameters.

---

### 4. Data Fitting (Malus' Law)

This section fits the processed data to a cos² function, based on Malus' Law, which describes the relationship between light intensity and polarization angle. This fitting process validates the alignment between experimental data and theoretical expectations.

#### Inputs:
- **`p0`**: Initial parameter guesses for the cos² fitting function. These values are estimated from the data visualization plot in the previous section.

#### Variables:
- **`angles`**: List of polarization angles used for each measurement.
- **`values`**: Photon count or intensity values at each angle, prepared for fitting.
- **`error`**: Standard deviations for each data point, representing measurement uncertainties.

#### Outputs:
- **`fit`**: Dictionary where each key is a subfolder name (representing a specific wind speed or condition), and each value is a list containing the fit parameters and the covariance matrix. The parameters correspond to the terms in the cos² fitting function: amplitude, offset, phase, and baseline.

#### Notes:
The fit parameters are used to check how closely the data matches Malus' Law and to identify any deviations that may arise from environmental factors, such as wind speed variations.

---

Each of these sections is designed to process and analyze experimental data for photon polarization under different conditions, making it suitable for exploring how factors like wind speed (via Reynolds number) influence polarization in both classical and quantum regimes.


You can install these dependencies via pip:
```bash
pip install numpy scipy matplotlib pandas
