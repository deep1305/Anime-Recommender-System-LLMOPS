from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Initializing Anime Recommendation Pipeline")

            vector_builder = VectorStoreBuilder(persist_dir=persist_dir, csv_path="")

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Anime Recommendation Pipeline Initialized successfully")
        
        except Exception as e:
            logger.error(f"Error initializing Anime Recommendation Pipeline: {str(e)}")
            raise CustomException("Error during pipeline initialization", e)

    
    def recommend(self, query:str)->str:
        try:
            logger.info(f"Received a query: {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info(f"Generated recommendation: {recommendation}")
            return recommendation
        
        except Exception as e:
            logger.error(f"Error generating recommendation: {str(e)}")
            raise CustomException("Error during recommendation generation", e)