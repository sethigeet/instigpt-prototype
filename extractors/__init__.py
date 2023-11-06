from dotenv import load_dotenv
from .utils import get_env_var

load_dotenv()

RESOBIN_SESSIONID = get_env_var("RESOBIN_SESSIONID")
