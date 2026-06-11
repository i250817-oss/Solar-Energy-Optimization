# --------------------------------
#  Ahmad Ali            
#  Liaba Naveed         
#  Muhammad Osaid Zahid 
# --------------------------------


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from scipy import integrate
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')


#Read data from csv using pandas
df = pd.read_excel("Dataset_30days.xlsx")
df.head()

#define data fragment
X = df[['G_Irradiance', 'Temperature', 'Theta_deg']]
y = df['Power']

#SPlit 100/400 for testing and training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

#Define regression
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)


# Coefficients
b0 = lr.intercept_
bG, bT, bθ = lr.coef_

print("So the model is:")
print(f"P = {b0:.4f} + {bG:.4f}·G + {bT:.4f}·T + {bθ:.4f}·θ")
print(f"R**2 = {r2_score(y_test, y_pred):.4f}")



#   TASK 1
#Since its a linear model, min max will be at the corners so we extract them
corners = list(product([200, 1000], [15, 45], [0, 60]))
powers  = [lr.predict([[G, T, th]])[0] for G, T, th in corners]

max_i = np.argmax(powers)
min_i = np.argmin(powers)

print("\nTASK 1: MAX AND MIN POWER ")
print("MAX:", round(powers[max_i], 2), "W  at  G=", corners[max_i][0], "T=", corners[max_i][1], "θ=", corners[max_i][2])
print("MIN:", round(powers[min_i], 2), "W  at  G=", corners[min_i][0], "T=", corners[min_i][1], "θ=", corners[min_i][2])

#Strongest variable is which had the largest absolute coefficient
names = ['G_Irradiance', 'Temperature', 'Theta_deg']
print("Strongest influence:", names[np.argmax(np.abs(lr.coef_))])



#   TASK 2
#Gradients would simply be the coefficients cause its a linear function
G0, T0, θ0 = df['G_Irradiance'].mean(), df['Temperature'].mean(), df['Theta_deg'].mean()
grad = np.array([bG, bT, bθ])

print("\nTASK 2: GRADIENT")
print(f"Operating point: G={G0:.1f}, T={T0:.1f}, θ={θ0:.1f}")
print(f"∇P = [{bG:.4f}, {bT:.4f}, {bθ:.4f}]")
print("Largest component:", names[np.argmax(np.abs(grad))])

#Unit vector would be the direction of steepest increase
unit = grad / np.linalg.norm(grad)
print(f"Fastest increase direction (unit vector): [{unit[0]:.4f}, {unit[1]:.4f}, {unit[2]:.4f}]")



#     TASK 3
#Negative gradient is the direction of fastest power decrease
neg_grad = -grad

print("\nTASK 3: STEEPEST DESCENT ")
print(f"−∇P = [{neg_grad[0]:.4f}, {neg_grad[1]:.4f}, {neg_grad[2]:.4f}]")
print("Power drops fastest when G decreases (cloud cover) and θ increases")




#   TASK 4
#We take a scenario where irradiance drops, temperature is steady and angle slightly increases
d = np.array([-1.0, 0.0, 0.5])
d_unit = d / np.linalg.norm(d)
dir_deriv = np.dot(grad, d_unit)

print("\n TASK 4: DIRECTIONAL DERIVATIVE")
print(f"Direction (ΔG=-1, ΔT=0, Δθ=+0.5): {d_unit.round(4)}")
print(f"D_u P = {dir_deriv:.4f} W per unit step")
print("Negative meaning power is decreasing ")



#   TASK 5
#Integrate P(G,T,θ) over full operating envelope
G1, G2   = 200, 1000
T1, T2   = 15,  45
th1, th2 = 0,   60

def P(th, T, G):
    return b0 + bG*G + bT*T + bθ*th

result, _ = integrate.tplquad(P, G1, G2, T1, T2, th1, th2)
avg_power = result / ((G2-G1) * (T2-T1) * (th2-th1))

print("\nTASK 5: TRIPLE INTEGRAL")
print(f"∭ P dG dT dθ = {result:.2f}")
print(f"Average power over operating envelope = {avg_power:.2f} W")



#    TASK 6

locations = {
    "Desert"     : [950, 42, 10],
    "Coastal"    : [700, 28, 25],
    "High-Alt."  : [900, 18,  5],
    "Urban"      : [550, 35, 40],
}

print("\nTASK 6: LOCATION PERFORMANCE")
loc_powers = {name: lr.predict([vals])[0] for name, vals in locations.items()}
for name, p in loc_powers.items():
    print(f"  {name:<12}: {p:.2f} W")
print("Best :", max(loc_powers, key=loc_powers.get))
print("Worst:", min(loc_powers, key=loc_powers.get))

#  GRAPHS 
# Actual vs Predicted
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel('Actual Power (W)')
plt.ylabel('Predicted Power (W)')
plt.title('Actual vs Predicted')
plt.show()

# Irradiance vs Power
plt.scatter(df['G_Irradiance'], df['Power'], alpha=0.5)
plt.xlabel('G_Irradiance (W/m²)')
plt.ylabel('Power (W)')
plt.title('Irradiance vs Power')
plt.show()





