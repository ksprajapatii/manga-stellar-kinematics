# Milestone 9 — Quantitative Stellar Kinematics: Consolidated Results

## Project
**Stellar Kinematics Mapping of a Galaxy Using IFU Data**  
Target: MaNGA plate-IFU **8138-12704**  
DAPTYPE: **HYB10-MILESHC-MASTARSSP**  
Data product: MaNGA DR17 MAPS / DAP products

---

## 1. Executive summary

Milestone 9 quantitatively revalidated the stellar velocity and velocity-dispersion measurements, compared alternative weighting choices for the first-order kinematic-plane fit and the projected angular-momentum proxy \(\lambda_R\), and examined radial trends.

The stellar kinematic footprint contains **2,704 spaxels** representing **2,194 unique stellar bins**. The binning is singleton-dominated: **2,072 bins (94.44%)** contain one spaxel. The corrected stellar velocity-dispersion profile declines strongly from the central region to approximately \(1\)–\(1.5\,R_e\), with a small outer-bin increase that should be treated cautiously because the outermost radial bin contains only 94 bins.

The first-order kinematic position angle is approximately **167°**. The \(\lambda_R\) estimate within \(2\,R_e\) depends on whether each bin is weighted by its mean flux alone or by an approximate integrated-bin flux. The area-weighted result is **0.6998**, compared with **0.7156** for per-bin flux weighting. The area-weighted value is adopted as the primary working estimate, while the per-bin result is retained as a methodology sensitivity check.

These are projected, aperture-dependent measurements. They do not by themselves establish an intrinsic circular speed, a unique dynamical model, or a supermassive-black-hole binary.

## 2. Data selection and valid sample

- Stellar bin map: `BINID[1]` (stellar-continuum channel, C2).
- Covered stellar footprint: `BINID[1] >= 0`.
- Covered spaxels: **2,704**.
- Unique stellar bins: **2,194**.
- Singleton bins: **2,072 (94.44%)**.
- Multi-spaxel bins: **122**.
- Median bin size: **1 spaxel**.
- 95th-percentile bin size: **2 spaxels**.
- Maximum bin size: **29 spaxels**.

The MAPS stellar velocity and dispersion values are constant within multi-spaxel stellar bins, as expected for measurements assigned from the binned stellar-continuum fit.

### Mask interpretation

The MAPS mask contains:
- `0`: 2,704 spaxels.
- `2^30 + 2^4` (`DONOTUSE + NOVALUE`): 2,480 spaxels.

The 2,704 spaxels in the stellar BINID footprint all have mask value zero. The 2,480 flagged pixels lie outside the stellar footprint (`BINID[1] = -1`). Therefore, these flagged pixels represent non-footprint/uncovered locations in this target map, not failed measurements inside the covered stellar sample.

Within the covered footprint, velocity and dispersion are finite and their inverse variances are positive. The standard and strict samples therefore coincide when restricted to the stellar BINID footprint.

## 3. Stellar velocity and dispersion

### Velocity

- Median residual stellar velocity: **33.6441 km/s**.
- Weighted-plane intercept: **23.2515 km/s**.
- First-order velocity gradient: **20.2767 km/s/arcsec**.
- First-order kinematic PA: **167.3003°**.
- Projected rotation-amplitude proxy: **206.8342 km/s**.

The median velocity and plane intercept are descriptive reference quantities relative to the DAP velocity reference. Neither should be presented as an independently established absolute physical systemic velocity.

The robust velocity scatter previously calculated over the full velocity field was approximately **190.3 km/s**. This includes the spatial rotation gradient and is not a measurement uncertainty on the systemic velocity.

### Velocity-dispersion correction

The instrumental correction is applied as:

\[
\sigma_{\rm corrected} =
\sqrt{\sigma_{\rm raw}^{2} -
\sigma_{\rm inst}^{2}},
\]

where the instrumental term is taken from the first channel of `STELLAR_SIGMACORR`.

Within the covered footprint:
- Raw \(\sigma\) median: **100.055 km/s**.
- Corrected \(\sigma\) median: **98.220 km/s**.
- Corrected \(\sigma\) range: **51.077–203.025 km/s**.
- Instrumental correction range: **12.972–24.027 km/s**.

No negative radicands were found in the covered footprint.

Formal uncertainty medians from inverse variance:
- Stellar velocity: **5.257 km/s**.
- Stellar dispersion: **6.728 km/s**.

These are formal measurement uncertainties and do not include all systematic uncertainties (e.g. template mismatch, PSF effects, or model assumptions).

## 4. Weighting sensitivity of the kinematic-plane fit

Two plane-fit weighting schemes were compared:

| Weighting | Intercept (km/s) | Gradient (km/s/arcsec) | PA (deg) |
|---|---:|---:|---:|
| Inverse variance | 23.2515 | 20.2767 | 167.3003 |
| Inverse variance × bin area | 23.4094 | 19.9509 | 166.4914 |

The fitted PA changes by less than one degree between these choices, and the gradient changes modestly. The first-order PA is therefore reasonably stable to this particular weighting choice. It remains a plane-fit estimate, not a full kinemetry result, and should be compared with the photometric PA before making strong statements about alignment.

The projected rotation-amplitude proxy is not a deprojected circular velocity. Inclination and a suitable dynamical model would be required for that interpretation.

## 5. Radial velocity-dispersion profile

Elliptical-radius annuli produced the following profile:

| Radius (Re) | Annulus (Re) | Number of bins | Median residual velocity (km/s) | Median corrected sigma (km/s) | Median raw sigma (km/s) |
|---:|---:|---:|---:|---:|---:|
| 0.25 | 0.0–0.5 | 254 | -10.1846 | 156.6854 | 158.1310 |
| 0.75 | 0.5–1.0 | 770 | -5.7096 | 110.5164 | 112.2857 |
| 1.25 | 1.0–1.5 | 1,076 | +5.2231 | 89.4793 | 91.3332 |
| 1.75 | 1.5–2.0 | 94 | +22.9350 | 91.6725 | 93.5449 |

The corrected dispersion decreases from approximately **156.7 km/s** in the central \(0\)–\(0.5\,R_e\) annulus to approximately **89.5 km/s** at \(1.0\)–\(1.5\,R_e\). It then rises slightly to approximately **91.7 km/s** in the \(1.5\)–\(2.0\,R_e\) annulus. Because the outermost annulus contains only 94 bins, this small increase should not be over-interpreted.

The annular median residual-velocity trend changes from negative to positive with radius. This is **not a conventional rotation curve**: elliptical annuli mix different azimuths, and an uneven spatial distribution can shift an annular median. A rotation curve should instead be extracted along the kinematic major axis or using angular sectors / a suitable tilted-ring or harmonic method.

## 6. \(\lambda_R\) methodology audit

The analysis compared three luminosity-weighting proxies:
1. `BIN_MFLUX` per bin.
2. `BIN_MFLUX × BIN_AREA`.
3. `BIN_MFLUX × number of spaxels`.

Results:

| Aperture | Weighting | \(\lambda_R\) | Number of bins |
|---|---|---:|---:|
| 1 Re | BIN_MFLUX per bin | 0.646215 | 1,024 |
| 1 Re | BIN_MFLUX × BIN_AREA | 0.646215 | 1,024 |
| 1 Re | BIN_MFLUX × spaxel count | 0.646215 | 1,024 |
| 2 Re | BIN_MFLUX per bin | 0.715598 | 2,194 |
| 2 Re | BIN_MFLUX × BIN_AREA | 0.699775 | 2,194 |
| 2 Re | BIN_MFLUX × spaxel count | 0.699775 | 2,194 |

At \(1\,R_e\), the methods give the same result for this sample. At \(2\,R_e\), area/spaxel-count weighting lowers \(\lambda_R\) by approximately **0.0158** relative to per-bin weighting.

`BIN_MFLUX` is a mean flux quantity per spaxel, while `BIN_AREA` records bin area. Their product is a reasonable approximation to integrated bin flux for this purpose, subject to the bin-centre/aperture-boundary and spatial-weighting approximations. Consequently, the working primary values are:

- **\(\lambda_R(<1R_e) = 0.6462\)**.
- **\(\lambda_R(<2R_e) = 0.6998\)** (area-weighted).

Retain **0.7156** as the \(2\,R_e\) per-bin-weighting sensitivity result. Do not hide this methodological dependence. \(\lambda_R\) is a projected, aperture-dependent proxy; its interpretation depends on geometry, flux weighting, PSF, spatial sampling, and aperture definition.

## 7. Bootstrap uncertainty

The previous 2,000-iteration bootstrap gave the following 16th/50th/84th percentiles:

| Quantity | 16th | Median | 84th |
|---|---:|---:|---:|
| Systemic/reference velocity estimate (km/s) | 26.6949 | 33.7738 | 38.5799 |
| Kinematic PA (deg) | 166.877 | 167.307 | 167.739 |
| Gradient (km/s/arcsec) | 20.1185 | 20.2696 | 20.4209 |
| Projected rotation proxy (km/s) | 205.917 | 206.781 | 207.574 |
| \(\lambda_R(<1R_e)\) | 0.637341 | 0.645878 | 0.654866 |
| \(\lambda_R(<2R_e)\) | 0.709792 | 0.715463 | 0.721073 |

These bootstrap intervals quantify sampling variation under the adopted resampling procedure. They do **not** account for all systematic effects, including PSF/beam smearing, template mismatch, DAP assumptions, photometric geometry, or inclination.

The bootstrap \(\lambda_R\) values above correspond to the earlier bootstrap implementation and should not be silently conflated with the later area-weighted primary estimate. A future uncertainty analysis should bootstrap the selected area-weighted estimator directly.

## 8. Adopted results and interpretation

For the current project stage, report the following as the primary working values:

| Measurement | Adopted working value | Qualification |
|---|---:|---|
| Covered stellar spaxels | 2,704 | Stellar BINID footprint |
| Unique stellar bins | 2,194 | 2,072 singleton bins |
| Kinematic PA | 167.3 deg | First-order weighted-plane fit |
| Velocity gradient | 20.28 km/s/arcsec | Projected plane-fit gradient |
| Projected rotation proxy | 206.8 km/s | Not deprojected circular speed |
| Corrected sigma median | 98.22 km/s | Instrumentally corrected |
| \(\lambda_R(<1R_e)\) | 0.6462 | Weighting methods agree here |
| \(\lambda_R(<2R_e)\) | 0.6998 | Area-weighted primary estimate |
| \(\lambda_R(<2R_e)\), sensitivity | 0.7156 | Per-bin flux weighting |

The data show organized projected stellar rotation and a centrally elevated stellar velocity dispersion that declines outward over most of the measured radial range. These observations motivate further dynamical analysis but do not uniquely determine the galaxy's three-dimensional dynamics.

## 9. Limitations and claims to avoid

Do not claim, on the basis of these milestones alone, that:
- the projected rotation proxy is the galaxy's intrinsic circular velocity;
- the annular median-velocity profile is a conventional rotation curve;
- the plane-fit PA is a full kinemetry PA;
- the formal IVAR errors include all systematic uncertainties;
- the observed central dispersion enhancement uniquely identifies a central black hole;
- a supermassive-black-hole binary has been detected or established.

Important remaining systematics include PSF/beam smearing, inclination, photometric geometry, template mismatch, DAP model assumptions, and the exact flux/aperture weighting used for \(\lambda_R\).

## 10. Next milestone

**Milestone 10 should focus on spatially resolved kinematic validation**, not on repeating the same annular statistics. Recommended analyses:

1. Derive a major-axis velocity profile using the measured kinematic PA and a clearly stated slit/sector width.
2. Compare the kinematic PA with a photometric PA derived from imaging or a documented catalogue value.
3. Examine approaching/receding-side symmetry and residuals from a simple projected rotation model.
4. Quantify \(V/\sigma\) with an explicit aperture and weighting definition.
5. If data quality supports it, perform harmonic/kinemetry-style analysis and report the model limitations.
6. Carry the adopted area-weighted \(\lambda_R\) estimator into a bootstrap that recomputes the same estimator.

### Reproducibility note

This report consolidates the numerical results supplied from the user's executed Milestone 9 and 9B outputs, together with the already established Milestone 8 footprint/mask validation. It is a synthesis of those outputs, not a claim that this report-generation step re-executed the user's local notebooks or re-opened the original FITS files.
