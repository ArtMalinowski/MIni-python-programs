import numpy as np
import pydoc
def read_data(filename):
    a = np.loadtxt(filename, dtype=float, skiprows=1)
    return a
    
def find_offset(year):
     a = np.where(x==year)
     b = int(a[0])
     return b 
    
 
def get_years(array, start_year, stop_year):
    y=find_offset(start_year)
    z=find_offset(stop_year)
    return(array[y:z])
    
def mean_temps(array):
    t1=np.mean(array[:, 1])
    t2=np.mean(array[:, 3])
    print("Mean winter temperature is", t1,"and mean summer temperature is",t2)
    return t1, t2
def main():
    a=get_years(x,1845,1900)
    b=get_years(x,1970,2011)
    c=mean_temps(a)
    d=mean_temps(b)
    print("Mean winter and summer temperatures for Victorian era:", c, "and for modern era", d)
    print("Difference between winter temperature is", c[0]-d[0], "and difference between summer temperature is", c[1]-d[1])
x=read_data("raintemp_1845_2011.csv")
w=find_offset(1845)
print(w)
z=find_offset(1846)
print(z)
k=get_years(x, 1850, 1855)
print(k)
mean_temps(x)
l=mean_temps(k)
print(l)
if __name__ == "__main__":
    main()
import meteo
pydoc.writedoc(meteo)