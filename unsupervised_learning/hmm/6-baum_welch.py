#!/usr/bin/env python3
"""
This module contains a function that performs the Baum-Welch algorithm
for a hidden markov model
"""
import numpy as np


def forward(Observations, Emission, Transition, Initial):
    """
    Performs the forward algorithm for a hidden markov model
    """
    T = Observations.shape[0]
    M = Transition.shape[0]
    
    F = np.zeros((M, T))
    F[:, 0] = Initial.T * Emission[:, Observations[0]]
    
    for t in range(1, T):
        for j in range(M):
            F[j, t] = np.sum(F[:, t-1] * Transition[:, j]) * Emission[j, Observations[t]]
    
    return F


def backward(Observations, Emission, Transition, Initial):
    """
    Performs the backward algorithm for a hidden markov model
    """
    T = Observations.shape[0]
    M = Transition.shape[0]
    
    B = np.zeros((M, T))
    B[:, T-1] = 1
    
    for t in range(T-2, -1, -1):
        for j in range(M):
            B[j, t] = np.sum(Transition[j, :] * Emission[:, Observations[t+1]] * B[:, t+1])
    
    return B


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000):
    """
    Performs the Baum-Welch algorithm for a hidden markov model
    Observations: numpy.ndarray (T,) containing the index of the observation
    Transition: numpy.ndarray (M, M) initialized transition probabilities
    Emission: numpy.ndarray (M, N) initialized emission probabilities
    Initial: numpy.ndarray (M, 1) initialized starting probabilities
    iterations: number of times expectation-maximization should be performed
    Returns: the converged Transition, Emission, or None, None on failure
    """
    if not isinstance(Observations, np.ndarray) or len(Observations.shape) != 1:
        return None, None
    
    if not isinstance(Transition, np.ndarray) or len(Transition.shape) != 2:
        return None, None
    
    if not isinstance(Emission, np.ndarray) or len(Emission.shape) != 2:
        return None, None
    
    if not isinstance(Initial, np.ndarray) or len(Initial.shape) != 2:
        return None, None
    
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None
    
    T = Observations.shape[0]
    M, N = Emission.shape
    
    if Transition.shape[0] != M or Transition.shape[1] != M:
        return None, None
    
    if Initial.shape[0] != M or Initial.shape[1] != 1:
        return None, None
    
    for _ in range(iterations):
        F = forward(Observations, Emission, Transition, Initial)
        B = backward(Observations, Emission, Transition, Initial)
        
        xi = np.zeros((M, M, T-1))
        for t in range(T-1):
            denominator = np.sum(F[:, t] * B[:, t])
            for i in range(M):
                for j in range(M):
                    numerator = F[i, t] * Transition[i, j] * Emission[j, Observations[t+1]] * B[j, t+1]
                    xi[i, j, t] = numerator / denominator
        
        gamma = np.sum(xi, axis=1)
        gamma = np.hstack((gamma, np.sum(xi[:, :, T-2], axis=1).reshape((-1, 1))))
        
        Transition = np.sum(xi, axis=2) / np.sum(gamma[:, :-1], axis=1).reshape((-1, 1))
        
        denominator = np.sum(gamma, axis=1).reshape((-1, 1))
        for k in range(N):
            mask = (Observations == k)
            Emission[:, k] = np.sum(gamma[:, mask], axis=1)
        
        Emission = Emission / denominator
    
    return Transition, Emission
