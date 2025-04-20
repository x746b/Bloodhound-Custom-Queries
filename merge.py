import json

# Load the two BloodHound custom query files
with open('./customqueries1.json') as f1, open('customqueries2.json') as f2:
    bh1 = json.load(f1)
    bh2 = json.load(f2)

# Merge the "queries" lists
merged = {
    "queries": bh1.get("queries", []) + bh2.get("queries", [])
}

# Write out the merged file
output_path = './customqueries.json'
with open(output_path, 'w') as fout:
    json.dump(merged, fout, indent=4)

print(f"Merged BloodHound queries saved to: {output_path}")
