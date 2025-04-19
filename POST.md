We want good electoral boundaries.

But we need to have a reasonable set of criteria for what is meant by "better" - and numerically model this.

I have developed a set of criteria to measure the quality of electoral boundaries.

You can interact with the electoral boundaries here: https://tonghuikang.github.io/electoral-boundaries/

![official](https://i.imgur.com/mNtLvK1.png)


# Modeling Electoral Boundaries as an Assignment Problem

Each constituency is made up of multiple polling districts.

Instead of drawing polling districts and electoral boundaries from scratch, I assume that the polling districts are predetermined.
I used the polling district coordinates collected by [Yudhishthra Nathan and Goh Tiong Ann](https://www.linkedin.com/posts/yudhishthra-nathan-5a2b3816b_ge2025-electoral-map-15th-parliament-of-activity-7317831656130670592-USiD/), and I have made numerous improvements.
The elector size of each polling district is estimated, because I do not have the official counts.

We will also be constrained to keeping the same distribution of member sizes (15 SMCs, 8 4-MP GRCs, 10 5-MP GRCs).

The task is now reduced to grouping these polling districts - each group is a constituency.
Each constituency should have a member size, a name, and the set of polling districts that it comprises.


# Measuring how Well Polling Districts are Assigned

For each constituency, we can measure quality based on:

- Electoral Balance - Electors per member should be close to the mean
- Nonenclavity - Constituencies should not be enclaved within other constituencies
- Compactness - Constituencies should be relatively round in shape
- Convexity - Constituencies should have a convex shape
- Relevance - Constituency names should accurately reflect their geographic locations

The score of each constituency is the average of these scores.
The overall score of the entire assignment is the member size weighted average of constituency scores.

You can find further elaboration [here](https://github.com/tonghuikang/electoral-boundaries/blob/master/SCORING.md).


# Best and Worst Drawn Electoral Boundaries

These are the constituencies ordered from the best drawn to the worst drawn.

| Constituency | Member Size | Elector Balance | Nonenclavity | Compactness | Convexity | Relevance | Constituency Score |
|--------------|-------------|-----------------|--------------|-------------|-----------|-----------|-------------------|
| Punggol | 4 | 91.89 | 100 | 90.87 | 81.94 | 100 | 91.89 |
| Tampines | 5 | 95.95 | 100 | 91.70 | 72.50 | 96.25 | 91.28 |
| Nee Soon | 5 | 93.59 | 100 | 78.55 | 87.88 | 94.00 | 90.80 |
| Sengkang | 4 | 89.65 | 100 | 88.79 | 88.06 | 95.12 | 89.65 |
| Bukit Gombak | 1 | 92.88 | 85.71 | 90.14 | 85.61 | 85.71 | 88.01 |
| Bishan-Toa Payoh | 4 | 86.76 | 100 | 82.38 | 88.26 | 76.57 | 86.76 |
| Jurong East-Bukit Batok | 5 | 99.59 | 100 | 83.61 | 60.87 | 67.62 | 82.34 |
| Sembawang | 5 | 94.36 | 100 | 84.77 | 77.83 | 54.34 | 82.26 |
| Chua Chu Kang | 4 | 82.24 | 100 | 90.77 | 81.70 | 80.06 | 82.24 |
| Queenstown | 1 | 98.36 | 40.00 | 87.85 | 91.12 | 90.91 | 81.65 |
| Marsiling-Yew Tee | 4 | 95.13 | 100 | 88.31 | 73.16 | 48.29 | 80.98 |
| Yio Chu Kang | 1 | 89.38 | 100 | 64.49 | 70.24 | 77.78 | 80.38 |
| Mountbatten | 1 | 80.17 | 83.33 | 85.40 | 82.34 | 57.15 | 77.68 |
| Pasir Ris-Changi | 4 | 88.64 | 52.78 | 91.97 | 84.71 | 68.94 | 77.41 |
| Ang Mo Kio | 5 | 88.02 | 100 | 74.62 | 70.72 | 49.09 | 76.49 |
| West Coast-Jurong West | 5 | 89.49 | 100 | 89.99 | 95.83 | 0.00 | 75.06 |
| Potong Pasir | 1 | 91.87 | 57.14 | 88.21 | 84.25 | 50.00 | 74.29 |
| Jurong Central | 1 | 95.83 | 100 | 80.69 | 88.74 | 0.00 | 73.05 |
| Hougang | 1 | 96.44 | 22.22 | 74.83 | 69.67 | 100 | 72.63 |
| Jalan Kayu | 1 | 96.00 | 92.86 | 83.42 | 87.73 | 0.00 | 72.00 |
| Tanjong Pagar | 5 | 98.43 | 100 | 83.86 | 66.71 | 7.58 | 71.32 |
| Aljunied | 5 | 98.53 | 100 | 88.40 | 69.30 | 0.00 | 71.25 |
| East Coast | 5 | 94.18 | 100 | 74.71 | 86.48 | 0.00 | 71.07 |
| Holland-Bukit Timah | 4 | 92.39 | 100 | 75.42 | 70.19 | 3.54 | 68.31 |
| Kebun Baru | 1 | 78.29 | 95.83 | 83.59 | 82.52 | 0.00 | 68.05 |
| Bukit Panjang | 1 | 84.56 | 0.00 | 74.56 | 76.60 | 100 | 67.14 |
| Marine Parade-Braddell Heights | 5 | 92.65 | 100 | 78.55 | 61.51 | 0.00 | 66.54 |
| Tampines Changkat | 1 | 83.86 | 92.59 | 68.82 | 67.76 | 0.00 | 62.61 |
| Jalan Besar | 4 | 93.45 | 84.06 | 66.73 | 63.34 | 4.76 | 62.47 |
| Pioneer | 1 | 88.66 | 0.00 | 71.50 | 77.59 | 66.67 | 60.88 |
| Radin Mas | 1 | 89.83 | 37.04 | 82.03 | 93.54 | 0.00 | 60.49 |
| Marymount | 1 | 81.80 | 33.33 | 82.90 | 81.58 | 14.29 | 58.78 |
| Sembawang West | 1 | 85.09 | 0.00 | 89.83 | 90.48 | 0.00 | 53.08 |


# Improved Electoral Boundaries According to the Measure

I have written a simple algorithm to optimize the current set of electoral boundaries.
The algorithm renames the constituencies with more relevant names, compares pairs of constituencies to determine which polling districts should be swapped, and repeats this process.

![optimized](https://i.imgur.com/DElL89P.png)

Note that these are not the best possible electoral boundaries.
A better set of electoral boundaries would probably require starting from scratch, rather than optimizing from the official set of electoral boundaries.


# Summary

Here is some feedback I expect:

Why are there some stray lines in your map?
- My electoral boundaries are rendered based on the polling districts that are assigned to them.
- However, the vertices of the polling districts do not exactly align with the adjacent polling districts.
- I plan to write an algorithm to fix this.


I literally live along Jalan Kayu. Why is my constituency's name totally irrelevant?
- Currently I only use MRT location and passenger count to determine the set of names your polling district is relevant to.
- I intend to consider road names as well.


Why does your new electoral boundary look so weird?
- The boundaries look less straight this time, and indeed appear suspicious.
- However, voter patterns are not used in the modeling.
- There are already some penalties for having badly shaped electoral boundaries (compactness, convexity).
- These penalties are likely less severe compared to the improvements in other metrics (relevance, electoral balance).


I think I can draw better electoral boundaries.
- If you could figure out how to run my [code](https://github.com/tonghuikang/electoral-boundaries), you can score your boundaries as well.
- I am happy to assist if you provide me a file similar to this [file](https://github.com/tonghuikang/electoral-boundaries/blob/master/assignments/official_ge_2025.json).


Happy to hear what you think!
