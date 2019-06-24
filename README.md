## Predicting the cause of aviation accidents

My third Metis project. I attempted to predict the cause of aviation accidents (human-caused vs. not) with a logistic regression model.

This uses the NTSB’s [eADMS database](https://app.ntsb.gov/avdata/), converted to a local PostgreSQL database. In `extract_data.ipynb`, relevant features from multiple tables are extracted from that Postgres db to a pandas DataFrame. 

`model.ipynb` contains all of the code for feature generation, model development, and validation. 

I also built a [simple game](http://crashify.herokuapp.com/) in Flask, where features of a random aircraft from the dataset are shown, and the user chooses whether they think the accident was caused by the pilot or by other factors only. Their response is compared to that of the model. It’s fun! The code and templates appear in `flask_app`.