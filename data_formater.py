import json
from concurrent.futures import ProcessPoolExecutor
import os
import uuid

class DataFormatter:

    def __init__(self):
        pass

    def transform_file(self, input_line):
        output_line = {
            "answers": [input_line.get("answer", "")],
            "passages": [],
            "query": input_line.get("query", ""),
            "query_id": str(uuid.uuid4()),
            "query_type": "Question_Answering",
            "wellFormedAnswers": []
        }

        self.write_line_to_file(output_line)

    def write_line_to_file(self, line):
        with open('german_rag_transformed_reformated1.jsonl', 'a', encoding='utf-8') as f:
            f.write(json.dumps(line, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    formatter = DataFormatter()
    
    with open('german_rag_transformed.jsonl', 'r', encoding='utf-8', errors='ignore') as file:
        # lines = [json.loads(line) for line in file]
        [formatter.transform_file(json.loads(line)) for line in file]
    # with ProcessPoolExecutor() as executor:
    #     executor.map(formatter.transform_file, lines)
    # for line in lines:
    #     formatter.transform_file(line)