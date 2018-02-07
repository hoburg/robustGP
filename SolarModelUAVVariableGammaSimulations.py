from Robust import RobustModel
import GPModels as Models
import numpy as np

from RobustGPTools import RobustGPTools
from gpkit.small_scripts import mag
import matplotlib.pyplot as plt

the_model = Models.mike_solar_model(20)
the_nominal_solve = the_model.solve(verbosity=0)
the_gamma = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.29, 0.33, 0.39, 0.45, 0.6, 0.87, 1.05]
the_number_of_iterations = 300
the_min_num_of_linear_sections = 20
the_max_num_of_linear_sections = 30
the_verbosity = 0
factor = 0.79

the_directly_uncertain_vars_subs = [{k: np.random.uniform(v - k.key.pr * v / 100.0, v + k.key.pr * v / 100.0)
                                     for k, v in the_model.substitutions.items()
                                     if k in the_model.varkeys and RobustGPTools.is_directly_uncertain(k)}
                                    for _ in xrange(the_number_of_iterations)]


def different_uncertainty_sets(gamma, directly_uncertain_vars_subs, number_of_iterations,
                               min_num_of_linear_sections, max_num_of_linear_sections, verbosity):

    print ("box, uncertain exponents, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'box', gamma=gamma, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    iter_box = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    print ("box, uncertain coeffients, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'box', gamma=gamma, twoTerm=False, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    coef_box = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    print ("box, simple conservative, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'box', gamma=gamma, simpleModel=True, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    simple_box = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    print ("box, state of art, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'box', gamma=gamma, boyd=True, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    boyd_box = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    print ("elliptical, uncertain exponents, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'elliptical', gamma=gamma, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    iter_ell = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    print ("elliptical, uncertain coeffients, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'elliptical', gamma=gamma, twoTerm=True, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    coef_ell = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    print ("elliptical, simple conservative, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'elliptical', gamma=gamma, simpleModel=True, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    simple_ell = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    print ("elliptical, state of art, gamma = %s, max PWL = %s, "
           "min PWL = %s" % (gamma, min_num_of_linear_sections, max_num_of_linear_sections))
    robust_model = RobustModel(the_model, 'elliptical', gamma=gamma, boyd=True, nominalsolve=the_nominal_solve)
    robust_model_solution = robust_model.robustsolve(verbosity=verbosity,
                                                     minNumOfLinearSections=min_num_of_linear_sections,
                                                     maxNumOfLinearSections=max_num_of_linear_sections,
                                                     linearizationTolerance=0.001)
    simulation = RobustGPTools.probability_of_failure(the_model, robust_model_solution,
                                                      directly_uncertain_vars_subs, number_of_iterations, verbosity=1)
    boyd_ell = (
        simulation[0], simulation[1], robust_model_solution['cost'], robust_model_solution['setuptime'],
        robust_model_solution['soltime'],
        len([cs for cs in robust_model.get_robust_model().flat(constraintsets=False)]),
        robust_model_solution['numoflinearsections'])
    del robust_model, robust_model_solution, simulation

    return iter_box, coef_box, simple_box, boyd_box, iter_ell, coef_ell, simple_ell, boyd_ell

iter_box_prob_of_failure = []
iter_box_obj = []
iter_box_worst_obj = []

coef_box_prob_of_failure = []
coef_box_obj = []
coef_box_worst_obj = []

simple_box_prob_of_failure = []
simple_box_obj = []
simple_box_worst_obj = []

boyd_box_prob_of_failure = []
boyd_box_obj = []
boyd_box_worst_obj = []

iter_ell_prob_of_failure = []
iter_ell_obj = []
iter_ell_worst_obj = []

coef_ell_prob_of_failure = []
coef_ell_obj = []
coef_ell_worst_obj = []

simple_ell_prob_of_failure = []
simple_ell_obj = []
simple_ell_worst_obj = []

boyd_ell_prob_of_failure = []
boyd_ell_obj = []
boyd_ell_worst_obj = []

aeys = []
bs = []
cees = []
ds = []
es = []
fs = []
gs = []
hs = []

the_model = Models.mike_solar_model(20)
for a_gamma in the_gamma:
    a, b, g, c, d, e, h, f = different_uncertainty_sets(factor*a_gamma, the_directly_uncertain_vars_subs,
                                                        the_number_of_iterations, the_min_num_of_linear_sections,
                                                        the_max_num_of_linear_sections, the_verbosity)

    iter_box_prob_of_failure.append(a[0])
    iter_box_obj.append(mag(a[1]))
    iter_box_worst_obj.append(mag(a[2]))
    coef_box_prob_of_failure.append(b[0])
    coef_box_obj.append(mag(b[1]))
    coef_box_worst_obj.append(mag(b[2]))
    simple_box_prob_of_failure.append(g[0])
    simple_box_obj.append(mag(g[1]))
    simple_box_worst_obj.append(mag(g[2]))
    boyd_box_prob_of_failure.append(c[0])
    boyd_box_obj.append(mag(c[1]))
    boyd_box_worst_obj.append(mag(c[2]))
    iter_ell_prob_of_failure.append(d[0])
    iter_ell_obj.append(mag(d[1]))
    iter_ell_worst_obj.append(mag(d[2]))
    coef_ell_prob_of_failure.append(e[0])
    coef_ell_obj.append(mag(e[1]))
    coef_ell_worst_obj.append(mag(e[2]))
    simple_ell_prob_of_failure.append(h[0])
    simple_ell_obj.append(mag(h[1]))
    simple_ell_worst_obj.append(mag(h[2]))
    boyd_ell_prob_of_failure.append(f[0])
    boyd_ell_obj.append(mag(f[1]))
    boyd_ell_worst_obj.append(mag(f[2]))

    aeys.append(a)
    bs.append(b)
    cees.append(c)
    ds.append(d)
    es.append(e)
    fs.append(f)
    gs.append(g)
    hs.append(h)

for i in xrange(len(aeys)):
    print "gamma =", the_gamma[i]
    print aeys[i]
    print bs[i]
    print gs[i]
    print cees[i]
    print ds[i]
    print es[i]
    print hs[i]
    print fs[i]

plt.figure()
plt.plot(the_gamma, iter_box_obj, 'r--', label='Uncertain Exponents')
plt.plot(the_gamma, coef_box_obj, 'bs', label='Uncertain Coefficients')
plt.plot(the_gamma, simple_box_obj, 'g^', label='Simple Conservative')
plt.plot(the_gamma, boyd_box_obj, 'ro', label='State of Art')
plt.xlabel("Uncertainty Set Scaling Factor Gamma")
plt.ylabel("Objective Function")
plt.title("The Average Performance: Box Uncertainty Set")
plt.legend(loc=0)
plt.show()

plt.figure()
plt.plot(the_gamma, iter_box_worst_obj, 'r--', label='Uncertain Exponents')
plt.plot(the_gamma, coef_box_worst_obj, 'bs', label='Uncertain Coefficients')
plt.plot(the_gamma, simple_box_worst_obj, 'g^', label='Simple Conservative')
plt.plot(the_gamma, boyd_box_worst_obj, 'ro', label='State of Art')
plt.xlabel("Uncertainty Set Scaling Factor Gamma")
plt.ylabel("Objective Function")
plt.title("The Worst-Case Performance: Box Uncertainty Set")
plt.legend(loc=0)
plt.show()

plt.figure()
plt.plot(the_gamma, iter_box_prob_of_failure, 'r--', label='Uncertain Exponents')
plt.plot(the_gamma, coef_box_prob_of_failure, 'bs', label='Uncertain Coefficients')
plt.plot(the_gamma, simple_box_prob_of_failure, 'g^', label='Simple Conservative')
plt.plot(the_gamma, boyd_box_prob_of_failure, 'ro', label='State of Art')
plt.xlabel("Uncertainty Set Scaling Factor Gamma")
plt.ylabel("Probability of Failure")
plt.title("The Probability of Failure: Box Uncertainty Set")
plt.legend(loc=0)
plt.show()

plt.figure()
plt.plot(the_gamma, iter_ell_obj, 'r--', label='Uncertain Exponents')
plt.plot(the_gamma, coef_ell_obj, 'bs', label='Uncertain Coefficients')
plt.plot(the_gamma, simple_ell_obj, 'g^', label='Simple Conservative')
plt.plot(the_gamma, boyd_ell_obj, 'ro', label='State of Art')
plt.xlabel("Uncertainty Set Scaling Factor Gamma")
plt.ylabel("Objective Function")
plt.title("The Average Performance: Elliptical Uncertainty Set")
plt.legend(loc=0)
plt.show()

plt.figure()
plt.plot(the_gamma, iter_ell_worst_obj, 'r--', label='Uncertain Exponents')
plt.plot(the_gamma, coef_ell_worst_obj, 'bs', label='Uncertain Coefficients')
plt.plot(the_gamma, simple_ell_worst_obj, 'g^', label='Simple Conservative')
plt.plot(the_gamma, boyd_ell_worst_obj, 'ro', label='State of Art')
plt.xlabel("Uncertainty Set Scaling Factor Gamma")
plt.ylabel("Objective Function")
plt.title("The Worst-Case Performance: Elliptical Uncertainty Set")
plt.legend(loc=0)
plt.show()

plt.figure()
plt.plot(the_gamma, iter_ell_prob_of_failure, 'r--', label='Uncertain Exponents')
plt.plot(the_gamma, coef_ell_prob_of_failure, 'bs', label='Uncertain Coefficients')
plt.plot(the_gamma, simple_ell_prob_of_failure, 'g^', label='Simple Conservative')
plt.plot(the_gamma, boyd_ell_prob_of_failure, 'ro', label='State of Art')
plt.xlabel("Uncertainty Set Scaling Factor Gamma")
plt.ylabel("Probability of Failure")
plt.title("The Probability of Failure: Elliptical Uncertainty Set")
plt.legend(loc=0)
plt.show()
