import json

# Function to normalize strings
def normalize_str(answer):
    if isinstance(answer, str):
        return [answer.strip().lower()]
    return [str(answer).strip().lower()]

# Function to evaluate open-ended questions
def eval_open(gold_i, pred_i):
    correct = False
    if isinstance(gold_i, list):
        norm_answers = []
        for answer in gold_i:
            norm_answers.extend(normalize_str(answer))
    else:
        norm_answers = normalize_str(gold_i)

    for pred in pred_i:  # pred is already normalized
        if isinstance(pred, str):  # check if normalized answer is in the prediction
            for norm_ans in norm_answers:
                if isinstance(norm_ans, str) and norm_ans in pred:
                    correct = True
                    break
        else:  # for numeric comparison
            if pred in norm_answers:
                correct = True
                break
    return correct

# Input and output file paths
input_file = ""
output_file = ""

correct_ids = []

with open(input_file, "r") as f:
    for line in f:
        entry = json.loads(line.strip())
        if entry["mmmu_acc"]["parsed_pred"] == "No Answere Found":
            continue
        question_type = entry.get("question_type", "open")
        answer = entry["mmmu_acc"]["answer"]
        parsed_pred = entry["mmmu_acc"]["parsed_pred"]

        if question_type == "open":
            pred_list = normalize_str(parsed_pred) if isinstance(parsed_pred, str) else parsed_pred
            if eval_open(answer, pred_list):
                correct_ids.append(entry["doc"]["id"])
        else:
            if answer == parsed_pred:
                correct_ids.append(entry["doc"]["id"])

with open(output_file, "w") as f:
    json.dump({"correct_ids": correct_ids}, f, indent=4)

print(f"Matched IDs have been saved to {output_file}")
