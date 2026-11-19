# Notebook index and suggested execution order

This index is based on the notebook filenames visible in the supplied GitHub screenshots. It describes scope inferred from filenames only; inspect each notebook's markdown and code before treating these descriptions as verified.

| Order | Current filename | Apparent role | Notes |
|---:|---|---|---|
| 1 | `01_data_acquisition.ipynb` | Retrieve/document target MaNGA data | Record data release, URLs, checksums, and retrieval date. |
| 2 | `02_fits_metadata_exploration.ipynb` | Inspect FITS structure and metadata | There are also `_edited` and `_reviewed` variants; identify the canonical version. |
| 2a | `02_fits_metadata_exploration_edited.ipynb` | Alternate edited metadata notebook | Compare against original and reviewed versions. |
| 2b | `02_fits_metadata_exploration_reviewed.ipynb` | Alternate reviewed metadata notebook | Candidate for canonical version only after content comparison. |
| 3 | `03_stellar_kinematics_extraction.ipynb` | Extract/examine stellar kinematic quantities | Verify extensions, masks, units, and data provenance. |
| 4 | `04_wcs_visualization_galaxy_geometry.ipynb` | WCS visualization and projected geometry | Document coordinate conventions and adopted centre/PA. |
| 5 | `05_quantitative_stellar_kinematics.ipynb` | Quantitative stellar-kinematic analysis | Document definitions, masks, and uncertainty propagation. |
| 6 | `06_robustness_uncertainty_scientific_report.ipynb` | Robustness and uncertainty assessment | State each test and what it can/cannot establish. |
| 7 | `07_research_synthesis_reproducibility.ipynb` | Synthesis and reproducibility | Ensure conclusions link to reproducible outputs. |
| 8 | `08_advanced_kinematic_validation.ipynb` | Advanced validation | Document independent checks and acceptance criteria. |
| 9 | `09_quantitative_results_revalidation.ipynb` | Revalidation of quantitative results | Explain what changed relative to notebook 05. |
| 9b | `09B_radial_profiles_lambdaR_audit.ipynb` | Radial-profile and \u03bbR audit | Explain exact \u03bbR definition, apertures, and binning. |
| 10 | `10_spatially_resolved_kinematic_validation.ipynb` | Spatially resolved validation | Document spatial sampling and quality selection. |
| 11 | `11_photometric_geometric_analysis.ipynb` | Photometric/projected geometry analysis | Identify source image/catalog and PA/ellipticity conventions. |

## Recommended cleanup

1. Compare the three `02_fits_metadata_exploration*` notebooks cell-by-cell.
2. Select one canonical notebook for the main workflow.
3. Move superseded variants to `notebooks/archive/` or label them clearly as historical; do not delete them until their contents and outputs are checked.
4. Keep the `09B` audit notebook adjacent to the radial/\u03bbR analysis it supports; renumber only if all internal links and references are updated.
5. Add a short markdown preamble to every notebook: purpose, inputs, outputs, dependencies, and expected runtime.
6. Ensure each notebook runs from a fresh kernel in the documented order, or explicitly document dependencies on saved intermediate products.
