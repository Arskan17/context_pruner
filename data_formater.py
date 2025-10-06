import json
import orjson
from concurrent.futures import ProcessPoolExecutor
import os
import uuid
import re

class DataFormatter:

    def __init__(self):
        pass

    def transform_file(self, input_line):
        contexts = re.split(r'\. |\n\n', input_line.get("answer", ""))
        query_id = str(uuid.uuid4())
        output_line = {
            "answers": [],
            "passages": [
                {
                    "is_selected": 0,
                    "url": f"dataset/{query_id}",
                    "passage_text": context
                } for context in contexts
            ],
            "query": input_line.get("query", ""),
            "query_id": query_id,
            "query_type": "question_answering",
            "wellFormedAnswers": []
        }

        self.write_line_to_file(output_line)

    def write_line_to_file(self, line):
        with open('german_rag_transformed_reformated_MS-MARCO_v1.1.jsonl', 'a', encoding='utf-8') as f:
            f.write(json.dumps(line, ensure_ascii=False) + '\n')

    def write_line_to_file_cuncurrently(self, line):
        with open('german_rag_transformed_reformated_cuncurrent_MS-MARCO_v1.1.jsonl', 'a', encoding='utf-8') as f:
            f.write(json.dumps(line, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    formatter = DataFormatter()
    
    with open('german_rag_transformed.jsonl', 'r', encoding='utf-8', errors='ignore') as file:
        [formatter.transform_file(orjson.loads(line)) for line in file if line.strip()]