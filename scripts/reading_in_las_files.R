library(rlas)
library(dplyr)
library(sf)

# Read in a las file, which by default is a data.table
y = read.las("C:/Users/anarayanan/Downloads/1714.las")

# Convert to sf data frame
y = as_tibble(y)
y = st_as_sf(y, coords = c("X", "Y")) %>% 
  #explicitly set crs
  st_set_crs(6487)
