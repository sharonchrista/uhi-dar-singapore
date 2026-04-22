import ee, geemap, geopandas as gpd, rasterio, matplotlib, pandas as pd, numpy as np

print('All imports OK')
print(f'ee: {ee.__version__}')
print(f'geemap: {geemap.__version__}')
print(f'geopandas: {gpd.__version__}')
print(f'rasterio: {rasterio.__version__}')

try:
    ee.Initialize(project='g4g2023-wg')
    print('GEE initialized with g4g2023-wg')
except Exception as e:
    print(f'g4g2023-wg failed: {e}')
    try:
        ee.Initialize()
        print('GEE initialized with default project')
    except Exception as e2:
        print(f'GEE init failed completely — run: earthengine authenticate')
        print(f'Error: {e2}')