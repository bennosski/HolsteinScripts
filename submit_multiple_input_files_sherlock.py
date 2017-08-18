from numpy import *
import subprocess, time, os
import sys
import glob

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


#existing_files = os.listdir('outputfiles1/')
submit_ct = 0

#last_submitted = [0,0,0]
#last_submitted = loadtxt('last_submitted')
#print 'last_submitted ',last_submitted

#[i0,j0,k0]

skip = False


mu_map = load('../mu_map.npy')
[d1,d2,d3] = shape(mu_map)

def get_count(i,j,k):
    return i*d2*d3 + j*d3 + k

def get_ijk(c):
    i = c/(d2*d3)
    
    r = c%(d2*d3)
    j = r/d3

    k = (c%(d2*d3))%d3

    return i,j,k


#start = get_count(9,9,9)+1
#end = get_count(5,10,0)

#start = get_count(5,5,10)+1
start = get_count(0,0,0)
end = get_count(d1-1,d2-1,d3-1)+1


y = raw_input('confirm: all temp? \n  and did you create submit scripts')
if y!='y':
    1/0

for count in range(start, end):

            [i,j,k] = get_ijk(count)            


            #if j!=6:
            #    continue
            
            label = '_%d'%i+'_%d'%j+'_%d'%k
                        
            input_file_name = sys.argv[1]+'input'+label
            output_folder_name = sys.argv[2]+'output'+label
            
            if os.path.exists(output_folder_name):
                #files = glob.glob(output_folder_name+'/*Gtau0_u.dat')
                files = glob.glob(output_folder_name+'/*')
                #print output_folder_name+'len ',len(files)
                if len(files)<50:
                    print output_folder_name+' len ',len(files),' submitting'
                else:
                    continue
            
     
            '''    
            if j>1:
                continue
            '''

            #if os.path.exists(output_folder_name):
            #    continue

            
            print('submitting ',label)
            
            bash_command('sbatch ../submit_sherlock%d'%j + ' ' + input_file_name+' '+output_folder_name)

            submit_ct += 1
            
            #last_submitted = [i,j,k]
            #savetxt('last_submitted', last_submitted)
            
            time.sleep(0.05)


print(submit_ct)
