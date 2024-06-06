import shutil
import os 

starwise = "results/starwise/"
sourcewise = "results/sourcewise/"

sources = os.listdir(sourcewise)
plots = ["lightcurve.png","lk.png","phase_lc_1.png","phase_lc_2.png","phase_lc_3.png"]

for i in range(1,18):
    starwise_i = starwise+str(i)+"/"

    for source in sources:
        if os.listdir(sourcewise+source+"/"+str(i)+"/"):
            plots_path = sourcewise+source+"/"+str(i)+"/"+sorted(os.listdir(sourcewise+source+"/"+str(i)+"/"),reverse=True)[0]+"/" 

            for plot in plots:
                shutil.copy(plots_path+plot,starwise_i+source+"_"+plot)


        