# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    # answerDiscount = 0.9
    # answerNoise = 0.2

    #To make the agent cross the bridge, we need to:

    #Either increase the discount (to emphasize future rewards and encourage reaching the high-reward state).
    #Or decrease the noise (to reduce the risk of unintended actions and make crossing the bridge safer).
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    #Prefer the close exit (+1), risking the cliff (-10):
    #To make the agent prefer the shorter path (close exit) while risking the cliff, we:
    #Use a high discount to emphasize rewards.
    #Use low noise to make movements deterministic (risk-taking).
    #Use a small or zero living reward to avoid discouraging the agent from taking actions.


    answerDiscount = 0.5
    answerNoise = 0.0
    answerLivingReward = -2.0

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    #Prefer the close exit (+1), but avoiding the cliff (-10):
    #To avoid the cliff while preferring the close exit:
    #Use a high discount for future rewards.
    #Set moderate noise to discourage risky movements.
    #Use a small or zero living reward to avoid discouraging actions.


    answerDiscount = 0.5
    answerNoise = 0.3
    answerLivingReward = -0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    #Prefer the distant exit (+10), risking the cliff (-10)
    #To make the agent take the risky, shorter path to the distant exit:
    #Use a very high discount to prioritize the larger future reward.
    #Use low noise to encourage deterministic movements.
    #Use a small or zero living reward to avoid discouraging the agent.
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    #Prefer the distant exit (+10), avoiding the cliff (-10)
    #To avoid the cliff while preferring the distant exit:
    #Use a high discount to emphasize future rewards.
    #Use moderate noise to discourage risky movements.
    #Use a small or zero living reward to avoid discouraging actions.
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    #To make the agent avoid all exits and the cliff:
    #Use a high living reward to make the agent prefer staying alive.
    #Use moderate discount to reduce the value of terminal states.
    #Use low noise to avoid accidental termination.

    answerDiscount = 0.1
    answerNoise = 0.2
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = None
    answerLearningRate = None
    # return answerEpsilon, answerLearningRate
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
