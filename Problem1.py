#Problem 1: Comparing outcomes in a steady-state scenario (Weight 1):
# Present to the casino’s owner the change and the percentage change in their reward
# if they use an unfair coin for which the probability of head is 45%.

import Classes as Cls
import scr.FigureSupport as figureLibrary
import Steady_compare as Support

population_size=1000

# create a cohort of patients for when the drug is not available
cohortFair = Cls.SetOfGames(
    id=1,
    prob_head=0.5,
    n_games=population_size)
# simulate the cohort
fairOutcome = cohortFair.simulation()

# create a cohort of patients for when the drug is available
cohortUnfair = Cls.SetOfGames(
    id=1,
    prob_head=0.45,
    n_games=population_size)
# simulate the cohort
unfairOutcome = cohortUnfair.simulation()

# print outcomes of each cohort
Support.print_outcomes(fairOutcome, 'When the coin is fair:',alpha=0.05)
Support.print_outcomes(unfairOutcome, 'When the unfair coin whose probability of head is 45%:',alpha=0.05)

# print comparative outcomes
Support.print_comparative_outcomes(fairOutcome, unfairOutcome,0.05)