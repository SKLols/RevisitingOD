import torch
print("CUDA available:", torch.cuda.is_available())
print("Using GPU:", torch.cuda.current_device() if torch.cuda.is_available() else "No GPU")