import kaggle

# Download latest version
kaggle.api.authenticate()

path = kaggle.api.dataset_download_files("fxmikf/interior-exterior-scene-classification",path='./data',unzip=True)

print("Path to dataset files:", path)