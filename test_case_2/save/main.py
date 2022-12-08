import torch
import joblib

t = torch.Tensor([1.0, 2.0, 3.0])
joblib.dump(t, '../tensor.pkl')
