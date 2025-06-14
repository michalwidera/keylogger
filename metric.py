import numpy as np

def extract_timings(keystrokes):
    dwell_times = []
    flight_times = []

    for i, stroke in enumerate(keystrokes):
        dwell = stroke['release_time'] - stroke['press_time']
        dwell_times.append(dwell)
        if i > 0:
            prev_release = keystrokes[i-1]['release_time']
            flight = stroke['press_time'] - prev_release
            flight_times.append(flight)

    return dwell_times, flight_times

def dtw_distance(seq1, seq2):
    n, m = len(seq1), len(seq2)
    dtw = np.full((n+1, m+1), np.inf)
    dtw[0][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(seq1[i-1] - seq2[j-1])
            dtw[i][j] = cost + min(
                dtw[i-1][j],    # wstawienie
                dtw[i][j-1],    # usunięcie
                dtw[i-1][j-1]   # dopasowanie
            )
    return dtw[n][m]

def compare_keystroke_sequences_dtw(seq1, seq2, alpha=0.5):
    dwell1, flight1 = extract_timings(seq1)
    dwell2, flight2 = extract_timings(seq2)

    dwell_dtw = dtw_distance(dwell1, dwell2)
    flight_dtw = dtw_distance(flight1, flight2)

    return alpha * dwell_dtw + (1 - alpha) * flight_dtw

keystrokes1 = [
    {'key': 'a', 'press_time': 0.0, 'release_time': 0.1},
    {'key': 'b', 'press_time': 0.15, 'release_time': 0.25},
    {'key': 'c', 'press_time': 0.30, 'release_time': 0.38}
]

keystrokes2 = [
    {'key': 'a', 'press_time': 0.0, 'release_time': 0.12},
    {'key': 'b', 'press_time': 0.18, 'release_time': 0.28},
    {'key': 'c', 'press_time': 0.35, 'release_time': 0.45}
]

score = compare_keystroke_sequences_dtw(keystrokes1, keystrokes2)
print(f"DTW-based similarity score: {score}")
