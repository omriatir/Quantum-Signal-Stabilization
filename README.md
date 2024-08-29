# Quantum-Signal-Stabilization
Final Project - quantum signal stabilization analysis 


# Explanation about classical simulation
We modeled a classical Gaussian beam propagating through a noisy medium. We considered beam expansion in space and interaction with environmental particles, which cause propagation through varying refractive indices. The beam loses energy and amplitude. We aimed to determine if the beam becomes too distorted under windy and humid conditions as a prerequisite for proceeding to explore single-photon behavior in these conditions. we found that as long as the beam passes through turbulent air conditions, the change in the amplitude is not that significant compared to the beam divergance which makes hard to test without proper equipment.

change n2 = n(λ, t, p, h, xc)
    # λ: wavelength, 0.3 to 1.69 μm
    # t: temperature, -40 to +100 °C
    # p: pressure, 80000 to 120000 Pa
    # h: fractional humidity, 0 to 1
    # xc: CO2 concentration, 0 to 2000 ppm
in Classical Beam Propagation.py , line 66
and step, step size at lines 55,56
to see their influence over the beam.

