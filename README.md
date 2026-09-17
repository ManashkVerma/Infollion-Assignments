# Onboarding Experiment Investigation

## 1. Overall result

- Control: **7,136 users**
- Treatment: **6,864 users**
- Control conversion: **19.815022%**
- Treatment conversion: **26.427739%**

**Lift = 26.427739% - 19.815022% = 6.612716506214261 pp**

---

## 2. Segment result

| Segment | Control N | Control Rate | Treatment N | Treatment Rate | Lift |
|---|---:|---:|---:|---:|---:|
| app_store | 925 | 8.756757% | 960 | 20.000000% | +11.243243 pp |
| influencer | 119 | 23.529412% | 131 | 16.793893% | -6.735519 pp |
| organic | 1,298 | 35.285054% | 2,917 | 35.070278% | -0.214776 pp |
| paid_search | 3,353 | 15.180435% | 1,459 | 14.393420% | -0.787015 pp |
| referral | 1,441 | 23.455933% | 1,397 | 26.270580% | +2.814646 pp |

**Segment I would not trust: influencer.**  
It has only **250 users**, so its result is based on a smaller sample.

---

## 3. Mix-adjusted lift

I multiplied each segment's lift by its share of all users.

The result is:

**1.63 percentage points**

This is lower than the **6.61 pp** naive lift because the treatment and control groups have different segment mixes.

---

## 4. Segment with a positive effect

**app_store**

- Control: **8.756757%**
- Treatment: **20.000000%**
- Lift: **+11.243243 pp**

It also has **1,885 users**, with treatment and control almost evenly split.

---

## 5. Assignment check

The main issue is the difference in treatment share:

- **organic:** 69.21% treatment
- **paid_search:** 30.32% treatment

The other segments are close to 50/50.

So, the treatment and control groups are **not evenly distributed across segments**.
