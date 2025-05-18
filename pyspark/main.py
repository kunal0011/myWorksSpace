from pyspark import SparkConf
from pyspark import SparkContext

try:
    # Configure Spark for local execution
    conf = SparkConf() \
        .setAppName('spark-local') \
        .setMaster('local[*]') \
        .set('spark.driver.host', 'localhost')

    sc = SparkContext(conf=conf)


    def some_function(x):
        # Packages are imported and available from your bundled environment.
        from sklearn import __version__ as sklearn_version  # Changed import
        import pandas as pd
        import numpy as np

        # Use the libraries to do work
        return np.sin(x) ** 2 + 2


    rdd = (sc.parallelize(range(1000))
        .map(some_function)
        .take(10))

    print(rdd)

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Properly stop SparkContext
    if 'sc' in locals():
        sc.stop()
