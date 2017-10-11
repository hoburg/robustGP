from RobustGP import RobustGPModel
import GPModels
import numpy as np
# model = GPModels.simpleWing()
model = GPModels.mike_solar_model()
gammas = list(np.linspace(0.9, 1.5, 10))
printing_list = []
for gamma in [1]:  # gammas:
    printing_list.append("________________________________________________________________________")
    print "box boyd:"
    model_box_boyd = RobustGPModel(model, gamma, 'box', boyd=True)
    try:
        sol_model_box_boyd = model_box_boyd.solve(r_min=30, r_max=30, verbosity=1)
        st = ''
        if model_box_boyd.lower_approximation_used:
            st = 'box boyd infeasible, lower approximation used:'
        printing_list.append(st + "box boyd %s, gamma = %s, setup time = %s, solve time = %s" %
                             (sol_model_box_boyd['cost'], gamma, model_box_boyd.setup_time,
                              sol_model_box_boyd['soltime']))
    except:
        printing_list.append('box boyd infeasible')

    print "ell boyd:"
    model_ell_boyd = RobustGPModel(model, gamma, 'elliptical', boyd=True)
    try:
        sol_model_ell_boyd = model_ell_boyd.solve(r_min=30, r_max=30, verbosity=1)
        st = ''
        if model_ell_boyd.lower_approximation_used:
            st = 'ell boyd infeasible, lower approximation used:'
        printing_list.append(st+"elliptical boyd %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_ell_boyd['cost'], gamma, model_ell_boyd.setup_time,
                                sol_model_ell_boyd['soltime']))
    except:
        printing_list.append('elliptical boyd infeasible')

    print "one norm boyd:"
    model_one_boyd = RobustGPModel(model, gamma, 'one norm', boyd=True)
    try:
        sol_model_one_boyd = model_one_boyd.solve(r_min=30, r_max=30, verbosity=1)
        if model_one_boyd.lower_approximation_used:
            printing_list.append('one norm boyd infeasible, lower approximation used:')
        printing_list.append("one norm boyd %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_one_boyd['cost'], gamma, model_one_boyd.setup_time,
                                sol_model_one_boyd['soltime']))
    except:
        printing_list.append('one norm boyd infeasible')
# -------------------------------------------------------------------------------------------------------------------------------------------------
    print "box cons:"
    model_box_cons = RobustGPModel(model, gamma, 'box', simple_model=True)
    try:
        sol_model_box_cons = model_box_cons.solve(r_min=30, r_max=30, verbosity=1)
        if model_box_cons.lower_approximation_used:
            printing_list.append('box cons infeasible, lower approximation used:')
        printing_list.append("box cons %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_box_cons['cost'], gamma, model_box_cons.setup_time,
                                sol_model_box_cons['soltime']))
    except:
        printing_list.append('box cons infeasible')

    print "ell cons:"
    model_ell_cons = RobustGPModel(model, gamma, 'elliptical', simple_model=True)
    try:
        sol_model_ell_cons = model_ell_cons.solve(r_min=30, r_max=30, verbosity=1)
        if model_ell_cons.lower_approximation_used:
            printing_list.append('ell cons infeasible, lower approximation used:')
        printing_list.append("elliptical cons %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_ell_cons['cost'], gamma, model_ell_cons.setup_time,
                                sol_model_ell_cons['soltime']))
    except:
        printing_list.append('elliptical cons infeasible')

    print "one norm cons:"
    model_one_cons = RobustGPModel(model, gamma, 'one norm', simple_model=True)
    try:
        sol_model_one_cons = model_one_cons.solve(r_min=30, r_max=30, verbosity=1)
        if model_one_cons.lower_approximation_used:
            printing_list.append('one norm cons infeasible, lower approximation used:')
        printing_list.append("one norm cons %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_one_cons['cost'], gamma, model_one_cons.setup_time,
                                sol_model_one_cons['soltime']))
    except:
        printing_list.append('one norm cons infeasible')
# -------------------------------------------------------------------------------------------------------------------------------------------------
    print "box :"
    model_box = RobustGPModel(model, gamma, 'box')
    try:
        sol_model_box = model_box.solve(r_min=30, r_max=30, verbosity=1)
        if model_box.lower_approximation_used:
            printing_list.append('box infeasible, lower approximation used:')
        printing_list.append("box %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_box['cost'], gamma, model_box.setup_time,
                                sol_model_box['soltime']))
    except:
        printing_list.append('box infeasible')

    print "ell:"
    model_ell = RobustGPModel(model, gamma, 'elliptical')
    try:
        sol_model_ell = model_ell.solve(r_min=30, r_max=30, verbosity=1)
        if model_ell.lower_approximation_used:
            printing_list.append('ell infeasible, lower approximation used:')
        printing_list.append("elliptical %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_ell['cost'], gamma, model_ell.setup_time,
                                sol_model_ell['soltime']))
    except:
        printing_list.append('elliptical infeasible')

    print "one norm:"
    model_one = RobustGPModel(model, gamma, 'one norm')
    try:
        sol_model_one = model_one.solve(r_min=30, r_max=30, verbosity=1)
        if model_one.lower_approximation_used:
            printing_list.append('one norm infeasible, lower approximation used:')
        printing_list.append("one norm %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_one['cost'], gamma, model_one.setup_time,
                                sol_model_one['soltime']))
    except:
        printing_list.append('one norm infeasible')
# -------------------------------------------------------------------------------------------------------------------------------------------------
    print "box two term:"
    model_box_two_term = RobustGPModel(model, gamma, 'box', two_term=True)
    try:
        sol_model_box_two_term = model_box_two_term.solve(r_min=30, r_max=30, verbosity=1)
        if model_box_two_term.lower_approximation_used:
            printing_list.append('box two term infeasible, lower approximation used:')
        printing_list.append("box two term %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_box_two_term['cost'], gamma, model_box_two_term.setup_time,
                                sol_model_box_two_term['soltime']))
    except:
        printing_list.append('box two term infeasible')

    print "ell two term:"
    model_ell_two_term = RobustGPModel(model, gamma, 'elliptical', two_term=True)
    try:
        sol_model_ell_two_term = model_ell_two_term.solve(r_min=30, r_max=30, verbosity=1)
        if model_ell_two_term.lower_approximation_used:
            printing_list.append('ell two term infeasible, lower approximation used:')
        printing_list.append("elliptical two term %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_ell_two_term['cost'], gamma, model_ell_two_term.setup_time,
                                sol_model_ell_two_term['soltime']))
    except:
        printing_list.append('elliptical two term infeasible')

    print "one norm two term:"
    model_one_two_term = RobustGPModel(model, gamma, 'one norm', two_term=True)
    try:
        sol_model_one_two_term = model_one_two_term.solve(r_min=30, r_max=30, verbosity=1)
        if model_one_two_term.lower_approximation_used:
            printing_list.append('one norm two term infeasible, lower approximation used:')
        printing_list.append("one norm two term %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model_one_two_term['cost'], gamma, model_one_two_term.setup_time,
                                sol_model_one_two_term['soltime']))
    except:
        printing_list.append('one norm two term infeasible')
# -------------------------------------------------------------------------------------------------------------------------------------------------
    print "deterministic:"
    try:
        sol_model = model.solve(verbosity=1)
        printing_list.append("deterministic %s, gamma = %s, setup time = %s, solve time = %s"
                             % (sol_model['cost'], gamma, 0, sol_model['soltime']))
    except:
        printing_list.append('deterministic infeasible')

for statement in printing_list:
    print(statement)
