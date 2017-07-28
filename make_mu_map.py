from numpy import *

N = 100
W = 8.


folder = 1



if folder == 1:
    #outputfiles_l0p3
    omegas = [0.4,1.2,2.0]
    betas  = [0.8, 1.6, 2.4, 4.8, 8.0, 12.0, 16.0]
    lamb   = 0.3
    num_mus = 15

save('omegas',omegas)
save('betas',betas)
save('lamb', lamb)
save('N',N)


mu_map = zeros([len(omegas), len(betas), num_mus])


if folder == 1:
    mu_map_interpolated = load('mu_map_interpolated_l0p3.npy')
    
for i in range(len(omegas)):
    omega = omegas[i]
    for j in range(len(betas)):
        
        #mu_map[i,j,:] = linspace(-2.5-lamb*W,-lamb*W,num_mus)

        if folder == 1:
            mu_map[i,j,:] = mu_map_interpolated[i,j,:]
        
                                           
save('mu_map', mu_map)
print 'done saving mu map'
print shape(mu_map)
