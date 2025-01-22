import json

# Paths to your JSON files
file1 = " "  # Replace with your actual adaptation JSON file path
file2 = " "  # Replace with your actual question_only JSON file path

# Load the IDs from each file
with open(file1, "r") as f1, open(file2, "r") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

# Convert IDs lists to sets for set operations
ids1 = set(data1["correct_ids"])
ids2 = set(data2["correct_ids"])

# Calculate differences
ids_in_file1_not_in_file2 = ids1 - ids2
ids_in_file2_not_in_file1 = ids2 - ids1

output_w2r_path = ""
output_r2w_path = ""
# Save to JSON files
with open(output_w2r_path, "w") as w2r_file:
    json.dump({"total_ids_in_adaptation_not_in_question_only": len(ids_in_file1_not_in_file2), "ids": sorted(ids_in_file1_not_in_file2)}, w2r_file, indent=4)

with open(output_r2w_path, "w") as r2w_file:
    json.dump({"total_ids_in_question_only_not_in_adaptation": len(ids_in_file2_not_in_file1), "ids": sorted(ids_in_file2_not_in_file1)}, r2w_file, indent=4)

# Optional: Print summary
print("Summary of ID comparison:")
print(f"1. Total IDs in adaptation but not in question_only: {len(ids_in_file1_not_in_file2)}")
print(f"2. Total IDs in question_only but not in adaptation: {len(ids_in_file2_not_in_file1)}")
print(f"3. Total IDs in both files: {len(ids1 & ids2)}")
print(f"4. Total correct in adaptation: {len(ids1)}")
print(f"5. Total correct in question_only: {len(ids2)}")

# Calculate wrong2right and right2wrong rate
wrong2right_rate = len(ids_in_file1_not_in_file2) / (300 - len(ids2)) * 100
right2wrong_rate = len(ids_in_file2_not_in_file1) / len(ids2) * 100

print(f"6. Wrong2Right_Rate: {wrong2right_rate}")
print(f"7. Right2Wrong_Rate: {right2wrong_rate}")
