import pandas as pd
import matplotlib.pyplot as plt
from astroquery.gaia import Gaia

query = """
SELECT TOP 1000
    source_id, ra, dec, phot_g_mean_mag, parallax
FROM
    gaiaedr3.gaia_source
WHERE
    parallax > 10
"""

job = Gaia.launch_job(query)
results_table = job.get_results()

df = results_table.to_pandas()

print(df.head())