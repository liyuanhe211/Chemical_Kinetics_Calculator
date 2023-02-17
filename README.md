# Eyring Equation and Chemical Kinetics Calculator
[![DOI](https://zenodo.org/badge/548741869.svg)](https://zenodo.org/badge/latestdoi/548741869)

This is a small educational program that can solve the Eyring Equation and first/second order kinetics.

To run the program, call `python Eyring_Eq.py`. The virtual environment can be installed with the pipenv pipfile.

Alternatively, you can [download a release](https://github.com/liyuanhe211/Eyring_Eq/releases) for Windows which includes an executable packed with `pyinstaller`.

##
### Background
In literature, people often quote inexact rules like "21 kcal/mol at room temperature" when discussing calculated activation Gibbs free energies. They might even ask for a reference to support these crude rules or ask for values at different conditions. However, it's easy to calculate the reaction time, required temperatures, etc. from the Eyring equation and first/second order kinetics (assuming the reaction is kinetically controlled). So, I created this small program for that purpose.

### Usage

To use the program, fill in the known values for the equations, and leave the unknown values blank. If the number of filled parameters is sufficient (and not excessive), the \[Calculate\] button will become available. Click it to get the values you left blank. 

For example, you can calculate:

For a 21 kcal/mol unimolecular reaction to get a 98% conversion at 20 °C, you need 49 min.

<p align="center"><img src="https://user-images.githubusercontent.com/18537705/194800939-fbc173a3-6b08-499e-aa5a-5ff7c7e80736.png" width="80%" height="80%" align="center"></img></p>

For a second order reaction that can "finish" in 2 hours at 25 °C with a starting concentration of 0.01 mol/L, the Gibbs free energy corresponds to 81.8 kJ/mol

<p align="center"><img src="https://user-images.githubusercontent.com/18537705/194801049-bf00d1a6-5ed8-47fb-8fad-95922141c454.png" width="80%" height="80%" align="center"></img></p>

For a reaction with 120 kJ/mol activation Gibbs free energy (note that you do need to consider changes of Gibbs free energy relative to temperature) to get a 98% conversion within one day, the temperature needs to be 90 °C.

<p align="center"><img src="https://user-images.githubusercontent.com/18537705/194801142-e3cb8fa9-c2e2-4045-9eff-736dda17f7a1.png" width="80%" height="80%" align="center"></img></p>

Or any other valid combination of known/unknown values.
##
### Equations
 * Eyring Equation:

$$k =\sigma\frac{k_B  T}{h}\left ( \frac{R T}{1\ atm} \right )^{\Delta n}exp(-\frac{{\Delta G}^{\neq}}{R T})$$

 * First order kinetics:

$$c = c_{0}\ exp(-kT)$$

 * Second order kinetics:

Starting with different concentration for species A and B (could someone tell my why the zeros are not subscripted?):

$$ln\frac{[B] [A]_{0}}{[A] [B]_{0}} = k([B]_{0}-[A]_{0})t$$

Starting A and B at the same concentration:

$$\frac{1}{[A]} = \frac{1}{[A]_{0}}+kt$$

##
### Citation
I believe the Eyring equation and the first/second order kinetics are old and well-known enough to not require citation. However, if you need to cite this program, you can use the Zenodo DOI [![DOI](https://zenodo.org/badge/548741869.svg)](https://zenodo.org/badge/latestdoi/548741869).

E.g. Li, Y.-H. _Eyring Equation and Chemical Kinetics Calculator 1.1.1_ (DOI: 10.5281/zenodo.7214153), **2022**. (Please change the info to respect the version you are using.)

##
### Update History
**1.2**
 * Support A+Cat->P+Cat mode.
 * Support kcal/mol, eV, min, h, day, year units.
 * Add shortcut to pushbuttons.
 * Add sanity check for inputs.
 * Solve number overflow, divided by zero problem when conversion is too close to 100%.
 * Add automatic tests.
 * Correct number representation function using floor instead of round.
 * Switch to PyQt6 for better high DPI support.
 * Switch to pipenv for smaller packed exe.
