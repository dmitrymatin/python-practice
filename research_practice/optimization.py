from scipy.optimize import linprog

'''
scipy.optimize.linprog(
    c,
    A_ub=None,
    b_ub=None,
    A_eq=None,
    b_eq=None,
    bounds=None,
    method="simplex",
    callback=None,
    options={
        "maxiter": 5000,
        "disp": False,
        "presolve": True,
        "tol": 1e-12,
        "autoscale": False,
        "rr": True,
        "bland": False,
    },
    x0=None,
)
'''

k_F = [-320, -290] 	#прибыль - коэффециент 
k_M = [[0.12, 0.24],  #расход - коэффециент 
       [0.22, 0.09],  #расход - коэффециент 
       [0.14, 0.06]]  #расход - коэффециент 
res_M = [120, 		#M1 - ресурсы
         80,  		#M2 - ресурсы
         60]  		#M2 - ресурсы
opt = linprog (c=k_F, A_ub=k_M, b_ub=res_M, method="simplex")
print(opt)
