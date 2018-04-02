import scr.FormatFunctions as Format
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat


def print_outcomes(sim_output, strategy_name, alpha):
    """ prints the outcomes of a simulated cohort under steady state
    :param sim_output: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
     """

    # mean and confidence interval text of patient survival time
    reward_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean survival time (years) and {:.{prec}%} confidence interval:".format(1 - alpha, prec=0),
          reward_mean_CI_text)


def print_comparative_outcomes(cohort1, cohort2,alpha):
    """
    :param cohort1:
    :param cohort2:
    :return:
    """

    # increase in survival time
    increase = Stat.DifferenceStatIndp(
        name='Increase in rewards',
        x=cohort1.get_rewards(),
        y_ref=cohort2.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha),
        deci=1
    )
    print("Average increase in rewards and {:.{prec}%} confidence interval:".format(1 - alpha, prec=0),
          estimate_CI)

    # % increase in survival time
    relative_diff = Stat.RelativeDifferenceIndp(
        name='Average % increase in rewards',
        x=cohort1.get_rewards(),
        y_ref=cohort1.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_bootstrap_CI(alpha=alpha, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Average percentage increase in rewards and {:.{prec}%} confidence interval:".format(1 - alpha, prec=0),
          estimate_CI)