import sys

def main(argc, argv):

    if argc != 2 and argc != 1:
        print('Wrong Number of Command Line Arguments.\n')
        print('The program should be invoked from the commandline as follows:\n')
        print('compute_a_posteriori <observations>\n')
        print('Example observations: CLCCCCCL')
    
    f = open('result.txt', 'w')

    # Adding the Default Probabilites to the File
    f.write('Observation sequence Q: {}\n'.format(argv[1]) )
    f.write('Length of Q: {}\n'.format(len(argv[1])) )
    f.write('After Observation 0: \n\n')
    f.write('P(h1 | Q) = 0.10000\n')
    f.write('P(h2 | Q) = 0.20000\n')
    f.write('P(h3 | Q) = 0.40000\n')
    f.write('P(h4 | Q) = 0.20000\n')
    f.write('P(h5 | Q) = 0.10000\n')
    f.write('Probability that the next candy we pick will be C, given Q: 0.50000\n')
    f.write('Probability that the next candy we pick will be L, given Q: 0.50000\n\n')

    if argc == 1:
        exit(0)

    # Defining the Probabilities
    ph1 = 0.1
    ph2 = 0.2
    ph3 = 0.4
    ph4 = 0.2
    ph5 = 0.1

    p_C_h1 = 1
    p_L_h1 = 0
    p_C_h2 = 0.75
    p_L_h2 = 0.25
    p_C_h3 = 0.5
    p_L_h3 = 0.5
    p_C_h4 = 0.25
    p_L_h4 = 0.75
    p_C_h5 = 0
    p_L_h5 = 1
    
    pC  = 0.5
    pL  = 0.5

    for i in range (0, len(argv[1])):
        if argv[1][i] == 'C':
            ph1 = (p_C_h1 * ph1) / (pC)
            ph2 = (p_C_h2 * ph2) / (pC)
            ph3 = (p_C_h3 * ph3) / (pC)
            ph4 = (p_C_h4 * ph4) / (pC)
            ph5 = (p_C_h5 * ph5) / (pC)  

        elif argv[1][i] == 'L':
            ph1 = (p_L_h1 * ph1) / (pL)
            ph2 = (p_L_h2 * ph2) / (pL)
            ph3 = (p_L_h3 * ph3) / (pL)
            ph4 = (p_L_h4 * ph4) / (pL)
            ph5 = (p_L_h5 * ph5) / (pL) 
        
        else:
            f.write('Wrong Observation {}: {}\n\n'.format(i+1, argv[1][i]))
            continue
        
        pC = (ph1 * p_C_h1) + (ph2 * p_C_h2) + (ph3 * p_C_h3) + (ph4 * p_C_h4) + (ph5 * p_C_h5)
        pL = (ph1 * p_L_h1) + (ph2 * p_L_h2) + (ph3 * p_L_h3) + (ph4 * p_L_h4) + (ph5 * p_L_h5)

        f.write('After Observation {}: {}\n\n'.format(i+1, argv[1][i]))
        f.write('P(h1 | Q) = {:.5f}\n'.format(ph1))
        f.write('P(h2 | Q) = {:.5f}\n'.format(ph2))
        f.write('P(h3 | Q) = {:.5f}\n'.format(ph3))
        f.write('P(h4 | Q) = {:.5f}\n'.format(ph4))
        f.write('P(h5 | Q) = {:.5f}\n'.format(ph5))
        f.write('Probability that the next candy we pick will be C, given Q: {:.5f}\n'.format(pC))
        f.write('Probability that the next candy we pick will be L, given Q: {:.5f}\n\n'.format(pL))
        
    
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)