def letra(msm):
    from time import sleep

    for i in msm:
        sleep(0.2)
        print(i, end='', flush=True)


letra('PROCESSANDO...')
