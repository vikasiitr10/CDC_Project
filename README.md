Step 1 : Create a Project folder in your drive
Step 2 : Add train(1).xlsx and test.xlsx dataset inside that folder.
Step 3 : Open Google Colab --> create new notebook file
Step 4 : connect your google drive with colab using mount function, you can use this code to mount your drive with colab
        '''
            from google.colab import drive
            drive.mount('/content/drive')
            print("Setup complete!")'''
            
step5: install all required libraries using this line of code
      # !pip install -q torch torchvision opencv-python-headless

PhaseOne : EDA
step 5: Do all necessary EDA to understand data.

### Data Fetching......

step 6: downloading the images of properties using Mapbox Static Images API.
        -- to generate the API key. Go the Mapbox site --> create your account and generate your API key and copy that key.
        -- Create a image folder in your drive to save the images of properties.
        -- Use the data_fetcher.py code inside a new cell to fetch images. Replace the MAPBOX API key with your own key in the code.
        -- hit the run button --> this will download all the images inside the image folder in your drive for training and testing dataset using lat and long feature columns.

### Data Preprocessing....

Step 7: Open a new cell and insert the preprocessing.ipynb code for Data cleaning and feature engineering and hit run button.
-- this will save our preprocessing data in our drive and we can use this data whenever we want.
-- Once it completed we can move towards the Modeling part.
-- before that switch the runtime type to T4:GPU from CPU in google colab setting as our model training requires a powerful GPU --> IMPORTANT.
-- This will reset the colab, Click on Run all cell before moving further.

### Data Modeling......

Step 7: open a new cell and insert model_training.ipynb code and hit run button for The training loop for the multimodal modeling.
-- Hit the run button. This will take some time(Approx 1-2hr) to create our model.
-- Our best model will be saved inside our project folder in drive automatically.
-- To make this process even faster your can import all the images locally and then train your model. this will take much less time compare to using drive. For that you need to change you code a bit. GIVEN CODE GENERATE THE MODEL USING DRIVE ONLY.--> SO it will take 1-2 hr. Keep your laptop turn On for this duration.
-- Once the modeling complete we can move towards the final part, that is Test prediction.

### Test prediction.

Step8 : Open a new cell and insert the test_prediction.ipynb code and insert the run button
-- This will load all the test data along with best model from drive and generate the test_prediction.csv file in our project folder.
-- We can download this file from our drive..

-- For new test data set apart from test.xlsx. fetch their respective images using mapbox API and save it inside the image folder using the naming convention. and Run the test_prediction.ipynb code again.
