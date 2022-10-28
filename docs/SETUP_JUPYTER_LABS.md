# Setup Jupyter Labs


1. Create and activate a new Conda environment.

```
conda create -n jupyter
conda activate jupyter
```

2. Install Jupyter Labs and other commonly used packages.

```bash
python -m pip install jupyterlab jupyterlab-lsp python-lsp-server
python -m pip install numpy matplotlib pandas scipy
```

3. Install a new kernel using the new Conda environment.
```bash
python -m ipykernel install --user --name=jupyter
```

4. Run Jupyter Labs.

```bash
jupyter-lab
```