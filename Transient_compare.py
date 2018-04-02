import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat


def print_outcomes(multi_cohort, strategy_name, alpha):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    survival_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_cohort.get_mean_total_reward(),
        interval=multi_cohort.get_PI_total_reward(alpha),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean rewards and {:.{prec}%} prediction interval:".format(1 - alpha, prec=0),
          survival_mean_PI_text)

def print_comparative_outcomes(cohort1, cohort2, alpha):
    """
    :param cohort1:
    :param cohort2:
    :return:
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean rewards',
        x=cohort1.get_all_total_rewards(),
        y_ref=cohort2.get_all_total_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=alpha),
        deci=1
    )
    print("Expected increase in mean rewards and {:.{prec}%} prediction interval:".format(1 - alpha, prec=0),
          estimate_CI)
