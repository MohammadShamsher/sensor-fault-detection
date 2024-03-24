Data ingestion Config will give us detail that from this database we gonna extract our data, whats database whats table name etc it will be in data Ingest Config.

Data validation we need to know how much columns we have , its datatypes , Data Drift Detection etc everything will be handled in data validation and all the necessary info that is required by this component will be provided by the config files.


data Transformation you doing so you need one hot encoding ,or scaler these info will be provided by Transformation config.

Model training config will give info which model to train , what hyper parameters has to be used , what wil be the values of Hyper Parameter tuning etc.

Similarly model evaluator will evaluate your this train model with the model already in the production and if your new model is good then only your new model will be accepted and will be pushed to Production else not.