# cdat_compute_graph

A package that extends the functionality of compute_graph with support for cdms2 functions and variables. 

# Releasing cdat_compute_graph

#### Set up

If this is the first time you have done a conda release make sure the following prerequisites are met:
1. You will need the anaconda client and the build package.
  * `conda install -q anaconda-client conda-build`
2. Make sure automatic uploads are turned off. 
  * `conda config --set anaconda_upload no`
3. If you are behind a corporate firewall that intercepts ssl you may need to turn ssl off. 
  * `conda config --set ssl_verify False`
  * `anaconda config --set verify_ssl False`

#### Set Version and git_tag

Set the new `version` number and `git_tag` inside `meta.yaml`.
  * Conda build will look for this tag in the git repo. We will set it in a later step.
  * The version number set here will appear in the anaconda repo.
  
#### Release on Github

Make sure the updated `meta.yaml` is pushed to Github.

Create a new release on Github [here](https://github.com/CDAT/cdat_compute_graph/releases), and make sure the tag matches the one inside the `meta.yaml`.
  
#### Build and Upload

To build the software run `conda build . -c cdat -c conda-forge`

To upload the newly built file, run `anaconda -t $TOKEN upload -u cdat $PATH`
  * $TOKEN comes from https://anaconda.org/cdat/settings/access
  * $PATH should look something like `/Users/your_user/miniconda2/conda-bld/noarch/cdat_compute_graph-0.0.0-py_0.tar.bz2`
