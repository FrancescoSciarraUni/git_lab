import numpy as np
import pandas as pd

if __name__ == "__main__":
    print("hello world")
    df = pd.read_csv('../git_test.csv')
    df['Food'] = ['P','G','F','A']
    df.to_csv('../git_test.csv')