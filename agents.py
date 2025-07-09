from crewai import Agent
from tools import yt_tool
import os 

from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME'] = "gpt-4o-mini"



# Researcher Agent

blog_researcher = Agent(
    role = "Blog Researcher",
    goal = "Get the relevant video content for the topic {topic} from the YT channel",
    verbose = True,
    memory = True,
    backstory = (
        "You are an expert in understanding videos in the AI Data Science, ML and Gen AI space."
    ),
    tools = [yt_tool],
    allow_delegation = True
)

# Content Writer Agent

blog_writer = Agent(
    role = "Blog Writer",
    goal = "Narrate compelling stories about the video {topic} from YT channel",
    verbose = True,
    memory = True,
    backstory = (
        """
        You are expert in simplifying complex topics and craft engagin narratives that captivate and educate.
        """
    ),
    tools = [yt_tool],
    allow_delegation = False
)
