from src.Classification import logging
from Classification.pipeline.stage01 import DataIngestionTrainingPipeline
from Classification.pipeline.stage02 import PrepareBaseModelTrainingPipeline
from Classification.pipeline.stage03 import ModelTrainingPipeline
from Classification.pipeline.stage04 import EvaluationPipeline
from Classification.exception import CustomExpection
import sys

STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(f"Error in stage {STAGE_NAME}")
    raise CustomExpection(e,sys)

STAGE_NAME = "Prepare base model"
try: 
   logging.info(f"*******************")
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(f"Error in stage {STAGE_NAME}")
    raise CustomExpection(e,sys)

STAGE_NAME = "Training"
try: 
   logging.info(f"*******************")
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(f"Error in stage {STAGE_NAME}")
    raise CustomExpection(e,sys)

STAGE_NAME = "Evaluation stage"
try:
   logging.info(f"*******************")
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.error(f"Error in stage {STAGE_NAME}")
    raise CustomExpection(e,sys)
