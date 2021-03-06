# Change Log

All notable changes to this project will be documented in this file. It's a team effort
to make them as straightforward as possible.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project
adheres to [Semantic Versioning](http://semver.org/).

## [0.1.1] - In Progress

### Added

- Added registry for backbone models.
- Added additional links (CoC, PyPI) and information (contributing, citing) to project
  README.md.
- Added CMIC seminar where DeepReg was introduced to the project README.md.

### Changed

- Simplified configuration for backbone models.

### Fixed

- Fixed bias initialization for theta in GlobalNet.
- Remove invalid `first` argument in DataLoader for sample_index generator.
- Fixed build error when downloading data from private repo.

## [0.1.0] - 2020-11-02

### Added

- Added option to change kernel size and a kernel type for LNCC image similarity loss.
- Added visualization tool for generating gifs from model outputs.
- Added max_epochs argument for training to overwrite configuration.
- Added log_root argument for training and prediction to customize the log file
  location.
- Added more meaningful error messages for data loading.
- Added integration tests for all demos.
- Added environment.yml file for Conda environment creation.
- Added Dockerfile.
- Added documentation about using UCL cluster with DeepReg.

### Changed

- Updated TensorFlow version to 2.3.1.
- Updated the pre-trained models in MR brain demo.
- Updated instruction on Conda environment creation.
- Updated documentation regarding pre-commit and unit-testing.
- Updated the issue and pull-request templates.
- Updated the instructions for all demos.
- Updated pre-commit hooks version.
- Updated JOSS paper to address reviewers' comments.
- Migrated from travis-ci.org to travis-ci.com.

### Fixed

- Fixed prediction error when number of samples cannot be divided by batch size exactly.
- Fixed division by zero handling in multiple image/label losses.
- Fixed tensor comparison in unit tests and impacted tests.
- Removed normalization of DDF/DVF when saving in Nifti formats.
- Fixed invalid link in the quick start page.

## [0.1.0b1] - 2020-09-01

Initial beta release.
