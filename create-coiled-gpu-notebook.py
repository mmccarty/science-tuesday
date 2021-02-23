import coiled

coiled.create_notebook(
  name="xgboost-gpu-demo",
  container="gpuci/miniconda-cuda:10.2-runtime-ubuntu18.04",
  conda={
    "channels": ["rapidsai", "conda-forge", "defaults"],
    "dependencies": ["dask", "dask-cuda", "xgboost"],
  },
  cpu=2,
  description="XGBoost GPU Example",
) 