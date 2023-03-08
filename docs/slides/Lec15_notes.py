import numpy as np
import pandas as pd
import seaborn as sns

## Demo 1


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.pipeline import make_pipeline, make_union
from sklearn.compose import make_column_selector, make_column_transformer

books = pd.read_csv("https://sta663-sp22.github.io/slides/data/daag_books.csv")

p = make_pipeline(
  make_column_transformer(
    (OneHotEncoder(drop="first"), make_column_selector(dtype_include=object)),
    remainder = "passthrough"
  ),
  PolynomialFeatures(degree=2, include_bias=False, interaction_only=True),
  LinearRegression()
)

#p.fit(X = books.drop(["weight"], axis=1))
#p.transform(books.drop(["weight"], axis=1))
#p.get_feature_names_out()

p.fit(
  X = books.drop(["weight"], axis=1),
  y = books.weight
)

p.named_steps["linearregression"].intercept_
p.named_steps["linearregression"].coef_
p.get_feature_names_out()
p[:-1].get_feature_names_out()
p.get_params().keys()

