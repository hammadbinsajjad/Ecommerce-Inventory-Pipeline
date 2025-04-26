# Production Setup for Ecommerce Inventory Pipeline

Follow the steps below to set up the production environment for this project:

## 1. Create and Push the Image to GCP Artifact Registry
- Build and push the Docker image to the GCP Artifact Registry.
- Use either Docker or the `gcloud builds submit` command to create and upload the image.
- Ensure the image is tagged appropriately for your project.

## 2. Create a Cloud Run Instance
- Deploy a Cloud Run instance using the image created in the previous step.
- Set up the required environment variables.
- Mount the `kestra_config.yml` file (as a secret) to the `/app/config/kestra_config.yml` path.

## 3. Restrict Instance Count
- Limit the max Cloud Run instance count to 1 to ensure schedulers work as expected.

## 4. Set Up Cloud Run Schedulers
- Configure two Cloud Run schedulers:
    - One to start and load the required flow YAML file into Kestra.
    - Another to start the flow. Ensure the flow-starting trigger includes `?wait=true` in the query string to keep the server running the flow.

## 5. Verify Scheduler Execution
- Force run the schedulers to ensure they are functioning as expected.
- Check the logs and/or modification dates of the tables in BigQuery to confirm that the pipeline has executed successfully.
- Address any issues identified during this verification step.

## Points to Note
    - The environment variables and kestra's config need to be set up correctly; otherwise, issues may occur when the container is deployed or flows are run.
    - Ensure that the Cloud Run instance (compute service account or custom service account) has the necessary permissions to access BigQuery, Artifact Registry and Secrets and any other required services.
    - There are still issues in the production environment (random errors that do not occur in the local environment). But the flow runs successfully.
