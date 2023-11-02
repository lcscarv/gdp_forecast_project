# GDP Growth Forecasting

This project is a Time Series forecasting of GDP growth index. The forecast was done with time series data obtained from the International Monetary Fund (IMF) regarding the GDP index variation of various countries. 
Here, it follows a Feature/Training/Inference Pipeline Architecture (FTI), an MLOps approach that has the proposal to get faster to a minimal working ML system that can be iteratively improved, while following best practices for automated testing, versioning, and monitoring. The overall project is shown in the diagram below.

![diagram](https://github.com/lcscarv/gdp_forecast_project/assets/37702071/624ce4a0-5ed1-4e0f-8e8e-62687ae567e5)


This project was done using Hopsworks for feature store/model registry, Kedro for building pipelines, Jupyter Notebook for experimentation, MLFlow for model tracking and comparison, Google Cloud Plaftorm (GCP) for storing predictions, FastAPI to access and expose data via endpoint and Streamlit app for dashboard creation. 


https://github.com/lcscarv/gdp_forecast_project/assets/37702071/5e2eafe4-a8c0-434f-b81a-bb04c04d8a02


With the interactive dashboard, it's possible to view predictions by region, economic group, and country. Within each category, you can also identify the top five countries with the highest average growth over the four predicted years, based on the specified filters, as well as the predictions for each country within its respective group or region.

## 🚀 Getting Started

These instructions will allow you to obtain a copy of the project running on your local machine for development and testing purposes. To make a copy of this project on your local machine, use the following command:

`git clone https://github.com/lcscarv/gdp_forecast_project`

## 🧬  Code Structure

This project is split into two main components: the Kedro pipeline and the web app.

The **Kedro pipeline** consists of the following structure:

(insert folder structure)

- The **`conf/`** directory, which contains configuration for the project, such as data catalog configuration, parameters, etc.
    
- The **`src`** directory, which contains the source code for the project, including:
    
    - The **`pipelines`** directory, which contains the source code for your pipelines.
        
    - **`settings.py`** file contains the settings for the project, such as library component registration, custom hooks registration, etc. All the available settings are listed and explained in the [project settings chapter](https://docs.kedro.org/en/0.18.3/kedro_project_setup/settings.html).
        
    - **`pipeline_registry.py`** file defines the project pipelines, i.e. pipelines that can be run using `kedro run --pipeline`.
        
    - **`__main__.py`** file serves as the main entry point of the project in [package mode](https://docs.kedro.org/en/0.18.3/tutorial/package_a_project.html#package-your-project).
        
- **`pyproject.toml`** identifies the project root by providing project metadata, including:
    
    - `package_name`: A valid Python package name for your project package
        
    - `project_name`: A human-readable name for your project
        
    - `project_version`: Kedro version with which the project was generated

Which contains the pipelines:

- `feature_pipeline` -> Applies feature engineering over the raw data and stores it in the Hopsworks feature store
- `training_pipeline` -> Trains the Machine Learning model, and registry it into the Hopsworks model registry
- `prediction_pipeline`-> Calls the model from Hopsworks to effectuate predictions, storing it in the GCP bucket.

The **web app** consists of two modules:
- `app-api` ->  Expose the data stored in the GCP bucket via endpoints.
- `app-frontend`-> Creates the interactive dashboard accessing the API endpoints.

To follow the structure in its natural flow, read the folders in the following order:

1. `feature_pipeline`
2. `training_pipeline`
3. `prediction_pipeline`
4. `app-api`
5. `app-frontend` 

## 📋 Pre-requisites

- ##### Hopsworks Feature Store 

First, you need to set up a [Hospworks](https://www.hopsworks.ai/) account to use it as a serverless feature store. After creating an account, you must create a project and a API key for the respective project. For this, go to your Hopsworks account settings and get the API Key from there.

- ##### Google Cloud Platform (GCP)

For Google Cloud Platform, you must do as before, but with a few more steps
- create a project
- create a non-public bucket
- create a service account that has admin permissions to the newly created bucket
- create a service account that has read-only permissions to the newly created bucket
- download a JSON key for the newly created service accounts.

Your `bucket admin service account` should have assigned the following role: `Storage Object Admin`  
Your `bucket read-only service account` should have assigned the following role: `Storage Object Viewer`

After that, remember to update the `.env` files in each folder with your credentials.  

- ##### Docker

In this project was used `Docker version 24.0.6` 

- [Install Docker on Ubuntu.](https://docs.docker.com/engine/install/ubuntu/)
- [Install Docker on Mac.](https://docs.docker.com/desktop/install/mac-install/)
- [Install Docker on Windows.](https://docs.docker.com/desktop/install/windows-install/)

- ##### Environment Setup

You need to create a virtual environment in the project's home directory (if you haven't already).

For Linux:

```bash
python3 -m venv venv
```

For Windows in a Bash shell:

```bash
py -3.8 -m venv venv
```

If you have a version of Python later than 3.8 installed, it's recommended to use Python 3.8. The Python version used in this project is 3.8.10.

Additionally, the virtual environment should be activated every time you open the project using the following commands:

For Linux:

```bash
source venv/bin/activate
```

For Windows in a Bash shell:

```bash
source venv/Scripts/activate
```

For Windows in PowerShell:

```bash
.\venv\Scripts\activate.ps1
```

Make sure you are in the directory where the virtual environment was created. If it's activated correctly, the terminal will display (venv) in front of the username before each command. To deactivate the virtual environment, simply run:

```bash
deactivate
```

We use a `.env` file to store all our credentials. Every module that needs a `.env` file has a `.env.default` in the module's main directory that acts as a template. Thus, you have to run:

```bash
cp .env.default .env
```

... and complete with your information.
### 🔧 Installation

The next step is to install the libraries listed in the "requirements.txt" file. This can be done using pip:

For most cases, use this command:

```bash
pip install -r src/requirements.txt
```

If the above command doesn't work, you can try this alternative:

```bash
python -m pip install -r src/requirements.txt
```

To verify that all the libraries have been installed correctly, you can use either of the following commands:


```bash
pip list
```

or

``` bash
pip freeze
```

These commands will display a list of installed libraries along with their respective versions. Make sure that the required libraries from "requirements.txt" are included in the list.
## ⚙️ Running the project

### 🔩 Pipeline

After everything is set up, just go to the main project folder `gdp-time-series` and run the following command.

```bash
kedro run
```

This command will run all the pipelines, from the data extraction from the API until the storing into the GPC bucket.
### ⌨️ Web App

Fortunately, everything is a lot simpler when setting up the web app. This time, you need to configure only a few credentials.

Go to the API folder and make a copy of the `.env.default` file:

```bash
cd ./app_api
cp .env.default .env
```

Remember to complete the `.env` file with your own variables.

That is it!

Go back to the root directory of your `gdp-time-series` project and run the following docker command, which will build and run all the docker containers of the web app:

```bash
docker compose -f deploy/app-docker-compose.yml --project-directory . up --build
```
## 📦 Deployment

To Be Done.


## ✒️ Author


* **Lucas de Almeida Sabino Carvalho** - *Data Scientist* 
