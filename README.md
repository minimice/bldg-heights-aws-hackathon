## Predicting Building Heights—AWS Hackathon for Good
This repo contains all the information you will need to start working on the
Urban Institute’s challenge to create a novel dataset on building heights.

## Overview
We want you to create a dataset of building heights in Washington, DC, using
input building footprint data, LIDAR data, satellite imagery, and any other
auxiliary data sources you find. Our goal is to generalize the methodologies you
develop to create a national dataset of building footprints and heights, so
please try to keep auxiliary data sources as generalizable as possible. This
work is important for research organizations lie us and city governments to
achieve the following goals:

- understand what kind of housing currently exists in cities  
- create data driven affordable housing plans
- plan effectively for the future growth of cities

The `docs` directory contains an executive summary, a press release, and at 
the bottom of this repo is a FAQ list, which may be helpful for further
background information on this project. 

## Data
We recommend starting with the following datasets to generate building heights
for DC. These datasets can either be accessed in the `data` folder or at the
specified links:

1) Building footprint data: This is a listing of each of the 100,000+ buildings
   in DC and their polygon building footprints. These are the data we want you
   to append with heights. Specifically, we want you to append a column named 
   'ALTITUDE_M' with the height in meters for every row in the data. The data 
   can be found in geojson format at
   `data\training-data\DC_Buildings_Footprint_4326_training.geojson`. Some
   additional notes about these data follow:
     - In many instances, row houses and other contiguous building rooftops could
      not be broken apart using the process methodology and appear as a single
      structure. We want you to predict a single height for every row in the data. 
      So if a group of row houses appear as one building in the data, we want 
      one set of height predictions
    - In accordance with the geojson specification, the file uses the WGS 1984
      geographic projection (CRS: 4362).
    - This is a modified version of the original dataset (which you can find at 
    - `data\training-data\DC_Buildings_Footprint_4326_test.geojson`). We have simply
      stripped one column named `ALTITUDE_M` which are in fact the height in meters 
      of each of the buildings in the dataset. The original dataset actually has the 'true' 
      building heights because DC was one of the very few cities that contracted a
      private firm (and paid millions of dollars) to compute building heights. 
      However the methodology the private firm used to generate the building heights 
      was opaque, not scalable, and prohibitively expensive. We believe their methodology
      is mostly reproducible using the datasets we give you below and we would like you
      to come up with creative methodologies
      However, we would like you to predict the building heights of our modified data so we can make the
      methodology publicly available. It is probably a good idea to can use the test
      dataset to validate the accuracy of your methodologies on the training dataset.
    - Data include structures originally captured from 2005 aerial imagery, with
      updates based on 2010 aerial imagery. Not every building has been updated
      based on 2010 imagery, but you can assume this data is correct as of 2010. 

2) LIDAR point cloud data: Light detection and ranging (LIDAR) is a remote
   sensing method that emits thousands of light pulses a second to measure
   distances between the ground and the height of structures. These data
   essentially contain a series of dense points along with heights. These data
   are available as tiled `.LAS` files on S3. Access instructions and more
   information about these files can be found
   [here](https://docs.opendata.aws/dc-lidar-2018/readme.html). A couple of
   notes on these data:
    - These files are separated into numbered tiled “grids.” You can download a
      shapefile of the grids (and their associated numbers) by going to the link
      above. 
    - For those of you who haven’t worked with LAS files before, there are code
      examples for how to download and read in LAS files as sf dataframes using
      R or as geopandas dataframes using Python in the `scripts` directory.  
    - Some void exist in the data due to data redaction conducted under the
      guidance of the United States Secret Service, and based on the redaction
      areas contained
      [here](https://opendata.dc.gov/datasets/uss-redacted-1-meter-areas?geometry=-77.088%2C38.919%2C-77.043%2C38.925) 
    - This LIDAR data was captured on April 5, 2018
    - These files use the NAD83(2011) projection (CRS 6487).

3) Satellite Imagery Data: DC has collected Orthophotography (high resolution
   aerial imagery) for the city of DC for the past 20 years. You can learn about
   and download all the aerial imagery that DC has collected years
   [here](https://opendata.dc.gov/pages/dc-from-above).  The Aerial Imagery
   datasets are at the bottom of the webpage. We suggest starting with the
   [2010](https://drive.google.com/file/d/0B1Wt8FRXoFfJdWtRdFR0ZDkwb1U/view)
   aerial imagery data to be consistent with the building footprint data that
   was also collected in 2010. Couple of notes about these data: 
   - All the data are available in zipped MrSID formats.
   - Aerial Imagery is available for 2008, 2010 2012, 2013, 2015, and 2017, but
     again we recommend starting with the 2010 data 
   - The 2015 and 2017 data are slightly higher resolution (3 inch) than the
     2010 - 2013 data (6 inch)

## FAQ's

1) This seems hard! How exactly can we predict building heights?
    - On the simplest level, this is a data fusion task. We have data on
      building footprints and heights of points (LIDAR data) throughout the
      city. You simply need to come up with a smart merging scheme to combine
      these two datasets. Note that some buildings may have a lot of overlapping
      LIDAR points, but some will only have a few. You will have to think
      critically about whether to take the min/max/avg of the overlapping point
      heights, whether you should buffer the building footprints, etc. If you
      want you can complicate this task by building machine learning models /
      neural nets to predict building heights from input data, and/or use the
      satellite imagery data in unique/innovative ways, but that is not required
      for a successful submission.

2) Are we required to use all three datasets listed above?
     - No, in fact we expect
   that most teams won't. We do expect that everyone will use the building
   footprint data as those are the buildings we would like you to predict
   heights for. Exactly how you get the building heights is up to you and is
   left intentionally open ended, we've just provided the LIDAR data and the
   satellite imagery data as good reference starting points. 

3) What additional datasets can we bring in to help us with this task?
   - Feel free to find and use any additional datasets that you believe will
     help you with this task. Keep in mind however that our goal is to
     generalize the techniques you develop to create building heights datasets
     for all cities across the US. So keep the auxiliary datasets you bring in
     as generalizable as possible. It is also fine if you don't bring in any
     auxiliary datasets and only work with the datasets we provide above. 

4) How can we check the accuracy of our predicted building heights?
   - As mentioned above, the building footprint data we provide to you in this
     repo is a modified version of the original dataset from the DC Open Data
     Portal. The original dataset actually has the building heights appended.
     You can use the original dataset as test data to see how accurate your
     predictions are and to help you fine tune your approaches. 

5) If a building has a chimney that extends above the height of the roof (or another protrusion of that kind) should we predict the height of the chimney or the height of the roof?
    - This is a judgment call. we recommend predicting the height of the roof
      and not the protrusion. However if the protrusion is very large and
      covers most of the roof, then it might make sense to predict the height of
      the protrusion. This might involve coming up with rules based on the area
      of the protrusion. You can use the original building height dataset (which
      has actual building heights) to guide your decisions

6) If a building has multiple roof heights (eg part of the building is taller that another part) do you want us to predict the maximum height of the building? Average height? Or the separate height of each part of the building?
   - Again this is a judgment call. We  want only one height measurement for every building footprint. We think it's a safe bet to predict the height of the largest area of the roof, but again you can test different rules to see which is most accurate.
    
7) Was every building that was originally captured in 2005 updated in 2010 in the building heights data?
   - No, not necessarily. Only some of the buildings that the third party contract deemed as significantly changed were updated using 2010  imagery. But to make thing simpler you can assume that these are accurate  building footprints as of 2015.

8) Can we use the actual heights from the original footprint data in a training
   set to predict the heights in a test set sampled from the footprint data?
   - Yes, feel free to use supervised learning approaches and use the original
     footprint data as a training set.

9) Do we need to build a frontend app/ User Interface?
   -  This is not required, but if you feel it may aid your final presentation go ahead. 
      In the future we are planning to make a web tool that takes in the input datasets
      and outputs the 'new' dataset with building heights appended and displays a portion 
      of the data on a map. But again this is not required, we are really interested in the
      methodologies you develop to predict building heights.

10) If we're using AI / ML models, how do we generate input features?
      - It is up to you to use the input datasets you choose to generate input features - feel free to be creative! Note that you will need to generate input features on a per building basis. Examples of input features are functions of the intersecting LIDAR points(like the average heights, variance, SD of all intersecting points), functions of LIDAR points within a specific buffer around each building, and functions of satellite imagery associated with that building (if you choose to use this input data)
