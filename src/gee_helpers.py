"""Earth Engine initialization and shared helpers."""
import ee

GEE_PROJECT = 'black-octagon-291810'


def init_ee():
    """Initialize Earth Engine. Prompts auth if needed."""
    try:
        ee.Initialize(project=GEE_PROJECT)
    except Exception:
        ee.Authenticate()
        ee.Initialize(project=GEE_PROJECT)
    print(f"Earth Engine initialized with project: {GEE_PROJECT}")