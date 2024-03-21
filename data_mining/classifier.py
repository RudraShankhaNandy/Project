from extractor import FBextractor as fbe
import nltk
nltk.download('punkt')

extract_paras = fbe("website","id","password")


