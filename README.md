# Scones Unlimited Image Classification Project

## Project Overview

In this project, I tackled a challenging task as part of the Machine Learning Fundamentals Udacity Nanodegree. My mission revolved around building an image classification model for Scones Unlimited, a scone delivery logistics company. The main objective was to create a model that could automatically recognize the type of vehicle delivery drivers were using, facilitating optimized delivery routing and operations. Distinguishing between bicycles and motorcycles had the potential to significantly enhance delivery efficiency.

As a Machine Learning Engineer, my responsibility was to develop a scalable and dependable image classification model. This model needed to be accessible to other teams, capable of handling increased demand, and equipped with mechanisms to monitor and control performance degradation or drift.

For this endeavor, I turned to AWS SageMaker, an invaluable tool for constructing an image classification model capable of distinguishing between bicycles and motorcycles. This project encompassed not only model deployment but also the creation of supporting services using AWS Lambda functions and the integration of these components into an event-driven application using AWS Step Functions. By the end of this project, I had a portfolio-ready demonstration of my capabilities in constructing and integrating scalable AWS applications driven by machine learning.

## Project Steps Overview

1. **Data Staging**: I kicked off the project by setting up a SageMaker Studio workspace and meticulously preparing the data for machine learning.

2. **Model Training and Deployment**: I successfully trained an image classification model and deployed it as an API endpoint. This phase was a critical step in making the model accessible and usable.

3. **Lambdas and Step Function Workflow**: I created three Lambda functions for distinct tasks: image data retrieval, image classification, and filtering low-confidence inferences. These functions were seamlessly integrated into an event-driven workflow using AWS Step Functions.

4. **Testing and Evaluation**: A crucial aspect of the project involved monitoring the model for errors and creating custom visualizations based on Model Monitor data. This step ensured the model's reliability and effectiveness.

5. **Optional Challenge**: For those seeking an extra challenge, this optional segment allowed me to further enhance my skills and knowledge.

6. **Cleanup Cloud Resources**: To maintain the integrity of the AWS environment, it was essential to ensure that all cloud resources were properly cleaned up when the project reached completion.

## Project Success Criteria

### Train and Deploy a Machine Learning Model

- Setting up a SageMaker Studio workspace was successfully achieved.

- I meticulously completed the ETL (Extract, Transform, Load) phase for data preparation, ensuring the dataset was ready for machine learning.

- The successful training of an image classification model, up to the "Getting ready to deploy" stage, demonstrated my proficiency.

- Model deployment was a pivotal step, and I obtained a unique model endpoint name for future use, facilitating practical applications.

- The functionality of the model was demonstrated effectively by making predictions using a sample image.

### Build a Full Machine Learning Workflow

- I authored three Lambda functions, each with distinct roles: one for retrieving image data, one for image classification, and one for filtering low-confidence inferences.

- Saving the code for each Lambda function in separate Python scripts was essential to maintain clarity and organization.

- Creating an event-driven workflow by integrating the three Lambda functions using AWS Step Functions was a testament to my orchestration skills.

- Exporting the Step Function as JSON and providing a screenshot illustrated the functionality and architecture of the workflow.

### Monitor the Model for Errors

- Extracting model monitoring data from AWS S3 storage was a critical aspect of ensuring the model's reliability.

- Loading Model Monitor data into the notebook allowed me to analyze and visualize the model's performance effectively.

- Developing custom visualizations of Model Monitor data outputs demonstrated my ability to interpret and communicate model behavior.

This project exemplified my expertise in utilizing SageMaker, conducting data preparation, model training, deployment, and building a comprehensive machine learning workflow using AWS services. It was a valuable experience in showcasing my capabilities as a Machine Learning Engineer.