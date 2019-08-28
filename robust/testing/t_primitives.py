from robust.robust_gp_tools import RobustGPTools
from robust.robust import RobustModel
from robust.margin import MarginModel
from models import sp_test_model

def test_MarginModel():
    """ Tests creation and solution of MarginModel"""
    m = sp_test_model()
    mm = MarginModel(m, gamma = 0.5)
    margin_solution = mm.localsolve(verbosity=0)
    uncertain_varkeys = [k for k in m.varkeys if RobustGPTools.is_directly_uncertain(k)]
    # Checking margin allocation
    for key in list(uncertain_varkeys):
        assert(mm.substitutions.get(key) == m.substitutions.get(key) *
                                            (1.+mm.setting.get("gamma")*key.pr/100.))
    assert(margin_solution['cost'] >= mm.nominal_cost)

def test_conservativeness():
    """ Testing conservativeness of solution methods"""
    m = sp_test_model()
    sm = m.localsolve(verbosity=0)
    sem = RobustModel(m, 'elliptical').robustsolve(verbosity=0)
    smm = MarginModel(m).localsolve(verbosity=0)
    sbm = RobustModel(m, 'box').robustsolve(verbosity=0)
    assert(sm <= sem <= smm <= sbm)


def test():
    test_MarginModel()
    test_conservativeness()

if __name__ == "__main__":
    test()
