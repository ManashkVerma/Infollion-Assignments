import pandas as pd

# Load data
df = pd.read_csv("experiment_results.csv")

#Q1: Overall 

control = df[df["variant"] == "control"]
treatment = df[df["variant"] == "treatment"]

control_n = len(control)
treatment_n = len(treatment)

control_rate = control["converted"].mean()
treatment_rate = treatment["converted"].mean()

naive_lift = (treatment_rate - control_rate) * 100

print("=== Q1: OVERALL ===")
print(f"Control:   {control_n} users, {control_rate * 100:.2f}% conversion")
print(f"Treatment: {treatment_n} users, {treatment_rate * 100:.2f}% conversion")
print(f"Naive lift: {naive_lift:.2f} percentage points")


#Q2: By Segment

print("\n=== Q2: BY SEGMENT ===")

segment_results = []

for segment in df["segment"].unique():

    data = df[df["segment"] == segment]

    control = data[data["variant"] == "control"]
    treatment = data[data["variant"] == "treatment"]

    control_n = len(control)
    treatment_n = len(treatment)

    control_rate = control["converted"].mean()
    treatment_rate = treatment["converted"].mean()

    lift = (treatment_rate - control_rate) * 100

    segment_results.append({
        "segment": segment,
        "total": len(data),
        "control_n": control_n,
        "control_rate": control_rate * 100,
        "treatment_n": treatment_n,
        "treatment_rate": treatment_rate * 100,
        "lift_pp": lift
    })

segment_df = pd.DataFrame(segment_results)

print(segment_df.to_string(index=False))


#Q3: Mix-adjusted Lift

print("\n=== Q3: MIX-ADJUSTED LIFT ===")

total_users = len(df)
mix_adjusted_lift = 0

for _, row in segment_df.iterrows():

    weight = row["total"] / total_users
    contribution = weight * row["lift_pp"]

    mix_adjusted_lift += contribution

    print(
        f"{row['segment']}: "
        f"weight={weight:.4f}, "
        f"lift={row['lift_pp']:.2f} pp, "
        f"contribution={contribution:.2f} pp"
    )

print(f"Mix-adjusted lift: {mix_adjusted_lift:.2f} percentage points")


#Q5: Assignment Balance 

print("\n=== Q5: ASSIGNMENT BALANCE ===")

for segment in df["segment"].unique():

    data = df[df["segment"] == segment]

    total = len(data)
    treatment_n = len(data[data["variant"] == "treatment"])
    control_n = len(data[data["variant"] == "control"])

    treatment_pct = treatment_n / total * 100
    control_pct = control_n / total * 100

    print(
        f"{segment}: "
        f"Treatment = {treatment_n} ({treatment_pct:.2f}%), "
        f"Control = {control_n} ({control_pct:.2f}%)"
    )