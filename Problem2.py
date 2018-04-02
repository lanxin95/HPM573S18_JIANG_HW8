#Problem 2: Comparing outcomes in a transient-state scenario (Weight 1):
# Present to the gambler the change in their reward
# if they use an unfair coin for which the probability of head is 45%.

import Classes as Cls
import Transient_compare as Support

# settings for transient-state simulation
NUM_SIM_COHORTS = 1000  # number of simulated cohorts used for making projections

# create multiple cohorts for when the drug is not available
multiCohortFair = Cls.MultipleGameSets(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    prob_head=0.5,  # [p, p, ...]
    n_games_in_a_set=10 # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
)
# simulate all cohorts
multiCohortFair.simulation()

# create multiple cohorts for when the drug is available
multiCohortunFair = Cls.MultipleGameSets(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    prob_head=0.45,  # [p, p, ...]
    n_games_in_a_set=10 # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
)
# simulate all cohorts
multiCohortunFair.simulation()
# print outcomes of each cohort
Support.print_outcomes(multiCohortFair, 'When the coin is fair:', 0.05)
Support.print_outcomes(multiCohortunFair,'When the unfair coin whose probability of head is 45%:', 0.05)

# print comparative outcomes
Support.print_comparative_outcomes(multiCohortFair, multiCohortunFair,0.05)