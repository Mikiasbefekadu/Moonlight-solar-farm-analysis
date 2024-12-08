
# Solar Farm Data Analysis Project

## Project Overview
This project focuses on analyzing solar farm data from Benin, Sierra Leone, and Togo for MoonLight Energy Solutions. The analysis aims to develop a strategic approach to enhance operational efficiency and sustainability through targeted solar investments.

## Business Objective
As an Analytics Engineer, this project:
- Performs analysis of environmental measurements
- Identifies key trends and insights
- Provides data-driven recommendations for high-potential regions for solar installation


## Dataset Description
The dataset contains solar radiation measurement data with the following key parameters:

### Key Variables:
- **Solar Radiation Components:**
  - GHI (W/m²): Global Horizontal Irradiance
  - DNI (W/m²): Direct Normal Irradiance
  - DHI (W/m²): Diffuse Horizontal Irradiance

- **Module Measurements:**
  - ModA (W/m²): Module/sensor A measurements
  - ModB (W/m²): Module/sensor B measurements
  - TModA (°C): Temperature of Module A
  - TModB (°C): Temperature of Module B

- **Environmental Parameters:**
  - Tamb (°C): Ambient Temperature
  - RH (%): Relative Humidity
  - WS (m/s): Wind Speed
  - WD (°N): Wind Direction
  - BP (hPa): Barometric Pressure
  - Precipitation (mm/min)
 
    ## Methodology
       - Cleaning and preparing the data by removing irrelevant columns, clipping negative readings, and handling outliers.
       - Decomposing timestamps into 'Hour' and 'Month' for detailed temporal analysis.
       - Comparing solar panel efficiency and irradiation measurements across the three countries.
       - Assessing wind speed and direction to evaluate their impact on solar panel performance

  ## Tools

| Tool    | Purpose                        |
|---------|--------------------------------|
| Matplotlib | For visualization           |
| Pandas  | For data analysis              |
| Seaborn | For visualization              |
| Numpy   | For numerical operations       |
| Scipy   | For scientific computations    |

## conclusion
#### Sierra Leone emerges as the most favorable location for a solar farm due to its high solar potential, robust correlations between solar metrics, and consistent temporal trends.

## contributor 

##### Mikias Befekadu  - main contributor




