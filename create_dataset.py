import csv
import random

random.seed(42)

rows = []

for student_id in range(1, 101):
    study_hours = round(random.uniform(1, 8), 1)
    attendance = round(random.uniform(60, 100), 1)
    previous_score = round(random.uniform(40, 90), 1)
    assignments_completed = random.randint(3, 10)
    sleep_hours = round(random.uniform(5, 9), 1)
    participation = round(random.uniform(40, 100), 1)

    final_score = (
        0.30 * previous_score
        + 0.25 * study_hours * 10
        + 0.20 * attendance
        + 0.10 * assignments_completed * 10
        + 0.10 * sleep_hours * 10
        + 0.05 * participation
    )

    final_score += random.uniform(-5, 5)

    final_score = max(0, min(100, final_score))

    rows.append([
        student_id,
        study_hours,
        attendance,
        previous_score,
        assignments_completed,
        sleep_hours,
        participation,
        round(final_score, 1)
    ])

with open("data/student_performance.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "student_id",
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed",
        "sleep_hours",
        "participation",
        "final_score"
    ])

    writer.writerows(rows)

print("Dataset created successfully!")
print("Rows created:", len(rows))