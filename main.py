from models.model import predict_price
import pandas as pd

df = pd.read_csv("dataset/test_dataset.csv")

print(predict_price("This is a test news"))
print(predict_price(df))