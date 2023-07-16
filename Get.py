
import nibabel as nib
import nibabel.processing
import numpy as np
Atlas=nib.load('/aal.nii.gz')
func=nib.load('/bm20.nii.gz')
voxel_size= [2,2,2]
resampled_img=nibabel.processing.resample_to_output(Atlas,voxel_size)
nib.save(resampled_img, '/aal_2mm.nii.gz')

atlas=nib.load('/aal_2mm.nii.gz').get_fdata()
func = func.get_fdata()

gamma = [3,4,5,6,7,8]
for g in gamma:
    result=[]
    for i in range(20):
        values,ncounts=np.zeros(116),np.zeros(116)
        temp_func=func[:,:,:,i]
        for x in range(91):
            for y in range(109):
                for z in range(91):
                    node=int(atlas[x,y,z])
                    value=temp_func[x,y,z]
                    if value>0 and node>0:
                        values[node-1]+=1
                    if node>0:
                        ncounts[node-1]+=1
        result.append((values,ncounts))

    net=[]
    for i in range(20):
        values,ncounts = result[i][0],result[i][1]
        for value,ncount in zip(values,ncounts):
            net.append(value>=ncount*(g/10))
    ##print(net[348:463],len(net))
    net = np.array(net).reshape(20,116)

    np.save('/BM20_%s.npy'%str(g),net)
                    
# %%
