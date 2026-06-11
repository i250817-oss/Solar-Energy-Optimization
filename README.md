# ☀️ Solar Energy Optimization
### Multivariable Modeling of Photovoltaic Panel Efficiency

| Course | University | Semester | R2 Score |
|--------|------------|----------|----------|
| MT1008 Multivariable Calculus | FAST NUCES Islamabad | Spring 2026 | 0.9617 |

---

## 👥 Our Team

| Role | Name | ID |
|------|------|----|
| Group Leader | Ahmad Ali | 25i-0817 |
| Handwritten Solutions | Liaba Naveed | 25i-0818 |
| Python Developer | Muhammad Osaid Zahid | 25i-0524 |

**Submitted To:** Ms. Iqra Arshad, Instructor Multivariable Calculus

---

## About This Project

We built this project for our second semester Multivariable Calculus course at FAST NUCES Islamabad. The real question that drove everything was:

> "How do you build a function when no formula is given to you?"

That curiosity led us to Multiple Linear Regression. We had a 30-day dataset with three input variables and we used regression to find the best fit model. Once we had our function, we applied calculus tools to analyze and optimize it.

---

## The Model We Built

```
P(G, T, θ) = 0.808·G  −  2.548·T  −  4.9204·θ  +  223.0904
```

| Variable | Description | Range |
|----------|-------------|-------|
| G | Solar Irradiance | 200 to 1000 W/m2 |
| T | Panel Temperature | 15 to 45 C |
| θ | Angle of Incidence | 0 to 60 degrees |
| P | Power Output | Watts |

---

## The Six Tasks We Solved

### Task 1 : Maximum and Minimum Power

Since the model is linear all partial derivatives are constant and never zero. So no interior critical points exist. We checked all 8 corner points of the domain.

| Condition | G | T | θ | Power |
|-----------|---|---|---|-------|
| Maximum | 1000 W/m2 | 15 C | 0 degrees | 992.87 W |
| Minimum | 200 W/m2 | 45 C | 60 degrees | minus 25.19 W |

---

### Task 2 : Gradient Vector

```
∇P  =  ( 0.808,  −2.548,  −4.9204 )
```

The angle of incidence has the strongest influence on power because its coefficient has the largest magnitude. Irradiance increases power while temperature and angle both decrease it.

---

### Task 3 : Steepest Descent

```
−∇P  =  ( −0.808,  2.548,  4.9204 )
```

Power drops fastest when irradiance decreases and angle increases. This matches real world situations like sunset or cloud cover.

---

### Task 4 : Directional Derivative

We chose a direction where irradiance drops and angle increases while temperature stays the same.

```
u  =  ( −1, 0, 1 )
Directional Derivative  ≈  −4.049 W per unit step
```

The negative value means power is decreasing in that direction. This signals a need for battery storage dispatch in a grid.

---

### Task 5 : Triple Integral

```
Domain:  G in [200, 1000]   T in [15, 45]   θ in [0, 60]

Total Integral   =  696,727,296
Average Power    =  482.54 W
```

---

### Task 6 — Location Performance

| Rank | Location | G W/m2 | T C | θ degrees | Power |
|------|----------|---------|-----|-----------|-------|
| 1 | Desert | 950 | 40 | 10 | 839.57 W |
| 2 | High Altitude | 900 | 15 | 20 | 813.66 W |
| 3 | Coastal | 700 | 28 | 25 | 594.34 W |
| 4 | Urban | 500 | 35 | 35 | 365.70 W |

---

## Tools We Used

| Tool | Purpose |
|------|---------|
| Python 3.14.4 | Core programming language |
| scikit-learn | Multiple linear regression |
| scipy | Triple numerical integration |
| numpy | Math and vector operations |
| matplotlib | Graphs and plots |
| pandas | Reading the Excel dataset |
| VS Code and Google Colab | Writing and running the code |
| Overleaf LaTeX | Final report formatting |
| Draw.io | Flowcharts |

---

## Who Did What

**Ahmad Ali — Group Leader**
He led the whole project, formed the complete LaTeX document, built and tested the Python solution, and was part of the brainstorming for how to model the function.

**Liaba Naveed**
She wrote all the handwritten solutions for every task with full working shown and also took part in the brainstorming sessions.

**Muhammad Osaid Zahid**
He wrote, tested, and documented the Python code from scratch explaining every single line. He also joined the brainstorming discussions.

All three of us studied multiple linear regression from the ground up together and then applied it as a team.

---

## What We Learned

We learned how to build a predictive function from raw data when no formula exists. Multi linear regression gave us the best fit line across three variables at once. We also learned how calculus tools connect directly to real world engineering problems like solar energy.

The most important insight: proper panel alignment matters more than irradiance or temperature when it comes to improving solar efficiency.

---

## Project Contents

```
Solar Energy Optimization
    main.py                     Python source code fully commented
    Dataset_30days.xlsx         30 day solar panel dataset
    MVC_Project_Report.pdf      Full LaTeX report 44 pages
    README.md                   This file
```

---

BEST MVC PROJECT OF ALL TIME
We learned a lot. Thanks.

FAST NUCES Islamabad | Spring 2026
