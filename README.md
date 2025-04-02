In this repository, we open-source the code accompanying the empirical and simulation analyses of *The Impact of Ridesharing Platforms on Healthcare Access*


# Empirical Analysis

## Table of contents of empirical analysis
* [General Info](#general-info-emp)
* [Files](#files-emp)
* [Instruction to produce figures, tables, results](#instr)
* [Data Dictionary](#dic-data)


<a id='general-info-emp'></a>
## General Info 
This repository contains two code files, one as a python script and one as RMarkdown file, along with the data necessary to run them.


<a id='files-emp'></a>
## Files

* [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py): This is the code necessary to create the main data file for the empirical analysis in *The Impact of Ridesharing Platforms on Healthcare Access*. In order to run this code for yourself, you will need a Google API key and will need to update the timestamp of the request to a current timestamp (there is a comment in the file noting this) so the results may vary slightly from ours. The output of this file is saved separately as [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip)

* [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd): This is the RMarkdown file for the empirical analysis in *The Impact of Ridesharing Platforms on Healthcare Access*. 

* [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip): This is the zipped version of the main dataset used in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd). It contains the provider-year observations for every year from 2013-2020 and the variables calculated by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py). Each row records the main variables necessary for our analyses ('Tot_Clms', 'Tot_Benes', 'Bene_Avg_Risk_Scre', 'PRSCRBR_NPI', 'yearindicator'), for each provider in each year. File is zipped for git hub storage, but needs to be unzipped into csv file for use. 

* [Medicare_Part_D_Prescribers_by_Provider_Dataset_2013.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescribers_by_Provider_Dataset_2013.csv): Raw data file from https://data.cms.gov/ for 2013 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [Medicare_Part_D_Prescribers_by_Provider_Dataset_2014.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescribers_by_Provider_Dataset_2014.csv): Raw data file from https://data.cms.gov/ for 2014 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [Medicare_Part_D_Prescribers_by_Provider_Dataset_2015.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescribers_by_Provider_Dataset_2015.csv): Raw data file from https://data.cms.gov/ for 2015 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [Medicare_Part_D_Prescriber_by_Provider_Dataset_2016.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescriber_by_Provider_Dataset_2016.csv): Raw data file from https://data.cms.gov/ for 2016 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [Medicare_Part_D_Prescribers_by_Provider_2017_version2.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescribers_by_Provider_2017_version2.csv): Raw data file from https://data.cms.gov/ for 2017 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [Medicare_Part_D_Prescribers_by_Provider_2018.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescribers_by_Provider_2018.csv): Raw data file from https://data.cms.gov/ for 2018 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [Medicare_Part_D_Prescribers_by_Provider_2019.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescribers_by_Provider_2019.csv): Raw data file from https://data.cms.gov/ for 2018 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [Medicare_Part_D_Prescribers_by_Provider_2020.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Medicare_Part_D_Prescribers_by_Provider_2020.csv): Raw data file from https://data.cms.gov/ for 2018 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to help create [uber_providers_Reproduction.zip](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/uber_providers_Reproduction.zip).

* [zipcode_populations.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/zipcode_populations.csv): Data file containing the zipcode populations of older individuals from 2016 used by [Directions_API_Requests.py](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Directions_API_Requests.py) to randomly draw zipcodes to create the 'mean_duration' variable as described in the paper.

* [Texas_Miles.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/Texas_Miles.csv): Data file containing the miles offered of transportation by non-profit organizations under the FTA's Section 5310 program aggregated at the city level for each month from September 2012 to December 2020. 

* [city_census_data.csv](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Data/city_census_data.csv): Data file containing yearly city census data used in the empirical analysis.  


<a id='instr'></a>
## Instruction to Produce the Empirical Analysis

First run the code chunks in the Reading in Data Section.

* [**Table 1: Summary Statistics**] can be produced by the Summary Statistics Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Figure 2: Histograms of Data**] can be produced by the Histograms of Data Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 2: Parallel Trends**] can be produced by the Parallel Trends - Austin subsection in the Main Results Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 3: The Total Impact on Claims and Beneficiaries**] can be produced by the Total Claims and Total Beneficiaries subsections in the Main Results Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Figure 3: Effect on Total Claims Over Time (with 95% Confidence Intervals)**] can be produced by the code chunks in Time effect subsection in the Main Results Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 4: Heterogeneous Treatment Effects**] can be produced by the code chunks in the HTE Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Figure 4: Synthetic Control: Number of Providers**] can be produced by the code chunk in the Supply Side subsection of the Mechanisms Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 5: The Moderation Effect of Public Transportation Access**] can be produced by the Median of mean walking duration subsection in the Mechanisms Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 6: Mechanism Results**] can be produced by the Traffic SDID Results subsection and Other Cities Analysis subsections in the Mechanisms Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Figure 5: Synthetic Control: Non-Profit Miles Offered**] can be produced by the Synthetic Matching of Transit Data subsection in the Mechanisms Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 7: Robustness of Main Results on Winsorized Data**] can be produced by the Winsorized Results subsection in the Other Robustness Checks Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 8: Robustness of Main Results on Treatment City (Laredo)**] can be produced by the Different Treatment City - Laredo subsection in the Other Robustness Checks Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 9: Parallel Trends Robustness Checks**] can be produced by the Placebo test and Synthetic Did - Provider subsections in the Other Robustness Checks Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).
* [**Table 10: Adversarially Imputed Data Results**] can be produced by the Adversarial Imputation subsection in the Other Robustness Checks Section in [Empirical Analyses.Rmd](https://github.com/nsclyde/Ridesharing-Healthcare-Access/blob/main/Empirical%20Analyses.Rmd).


<a id='dic-data'></a>	
## Data Dictionary

| Column Name               | Meaning                                                                |
|---------------------------|------------------------------------------------------------------------|
| PRSCRBR_NPI               | Provider ID                                                            |
| Bene_Avg_Risk_Scre        | Average Risk Score of Provider's Beneficiaries                         |
| yearindicator             | year                                                                   |
| treatment_group           | indicator if provider is in Austin                                     |
| Tot_Clms                  | total claims for provider-year                                         |
| Tot_Benes                 | total beneficiaries for provider-year                                  |
| AfterReentry              | indicator for years 2018-2020                                          |
| similar_to_austin         | indicator for providers in Austin or control city                      |
| dual_perc                 | % of beneficiaries which are dual                                      |
| avg_pre_dual              | % of dual beneficiaries averaged over 2013-2015                        |
| st_avg_pre_risk           | standardized beneficiary risk averaged over 2013-2015                  |
| mean_duration             | mean walking duration for provider from Google Directions API          |
| Urban                     | indicator for whether provider has less than median mean_duration      |
| switching                 | indicator for if provider switches from Urban group to non-Urban group |
| similar_to_laredo         | indicator for providers in Laredo or control city                      |
| treatment_laredo          | indicator if provider is in Laredo                                     |
| placeboAfter              | placebo indicator for years 2015-2016                                  |
| standardized_elderlypop   | standardized elderly population for each city and year                 |
| standardized_pop          | standardized total population for each city and year                   |
| standardized_medianincome | standardized median income for each city and year                      |



