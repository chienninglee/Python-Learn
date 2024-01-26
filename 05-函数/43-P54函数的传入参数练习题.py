def ClassTem(c,t):
    if t <= 37.5:
        print("welcome！请出示您的健康码以及72小时核酸证明，并配合测量体温！"
              f"体温测量中，您的体温是:{t}°,体温正常请进！")
    else:
        print("welcome！请出示您的健康码以及72小时核酸证明，并配合测量体温！"
              f"体温测量中，您的体温是:{t}°,需要隔离！")


ClassTem(int,37.6)