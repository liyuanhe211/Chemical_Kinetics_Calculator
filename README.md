# Eyring Equation and Chemical Kinetics Calculator
A small educational program to solve Eyring Equation and first/second order kinetics.

To run the program, call `python Eyring_Eq.py`. You should be able to run it with stock Anaconda. 

Alternatively, you can download a release for Windows which has an executable packed with `Cx_Freeze` (I don't have the interest to optimize it, so it's quite large).

##
When people discussing calculated activation Gibbs free energies in literatures, it's common to see people quoting general, inexact rules like "activation Gibbs free energy for room temperature reaction should be below 21 kcal/mol", while asking for references for reaction at different temperature. However, it's easy to calculate the reaction time, required temperatures, etc, from Eyring equation and first/second order kinetics (suppose the reaction is kinetically controlled).

So I wrote this small program for this purpose. For example:

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

Starting with different concentration for species A and B:

$$ln\frac{[B] [A]_{0}}{[A] [B]_{0}} = k([B]_{0}-[A]_{0})t$$

Starting A and B at the same concentration:

$$\frac{1}{[A]} = \frac{1}{[A]_{0}}+kt$$
