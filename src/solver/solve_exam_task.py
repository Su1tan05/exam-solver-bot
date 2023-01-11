import numpy as np

U = 380

def solve_first(first_params):
    P_nom = first_params[0] * 1000
    n_i = first_params[1]
    K_i= first_params[2]
    cosfi = first_params[3]

    f1 = np.rad2deg(np.arccos(cosfi)) 
    sinfi = np.sin(np.arccos(cosfi))
    tgf1 = np.tan(np.arccos(cosfi))

    P_priv_1 = P_nom
    P_priv_1_4 = P_nom * n_i

    P_sr_sm_1 = P_priv_1 * K_i
    P_sr_sm_1_4 = P_priv_1 * K_i * n_i
    Q_sr_sm = P_sr_sm_1 * tgf1
    Q_sr_sm_14 = P_sr_sm_1_4 * tgf1
    
    S_sr_sm_1 = np.sqrt(P_sr_sm_1**2 + Q_sr_sm**2)
    S_sr_sm_1_4 = np.sqrt(P_sr_sm_1_4**2 + Q_sr_sm_14**2)

    I_nom_1 = P_priv_1 / (np.sqrt(3) * U)

    # return all as string list with values names

    return f'fi = {f1}\n'\
           f'sinfi = {sinfi}\n'\
           f'tgfi = {tgf1}\n'\
           f'P_priv_1 = {P_priv_1} Вт\n'\
           f'P_priv_1_4 = {P_priv_1_4} Вт\n'\
           f'P_sr_sm_1 = {P_sr_sm_1} Вт\n'\
           f'P_sr_sm_1_4 = {P_sr_sm_1_4} Вт\n'\
           f'Q_sr_sm = {Q_sr_sm} Вт\n'\
           f'Q_sr_sm_14 = {Q_sr_sm_14} Вт\n'\
           f'S_sr_sm_1 = {S_sr_sm_1} Вт\n'\
           f'S_sr_sm_1_4 = {S_sr_sm_1_4} Вт\n'\
           f'I_nom_1 = {I_nom_1} А\n'\


def solve_second(second_params):
    P_nom = second_params[0] * 1000
    n_i = second_params[1]
    K_i= second_params[2]
    cosfi = second_params[3]

    f1 = np.rad2deg(np.arccos(cosfi)) 
    sinfi = np.sin(np.arccos(cosfi))
    tgf1 = np.tan(np.arccos(cosfi))

    P_priv_1 = P_nom
    P_priv_1_4 = P_nom * n_i

    P_sr_sm_1 = P_priv_1 * K_i
    P_sr_sm_1_4 = P_priv_1 * K_i * n_i
    Q_sr_sm = P_sr_sm_1 * tgf1
    Q_sr_sm_14 = P_sr_sm_1_4 * tgf1
    
    S_sr_sm_1 = np.sqrt(P_sr_sm_1**2 + Q_sr_sm**2)
    S_sr_sm_1_4 = np.sqrt(P_sr_sm_1_4**2 + Q_sr_sm_14**2)

    I_nom_1 = P_priv_1 / (np.sqrt(3) * U)

    # return all as string list with values names

    return f'fi = {f1}\n'\
           f'sinfi = {sinfi}\n'\
           f'tgfi = {tgf1}\n'\
           f'P_priv_1 = {P_priv_1} Вт\n'\
           f'P_priv_1_4 = {P_priv_1_4} Вт\n'\
           f'P_sr_sm_1 = {P_sr_sm_1} Вт\n'\
           f'P_sr_sm_1_4 = {P_sr_sm_1_4} Вт\n'\
           f'Q_sr_sm = {Q_sr_sm} Вт\n'\
           f'Q_sr_sm_14 = {Q_sr_sm_14} Вт\n'\
           f'S_sr_sm_1 = {S_sr_sm_1} Вт\n'\
           f'S_sr_sm_1_4 = {S_sr_sm_1_4} Вт\n'\
           f'I_nom_1 = {I_nom_1} А\n'