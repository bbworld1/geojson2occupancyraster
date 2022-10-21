#!/bin/bash
rio rasterize test2.tif --overwrite --res 0.0000167 --all --default_value 255 < out.geojson
