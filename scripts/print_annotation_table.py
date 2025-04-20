#!/usr/bin/env python

import json


def load_scores():
    file_path = "scores/official_ge_2025.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["scores"]


def format_percentage(value):
    if value == 1:
        return "100"
    else:
        return f"{value*100:.2f}"


def print_table(scores):
    # Sort by constituency score (descending)
    scores = sorted(scores, key=lambda x: x["constituency_score"], reverse=True)

    # Print table header
    print("| Constituency | Member Size | Elector Balance | Nonenclavity | Compactness | Convexity | Relevance | Constituency Score |")
    print("|--------------|-------------|-----------------|--------------|-------------|-----------|-----------|-------------------|")

    # Print table rows
    for score_data in scores:
        print(
            f"| {score_data['constituency_name']} | {score_data['member_size']} | {format_percentage(score_data['elector_balance'])} | {format_percentage(score_data['nonenclavity'])} | {format_percentage(score_data['compactness'])} | {format_percentage(score_data['convexity'])} | {format_percentage(score_data['relevance'])} | {format_percentage(score_data['constituency_score'])} |"
        )


if __name__ == "__main__":
    scores = load_scores()
    print_table(scores)
