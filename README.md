Protein-AFM-Analysis-and-Lennard-Jones-Potential-Fitting

This repository contains the complete analysis pipeline for Atomic Force Microscopy (AFM) data collected from protein samples on a gold substrate. The data is processed to extract the region of interest, correct data, locate key points (such as minima and points of inflexion), and fit the derived potential and force with the Lennard-Jones potential function. Additional calculations include the Young's modulus, Hamaker constant, and energy dissipation.

Table of Contents
- [Introduction](introduction)
- [Features](features)
- [Requirements](requirements)
- [Usage](usage)
- [Files in the Repository](files-in-the-repository)
- [How to Run](how-to-run)
- [Contributors](contributors)
- [License](license)

Introduction
Atomic Force Microscopy (AFM) is widely used to study the interaction forces between a probe and a sample surface at the nanoscale. This repository focuses on the analysis of protein samples deposited on a gold substrate. The workflow includes data preprocessing, extraction of regions of interest, force and potential derivation, and application of the Lennard-Jones potential fitting to characterize the molecular interactions.

The analysis also computes key mechanical and physical properties such as
- Young's modulus
- Hamaker constant
- Energy dissipation

Features
- Data Extraction and Correction Extracts the region of interest and corrects the raw AFM data for further analysis.
- Key Points Identification Locates important features such as minima and points of inflexion in the force curve data.
- Lennard-Jones Potential Fitting Fits the Lennard-Jones potential to the derived interaction forces.
- Young's Modulus Calculation Computes the Young’s modulus of the protein samples from force-displacement data.
- Hamaker Constant Derives the Hamaker constant, which is essential for understanding van der Waals interactions.
- Energy Dissipation Calculates energy dissipation during AFM measurements.
  
Requirements
- Python 3.7 or higher
- Pandas
- Numpy
- Scipy
- Matplotlib (optional for plotting)
- OpenPyXL (for Excel file handling)

To install the required packages, run
```bash
pip install -r requirements.txt
```

Usage
1. Clone the repository
   ```bash
   git clone httpsgithub.commohdrafikProtein-AFM-Analysis-and-Lennard-Jones-potential-fitting.git
   cd Protein-AFM-Analysis-and-Lennard-Jones-potential-fitting
   ```

2. Prepare your AFM data files in `.xlsx` format and place them in the appropriate directory.

3. Modify the `main.py` script to specify your data paths and analysis parameters.

4. Run the analysis script
   ```bash
   python main.py
   ```

Files in the Repository
- main.py The main script that initiates the analysis workflow, including calling the necessary functions and setting up parameters.
- ham.py Contains the function `hamaker_const` which calculates the Hamaker constant and other related quantities.
- analysis_functions.py Houses the core analysis functions for data correction, potential derivation, force fitting, and calculation of Young’s modulus and energy dissipation.
- requirements.txt Lists the required Python packages.

How to Run
1. Place your `.xlsx` AFM data files in the data directory.
2. Adjust parameters such as `K`, `Q`, `R`, and `hamdeg` in `main.py` based on your experimental setup.
3. Run `main.py` to process your data, which will
   - Extract the region of interest.
   - Locate key points like minima and inflection points.
   - Correct and normalize the AFM data.
   - Fit the Lennard-Jones potential to the derived forces.
   - Calculate Young’s modulus, Hamaker constant, and energy dissipation.
4. The results, including fitted parameters and computed quantities, will be saved in an output file.

Contributors
- Mohd Rafik  
Feel free to contribute by opening issues, making pull requests, or suggesting improvements.

License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.