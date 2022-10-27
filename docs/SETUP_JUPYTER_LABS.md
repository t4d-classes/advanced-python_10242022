# Setup Jupyter Labs

1. Create and activate a new Conda environment.

```
conda create -n jupyter
conda activate jupyter
```

2. Install Jupyter Labs and other commonly used packages.

```bash
conda install -c conda-forge jupyterlab jupyterlab-lsp python-lsp-server
conda install -c conda-forge numpy matplotlib pandas scipy
```

3. Install a new kernel using the new Conda environment.
```bash
python -m ipykernel install --user --name=jupyter
```

4. Run Jupyter Labs.

```bash
jupyter-lab
```