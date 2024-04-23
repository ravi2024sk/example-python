# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).
import pyarrow as pa
import pandas as pd
import numpy as np
from pyarrow import parquet as pq


def handle_query(event, context):
    df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]},
                   index=list('abc'))
    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'example.parquet')
    print("i am here")
