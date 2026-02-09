# Climate-Resilient-REI summary
The goal of this project is to leverage my interest in commerical real estate investment with enhancing data like natural disaster risk, etc.

At this time, I am evaluating data sources and shapes to create a perspective on a real value api deliverable. WIP ideas:
- Recent natural disasters in an MSA will impact prices for 1+ years
- Knowing the natural disater history of your target MSA gives you better due diligigence questions -> no required process or reporting for flood damage. 
- Apply a weighting system of FEMa risk score to price to rent score

MVP - Start by correlating House Price and FEMA Risk datasets.

# Potential Data Sources
FEMA Risk Index: 
- https://www.fema.gov/vi/flood-maps/products-tools/national-risk-index - annually 
Population Trends:
- ? https://data.census.gov/
New Construction Trends: 
- Zillow New Construction Sales Count: https://www.zillow.com/research/data/ - Downloadable csv - monthly
- US Census Building Permist Survey: https://www.census.gov/construction/bps/current.html -> monthly
House Price Trends: 
- Zillow Home Value Index (ZHVI): https://www.zillow.com/research/data/ - Downloadable csv - monthly
Rent Trends: 
- Zillow Observed Rent Index (ZORI): https://www.zillow.com/research/data/ - Downloadable csv - monthly

# WIP Data Questions:
Should we reduce Markets covered to keep free-tier?
At what level do I want to join the data? Zip code? MSA?

# project outline - Subject to Change
apartment-data-pipeline/
├── etl_pipeline/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── dag.py
│   ├── config.py
│   └── requirements.txt
│
├── streaming/
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   └── spark_streaming.py
│
├── ai_search/
│   ├── embedding_model.py
│   ├── vector_store.py
│   ├── search_rag.py
│   ├── qa_bot.py
│   └── requirements.txt
│
├── api/
│   ├── app.py
│   ├── routes.pyS
│   ├── models.py
│   ├── config.py
│   └── requirements.txt
│
├── infra/
│   ├── docker-compose.yml
│   ├── Dockerfile.api
│   ├── Dockerfile.etl
│   ├── Dockerfile.airflow
│   ├── kubernetes.yaml
│   └── terraform.tf
│
├── notebooks/
│   ├── exploration.ipynb
│   └── embedding_demo.ipynb
│
├── dashboard/
│   ├── market_trends.twb
│   ├── user_behavior.pbix
│   └── dashboard_queries.sql
│
├── data/
│   ├── listings_sample.json
│   ├── search_events.csv
│   └── rental_transactions.csv
│
├── tests/
│   ├── test_transform.py
│   └── test_api.py
│
├── .env.example
├── Makefile
├── README.md
└── PRODUCTION_NOTES.md
