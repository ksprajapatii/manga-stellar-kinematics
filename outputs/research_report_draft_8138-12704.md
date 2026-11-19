# Stellar Kinematics of MaNGA Target 8138-12704

## Data
The analysis uses the MaNGA MAPS product for plate-IFU 8138-12704,
with DAPTYPE HYB10-MILESHC-MASTARSSP. Stellar kinematic measurements
are treated as Voronoi-bin measurements, with one representative
measurement retained per stellar bin.

## Methods
Stellar line-of-sight velocities and velocity dispersions were extracted
from the MAPS product. The velocity dispersion was corrected using
the first channel of STELLAR_SIGMACORR:
sigma_corrected = sqrt(sigma_raw^2 - sigma_instrumental^2).
Measurements were filtered using DAP quality flags and positive inverse
variance. A weighted first-order plane was fitted to estimate the
large-scale velocity gradient and a preliminary kinematic position angle.
Radial profiles and a projected lambda_R estimator were calculated
using the adopted DAP elliptical coordinates.

## Preliminary measurements
- Number of unique stellar bins: 2194
- Standard joint-valid bins: 2194
- Strict joint-valid bins: 2194
- Residual velocity relative to DAP input guess: 33.64 km/s
- First-order kinematic PA: 167.30 degrees (modulo 180)
- Projected rotation amplitude proxy: 206.83 km/s
- lambda_R within 1 Re: 0.6462
- lambda_R within 2 Re: 0.7156

## Robustness
Compare the standard and strict quality-cut results in the accompanying
robustness report. Bootstrap intervals quantify sampling variation among
the selected bins and do not include the full systematic error budget.

## Interpretation — complete after inspecting the figures
[Describe whether the velocity field is regular, whether the fitted
kinematic axis agrees with the map, and whether the dispersion profile
shows a central enhancement or other structure. Do not infer features
that are not visible or statistically supported.]

## Relevance to the candidate SMBH-binary host-galaxy question
[Explain what the measured large-scale stellar kinematics do and do not
constrain. These MaNGA measurements alone cannot establish the presence
of a close SMBH binary. State what independent evidence and higher
spatial/spectral resolution follow-up would be needed.]

## Limitations
[Discuss spatial resolution/PSF, inclination and geometry assumptions,
template mismatch, DAP binning, mask sensitivity, radial coverage,
and systematic uncertainties.]
