#!/usr/bin/env python

import json

def load_annotations():
    file_path = "annotations/official_ge_2025.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['annotations']

def format_percentage(value):
    if value == 1:
        return "100"
    else:
        return f"{value*100:.2f}"

def print_table(annotations):
    # Sort by constituency score (descending)
    annotations = sorted(annotations, key=lambda x: x['constituency_score'], reverse=True)
    
    # Print table header
    print("| Constituency | Member Size | Elector Balance | Nonenclavity | Compactness | Convexity | Relevance | Constituency Score |")
    print("|--------------|-------------|-----------------|--------------|-------------|-----------|-----------|-------------------|")
    
    # Print table rows
    for annotation in annotations:
        print(f"| {annotation['constituency_name']} | {annotation['member_size']} | {format_percentage(annotation['elector_balance'])} | {format_percentage(annotation['nonenclavity'])} | {format_percentage(annotation['compactness'])} | {format_percentage(annotation['convexity'])} | {format_percentage(annotation['relevance'])} | {format_percentage(annotation['constituency_score'])} |")

if __name__ == "__main__":
    annotations = load_annotations()
    print_table(annotations)