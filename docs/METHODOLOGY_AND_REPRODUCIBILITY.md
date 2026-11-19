# Methodology and reproducibility

## Scope

The notebook inventory indicates a workflow covering MaNGA data acquisition, FITS metadata inspection, stellar-kinematic extraction, WCS/galaxy geometry, quantitative analysis, uncertainty/robustness, radial profiles including a \u03bbR audit, spatially resolved validation, and photometric geometry.

This document is a reproducibility checklist. Fill in the exact implementation details from the notebooks before describing the workflow as a finalized method.

## Data provenance checklist

Record the following for every input:

- SDSS data release and product version.
- MaNGA plate and IFU: `8138-12704`.
- Exact MAPS/LOGCUBE/DRPALL filenames used.
- DAPTYPE and relevant extension names.
- Download source, retrieval date, and file checksum.
- Whether a value comes from a survey pipeline product or is recomputed in this project.

## Measurement and validation checklist

For every stellar-kinematic map or derived statistic, document:

- Physical quantity and units (e.g., line-of-sight velocity or velocity dispersion in km s\u207b\u00b9).
- FITS extension and data model used.
- Spatial coordinate convention and WCS handling.
- Valid-spaxel/bin selection, mask bits, and signal-to-noise criteria.
- Treatment of Voronoi/hybrid binning, if applicable.
- Instrumental-resolution correction, if applied, including the exact formula and resolution source.
- Adopted systemic velocity and whether velocities are relative or absolute.
- Position-angle convention, reference direction, and 180-degree ambiguity handling.
- Apertures, radial coordinate definition, and effective-radius normalization.
- Uncertainty propagation, covariance treatment, and robustness tests.

## Reproducible execution

1. Clone the repository.
2. Create and activate a Python environment.
3. Install the packages listed in `requirements.txt`.
4. Download the required MaNGA products using the data-acquisition notebook's documented source and release.
5. Place local data in the documented data directory (raw data should remain untracked).
6. Execute notebooks in the order in `NOTEBOOK_INDEX.md`.
7. Confirm that generated figures/tables match the committed outputs.
8. Record tested operating system, Python version, and package versions.

## Reporting standard

Every scientific claim in the README or a report should point to a notebook cell, generated table, or figure. Distinguish direct measurements from derived quantities and interpretation. A candidate SMBH-binary designation is a motivation/context, not a result established by a stellar-kinematic map alone.
