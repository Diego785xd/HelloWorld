import json
import pandas as pd
class tags:
    def __init__(self):
        self.tags = self.addTags()
        self.df = pd.DataFrame(self.tags)

    def addTags(self):
        with open("tags.json", 'r') as f:
            tags_dict = json.load(f)
        try:
            phrases = tags_dict['frases']
            return phrases
        except KeyError:
            print(f"No tag 'frases' found in tags.json config file at method __init__ in class tags")
            raise KeyError
        except Exception as e:
            print(f"Error at method __init__ in class tags: {e}")
            raise Exception
